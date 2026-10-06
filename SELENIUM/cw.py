import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://backup-mazzini.internal.timbrasil.com.br/opd/cws_grafana_json/"
VTOKEN = "9749d6ff559524cb80f8a650228aefb4d4bc3f4d6e4befee7068e60271290516"

headers = {
    "vtoken": VTOKEN,
    "Content-Type": "application/json",
}

resp = requests.post(URL, headers=headers, json={}, verify=False, timeout=30)
# print("Status:", resp.status_code)
# print(resp.text[:2000])
if resp.status_code == 200:
    dados = resp.json()
    print("Dados recebidos com sucesso:")
    print("Número de registros:", len(dados))
    print("Imprimindo registros:")

    for registro in dados:
        print(registro)
    print(dados)
else:
    print("Erro na requisição:", resp.status_code, resp.text)