import csv

# Leitura de um arquivo CSV
with open('dados.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv) # Ou csv.DictReader para cabeçalhos
    cabecalho = next(leitor_csv) # Pula a linha do cabeçalho
    print(f"Cabeçalho: {cabecalho}")
    for linha in leitor_csv:
        print(linha) # Cada linha é uma lista de strings

# Escrita de um arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 30, 'São Paulo'],
    ['Bob', 25, 'Rio de Janeiro']
]
with open('saida.csv', 'w', newline='', encoding='utf-8') as arquivo_saida:
    escritor_csv = csv.writer(arquivo_saida)
    escritor_csv.writerows(dados) # Escreve todas as linhas


# SBC é diários