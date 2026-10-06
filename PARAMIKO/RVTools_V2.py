import paramiko
import os
import traceback

caminho = r'C:\Users\F8091772\OneDrive - TIM\PYTHON\Automation\PARAMIKO'

##### credentials ######
servidor = '10.99.60.174'
user = 'root'
senha = 'infracloud2@23'

ARQUIVOS_ALVO = {
    'RVTools_tabvInfo.csv',
    'RVTools_tabvDisk.csv',
    'RVTools_tabvMemory.csv',
    'RVTools_tabvCPU.csv'
}

# Prefixo da pasta especial
PREFIXO_VCSA00 = 'vim-vm01-vcsa00.oss.timbrasil.com.br_'

ssh = None
sftp = None

try:
    # Garantir pasta local base
    try:
        os.makedirs(caminho, exist_ok=True)
    except Exception as e:
        print(f'[ERRO] Não consegui garantir a pasta local: {caminho}')
        print(f'       Motivo: {e}')

    ##### conection #######
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(servidor, username=user, password=senha, timeout=20)
        print('\nConectado ao servidor INFRACLOUD.\n')
    except Exception as e:
        print('[ERRO] Falha ao conectar via SSH.')
        print(f'       Motivo: {e}')
        raise

    ##### Acessar e guardar o diretório atual da semana #####
    try:
        stdin, stdout, stderr = ssh.exec_command('cd /home/rvtools/vmware/rvtools; ls -d */ -u')
        lista_dir = stdout.read().decode('utf-8', errors='replace').split()
        erro_dir = stderr.read().decode('utf-8', errors='replace').strip()

        if erro_dir:
            print(f'[ERRO] Erro ao listar diretórios semanais: {erro_dir}')

        if not lista_dir:
            raise RuntimeError('Nenhum diretório semanal retornado (lista vazia).')

        diretorio_semana = lista_dir[0].strip('/')
        print('Dirertório atual: ' + diretorio_semana + '\n')
    except Exception as e:
        print('[ERRO] Falha ao obter diretório da semana.')
        print(f'       Motivo: {e}')
        raise

    ##### Listando pastas de vCenters #####
    try:
        stdin, stdout, stderr = ssh.exec_command(
            f'cd /home/rvtools/vmware/rvtools/{diretorio_semana}; ls -d */ -u'
        )
        lista_vCenter = stdout.read().decode('utf-8', errors='replace').split()
        erro_vc = stderr.read().decode('utf-8', errors='replace').strip()

        if erro_vc:
            print(f'[ERRO] Erro ao listar vCenters: {erro_vc}')

        if not lista_vCenter:
            print('[AVISO] Nenhum vCenter encontrado nesse diretório semanal.')
            lista_vCenter = []
    except Exception as e:
        print('[ERRO] Falha ao listar pastas de vCenter.')
        print(f'       Motivo: {e}')
        lista_vCenter = []

    # Abre SFTP uma vez (se falhar, tenta sob demanda)
    try:
        sftp = ssh.open_sftp()
    except Exception as e:
        print('[AVISO] Não consegui abrir SFTP agora. Vou tentar abrir sob demanda.')
        print(f'        Motivo: {e}')
        sftp = None

    for vCenter in lista_vCenter:
        vCenter = vCenter.strip('/')

        # Lista arquivos dentro do vCenter
        try:
            stdin, stdout, stderr = ssh.exec_command(
                f'cd /home/rvtools/vmware/rvtools/{diretorio_semana}/{vCenter}; ls -u'
            )
            print('\nDiretório atual: ' + vCenter + '\n')

            arquivos = stdout.read().decode('utf-8', errors='replace').split()
            erro_ls = stderr.read().decode('utf-8', errors='replace').strip()
            if erro_ls:
                print(f'[ERRO] Erro ao listar arquivos do vCenter "{vCenter}": {erro_ls}')
                continue
        except Exception as e:
            print(f'[ERRO] Falha ao listar arquivos no vCenter "{vCenter}".')
            print(f'       Motivo: {e}')
            continue

        for arquivo in arquivos:
            if arquivo not in ARQUIVOS_ALVO:
                continue

            servidor_path = f'/home/rvtools/vmware/rvtools/{diretorio_semana}/{vCenter}/{arquivo}'

            # ✅ REGRA NOVA:
            # Se for vcsa00_XXXXXXXX, salva em subpasta separada e com nome original
            try:
                if vCenter.startswith(PREFIXO_VCSA00):
                    pasta_destino = os.path.join(caminho, vCenter)  # separado
                    os.makedirs(pasta_destino, exist_ok=True)
                    local_path = os.path.join(pasta_destino, arquivo)  # nome original
                else:
                    local_path = os.path.join(caminho, f'{vCenter}_{arquivo}')  # como você já fazia
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

    print('\nDownload finalizado. Arquivos baixados com sucesso.\n')

except Exception as e:
    print('\n[ERRO FATAL] O script encontrou um erro e não conseguiu continuar.')
    print(f'Motivo: {e}')
    print('\n--- STACKTRACE ---')
    print(traceback.format_exc())

finally:
    try:
        if sftp is not None:
            sftp.close()
    except Exception:
        pass

    try:
        if ssh is not None:
            ssh.close()
    except Exception:
        pass
