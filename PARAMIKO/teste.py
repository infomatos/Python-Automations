import os

caminho = r'C:\Users\F8091772\OneDrive - TIM\PYTHON\Automation\PARAMIKO'
nome_arquivos_master = ['RVTools_tabvCPU.csv', 'RVTools_tabvMemory.csv', 'RVTools_tabvDisk.csv', 'RVTools_tabvInfo.csv']

os.chdir(caminho)

### criar arquivos master
for nome in nome_arquivos_master:
    with open(nome, 'w', newline='', encoding='utf-8') as csvfile:
        pass
lista = []
lista = os.listdir()

## listar arquivos
print("\nListando arquivos da pasta..\n")
for arquivo in lista:
    print(arquivo)