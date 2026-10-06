import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://caminhoAPI/opd/cws_grafana_json/"
VTOKEN = ""

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
