# https://altaia.internal.empresa.com.br/idp/login

from selenium import webdriver
import time
# from webdriver_manager.microsoft import EdgeChromiumDriverManager as MSEdgeDriverManager
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.common.by import By

# definindo navegador ...

navegador = webdriver.Edge()
navegador.get('https://site.com')
navegador.maximize_window()
time.sleep(12)

navegador.find_element('').send_keys('FXXXXXXX')   
# edge_options = Options()
# edge_options.add_experimental_option('detach', True)

# #servico = Service(MSEdgeDriverManager)
# # OPCÃO A: Caminho manual do driver (substitua pelo seu caminho)
# servico = Service(executable_path='caminholocal-do-arquivo-navegador\\msedgedriver.exe')
# # driver = webdriver.Chrome(service=service)

# navegador = webdriver.Edge(service=servico, options=edge_options)

# # acessando sistema

# navegador.get('https://altaia-interno.internal.empresa.com.br/idp/login')

# # fazendo login ...
# navegador.find_element('xpath', '//*[@id="inputUsername"]').send_keys('FXXXXXXX)
# navegador.find_element('xpath', '//*[@id="next"]').click()
# navegador.find_element('xpath', '//*[@id="inputPassword"]').send_keys('Senha')
# navegador.find_element('xpath', '//*[@id="login"]').click()
