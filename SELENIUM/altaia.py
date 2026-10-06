# https://altaia.internal.timbrasil.com.br/idp/login

from selenium import webdriver
import time
# from webdriver_manager.microsoft import EdgeChromiumDriverManager as MSEdgeDriverManager
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.common.by import By

# definindo navegador ...

navegador = webdriver.Edge()
navegador.get('https://timbrasil.sharepoint.com/teams/TIM_2bed067103af41e4be740e3a1b1208da/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fteams%2FTIM%5F2bed067103af41e4be740e3a1b1208da%2FDocumentos%20Compartilhados%2FCapacity%20Report%2FBASE%2FRVTools&viewid=9b8bff42%2Dc255%2D4dcb%2Dabb1%2Da0884b1f5fe3&CT=1765913220049&OR=OWA%2DNT%2DMail&CID=4187fc0e%2D784a%2D7889%2Db816%2Da145385be7a6&e=5%3A5bfc708b8787400e8762f84ae862b80f&sharingv2=true&fromShare=true&at=9&FolderCTID=0x0120002DFCFA3F44BBBC4992F6956DE4514C90')
navegador.maximize_window()
time.sleep(12)

navegador.find_element('').send_keys('F8091772')   
# edge_options = Options()
# edge_options.add_experimental_option('detach', True)

# #servico = Service(MSEdgeDriverManager)
# # OPCÃO A: Caminho manual do driver (substitua pelo seu caminho)
# servico = Service(executable_path='C:\\Users\\F8091772\\OneDrive - TIM\\PYTHON\\Automation\\SELENIUM\\msedgedriver.exe')
# # driver = webdriver.Chrome(service=service)

# navegador = webdriver.Edge(service=servico, options=edge_options)

# # acessando sistema

# navegador.get('https://altaia-interno.internal.timbrasil.com.br/idp/login')

# # fazendo login ...
# navegador.find_element('xpath', '//*[@id="inputUsername"]').send_keys('F8091772')
# navegador.find_element('xpath', '//*[@id="next"]').click()
# navegador.find_element('xpath', '//*[@id="inputPassword"]').send_keys('Development@2025.4')
# navegador.find_element('xpath', '//*[@id="login"]').click()