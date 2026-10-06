import requests
import urllib3

import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apis = [
    #("https:///cws_grafana_json/", "cw.csv"),
    #("https:///linhasfo_grafana_json/", "linhasfo.csv"),
    ("https://derivados_grafana_json/", "derivados.csv"),
    #("https:///opd/demandas_grafana_json/", "demandas.csv"),
]

caminho = "caminho-interno/ou-de-rede"

def transforma_json_em_csv(dados):
    registros = dados.get("queryset", dados) if isinstance(dados, dict) else dados
    df = pd.json_normalize(registros)

    if "valor_contrato" in df.columns:
        df = df.drop(columns=["valor_contrato"])

    return df

def consulta_api(url, nome_arquivo):
    headers = {
        "Vtoken": ""
    }

    response = requests.post(url, headers=headers, verify=False)

    print("\nStatus: ", response.status_code)

    dados = response.json()

    df = transforma_json_em_csv(dados)
    df.to_csv(f"{caminho}/{nome_arquivo}", index=False, encoding="utf-8-sig")
        

    print(f"\nArquivo {nome_arquivo} criado com sucesso!")

for url, nome_arquivo in apis:
    consulta_api(url, nome_arquivo)
    
print("\nTodos os arquivos foram criados com sucesso!")
