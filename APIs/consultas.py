import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://backup-mazzini.internal.timbrasil.com.br/opd/cws_grafana_json/"

headers = {
    "Vtoken": "9749d6ff559524cb80f8a650228aefb4d4bc3f4d6e4befee7068e60271290516"
}

response = requests.post(url, headers=headers, verify=False)

print("\nStatus: ", response.status_code)

dados = response.json()

with open("cw.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)
    
print("\nArquivo cw.json criado com sucesso!")

url2 = "https://backup-mazzini.internal.timbrasil.com.br/opd/linhasfo_grafana_json/"
response2 = requests.post(url2, headers=headers, verify=False)

print("\nStatus: ", response2.status_code)

dados2 = response2.json()

with open("linhasfo.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados2, arquivo, indent=4)

print("\nArquivo linhasfo.json criado com sucesso!")

url3 = "https://backup-mazzini.internal.timbrasil.com.br/opd/derivados_grafana_json/"
response3 = requests.post(url3, headers=headers, verify=False)

print("\nStatus: ", response3.status_code)

dados3 = response3.json()

with open("derivados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados3, arquivo, indent=4)

print("\nArquivo derivados.json criado com sucesso!")

url4 = "https://backup-mazzini.internal.timbrasil.com.br/opd/demandas_grafana_json/"
response4 = requests.post(url4, headers=headers, verify=False)

print("\nStatus: ", response4.status_code)

dados4 = response4.json()

with open("demandas.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados4, arquivo, indent=4)

print("\nArquivo demandas.json criado com sucesso!")