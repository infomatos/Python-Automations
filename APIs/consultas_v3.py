import requests
import urllib3

import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apis = [
    #("https://backup-mazzini.internal.timbrasil.com.br/opd/cws_grafana_json/", "cw.csv"),
    #("https://backup-mazzini.internal.timbrasil.com.br/opd/linhasfo_grafana_json/", "linhasfo.csv"),
    ("https://backup-mazzini.internal.timbrasil.com.br/opd/derivados_grafana_json/", "derivados.csv"),
    #("https://backup-mazzini.internal.timbrasil.com.br/opd/demandas_grafana_json/", "demandas.csv"),
]

caminho = "C:\\Users\\F8091772\\TIM\\NFV Infrastructure - Consumo Contratos (Base KS)"

def transforma_json_em_csv(dados):
    registros = dados.get("queryset", dados) if isinstance(dados, dict) else dados
    df = pd.json_normalize(registros)

    if "valor_contrato" in df.columns:
        df = df.drop(columns=["valor_contrato"])

    return df

def consulta_api(url, nome_arquivo):
    headers = {
        "Vtoken": "9749d6ff559524cb80f8a650228aefb4d4bc3f4d6e4befee7068e60271290516"
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
