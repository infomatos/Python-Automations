from fileinput import filename

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apis = [
    ("https://backup-mazzini.internal.timbrasil.com.br/opd/cws_grafana_json/", "cw.json"),
    ("https://backup-mazzini.internal.timbrasil.com.br/opd/linhasfo_grafana_json/", "linhasfo.json"),
    ("https://backup-mazzini.internal.timbrasil.com.br/opd/derivados_grafana_json/", "derivados.json"),
    ("https://backup-mazzini.internal.timbrasil.com.br/opd/demandas_grafana_json/", "demandas.json"),
]

def consulta_api(url, nome_arquivo):
    headers = {
        "Vtoken": "9749d6ff559524cb80f8a650228aefb4d4bc3f4d6e4befee7068e60271290516"
    }

    response = requests.post(url, headers=headers, verify=False)

    print("\nStatus: ", response.status_code)

    dados = response.json()

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"\nArquivo {nome_arquivo} criado com sucesso!")

consulta_api("https://backup-mazzini.internal.timbrasil.com.br/opd/cws_grafana_json/", "cw.json")

consulta_api("https://backup-mazzini.internal.timbrasil.com.br/opd/linhasfo_grafana_json/", "linhasfo.json")

consulta_api("https://backup-mazzini.internal.timbrasil.com.br/opd/derivados_grafana_json/", "derivados.json")

consulta_api("https://backup-mazzini.internal.timbrasil.com.br/opd/demandas_grafana_json/", "demandas.json")