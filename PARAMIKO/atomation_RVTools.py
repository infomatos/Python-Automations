import paramiko
import os

caminho = r'C:\Users\F8091772\TIM\NFV Infrastructure - RVTools'
# Prefixo da pasta 00
PREFIXO_VCSA00 = 'nome-do-vCenter'

##### credentials ######
servidor = '00.00.00.000'
user = 'root'
senha = 'senha'

##### conection #######
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(servidor, username=user, password=senha)

print('\nConectado ao servidor NOMESERVIDOR.\n')

##### INICIO DO PRIMEIRO ATO (Baixar os arquivos e reuni-los em um unico local) #########

##### Acessar e guardar o diretório atual da semana #####
stdin, stdout, stderr = ssh.exec_command('cd /caminho; ls -d */ -u')
lista_dir = stdout.read().decode('utf-8').split()
diretorio_semana = lista_dir[0].strip('/')
print('Dirertório atual: ' + diretorio_semana + '\n')

##### Listando pastas de vCenters #####
stdin, stdout, stderr = ssh.exec_command(
    f'cd /caminho/{diretorio_semana}; ls -d */ -u'
    )
lista_vCenter = stdout.read().decode('utf-8').split()

for vCenter in lista_vCenter:
    vCenter = vCenter.strip('/') # remove barra final
   
    #### Lista arquivos dentro do vCenter
    stdin, stdout, stderr = ssh.exec_command(
        f'cd /caminho/{diretorio_semana}/{vCenter}; ls -u'
        )
    print('\nDiretório atual: ' + vCenter + '\n')
    arquivos = stdout.read().decode('utf-8').split()

    for arquivo in arquivos:
        try: 
            if (arquivo == 'RVTools_tabvInfo.csv' or arquivo == 'RVTools_tabvDisk.csv' or arquivo == 'RVTools_tabvMemory.csv' or arquivo == 'RVTools_tabvCPU.csv'):
                sftp = ssh.open_sftp()
            
            #### caminho no servidor
                servidor_path = f'/caminho/{diretorio_semana}/{vCenter}/{arquivo}'
            
            # Se for vcsa00_XXXXXXXX, salva em subpasta separada e com nome original
                try:
                    if vCenter.startswith(PREFIXO_VCSA00):
                        pasta_destino = os.path.join(caminho, 'Arquivos_Unificados')  # separado
                        os.makedirs(pasta_destino, exist_ok=True)
                        local_path = os.path.join(pasta_destino, arquivo)  # nome original
                    else:
                        local_path = os.path.join(caminho, f'{vCenter}_{arquivo}') 
                except Exception as e:
                    print(f'[ERRO] Falha ao preparar caminho local para "{arquivo}" ({vCenter}).')
                    print(f'       Motivo: {e}')
                    continue

                try:
                    if sftp is None:
                        sftp = ssh.open_sftp()

                    sftp.get(servidor_path, local_path)
                    print(f'Arquivo {arquivo} baixado.')
                except Exception as e:
                    print(f'[ERRO] Falha ao baixar "{arquivo}" do vCenter "{vCenter}".')
                    print(f'       Servidor: {servidor_path}')
                    print(f'       Local:    {local_path}')
                    print(f'       Motivo:   {e}')
                    try:
                        if sftp is not None:
                            sftp.close()
                    except Exception:
                        pass
                    sftp = None
                    continue
        except Exception as e:
            print('ERRO: ', {e})
            
#### baixar os dois arquivos fora daas pastas
stdin, stdout, stderr = ssh.exec_command(
    f'cd /caminho/{diretorio_semana}; ls *.csv'
    )
files = stdout.read().decode('utf-8').split()
for f in files:
    sftp = ssh.open_sftp()
    servidor_path = f'/caminho/{diretorio_semana}/{f}'
    
    local_path = os.path.join(caminho, f'{f}')
    
    sftp.get(servidor_path, local_path)
    print('\nArquivo: ' + f + ' baixado.')   
    sftp.close()
print('\nDownload finalizado. Arquivos baixados com sucesso.\n')
#### FIM DO PRIMEIRO ATO ######


##### ATO 2 - Unificar e descartar fontes #####
import shutil

print('\nIniciando unificação de arquivos...\n')

pasta_consolidada = os.path.join(caminho, 'Arquivos_Unificados')
os.makedirs(pasta_consolidada, exist_ok=True)

arquivos_alvo = {
    'RVTools_tabvInfo.csv',
    'RVTools_tabvDisk.csv',
    'RVTools_tabvMemory.csv',
    'RVTools_tabvCPU.csv'
}

def garantir_quebra_de_linha_no_final(path_destino: str):
    if not os.path.exists(path_destino) or os.path.getsize(path_destino) == 0:
        print('Arquivo vazio ou inexistente.\n')
        return
    with open(path_destino, 'rb') as f:
        f.seek(-1, os.SEEK_END)
        ultimo = f.read(1)
    if ultimo not in (b'\n', b'\r'):
        with open(path_destino, 'ab') as f:
            f.write(b'\n')

processados = 0
erros = 0

for nome in os.listdir(caminho):
    src = os.path.join(caminho, nome)

    # ignora pastas e ignora tudo que estiver dentro de Arquivos_para_Upar
    if os.path.isdir(src) or nome == 'Arquivos_Unificados':
        continue

    # só pega arquivos que terminam com um dos 4 alvos (os que têm prefixo do vCenter)
    alvo = next((a for a in arquivos_alvo if nome.endswith(a)), None)
    if not alvo:
        continue

    # destino sempre é o arquivo "original" dentro da pasta consolidada
    dest = os.path.join(pasta_consolidada, alvo)

    try:
        with open(src, 'rb') as fsrc:
            header = fsrc.readline()  # linha 1 (cabeçalho)

            if not os.path.exists(dest):
                # se ainda não existe o consolidado, cria com o cabeçalho + resto do arquivo
                with open(dest, 'wb') as fdst:
                    fdst.write(header)
                    shutil.copyfileobj(fsrc, fdst)
            else:
                # se já existe, só anexa a partir da linha 2
                garantir_quebra_de_linha_no_final(dest)
                with open(dest, 'ab') as fdst:
                    shutil.copyfileobj(fsrc, fdst)

        os.remove(src)  # descarta fonte
        processados += 1
        print(f'[OK] Unificado e removido: {nome} -> {alvo}')

    except Exception as e:
        erros += 1
        print(f'[ERRO] Falha ao unificar/remover {nome}: {e}')

print(f'\nATO 2 finalizado. Processados: {processados} | Erros: {erros}\n')
