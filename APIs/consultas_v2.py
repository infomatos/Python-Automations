from fileinput import filename

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apis = [
    ("https://opd/cws_grafana_json/", "cw.json"),
    ("https://linhasfo_grafana_json/", "linhasfo.json"),
    ("https:/opd/derivados_grafana_json/", "derivados.json"),
    ("https://demandas_grafana_json/", "demandas.json"),
]

def consulta_api(url, nome_arquivo):
    headers = {
        "Vtoken": ""
    }

    response = requests.post(url, headers=headers, verify=False)

    print("\nStatus: ", response.status_code)

    dados = response.json()

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"\nArquivo {nome_arquivo} criado com sucesso!")

consulta_api("https://cws_grafana_json/", "cw.json")

consulta_api("https://linhasfo_grafana_json/", "linhasfo.json")

consulta_api("https://derivados_grafana_json/", "derivados.json")

consulta_api("https://demandas_grafana_json/", "demandas.json")
