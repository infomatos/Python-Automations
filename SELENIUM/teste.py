from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# abrindo com o webdriver-manager
# O webdriver-manager baixa e gerencia o driver automaticamente
# service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
# driver = webdriver.Edge(service=service)

# travar o browser para não fechar
edge_option = Options()
edge_option.add_experimental_option('detach', True)
edge_option.add_argument("--start-maximized")

# Abrindo Edge local / caminho manual
service = EdgeService(executable_path=r"caminho-interno-navegador\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_option)

# Definindo um tempo para o navegador esperar carregar a pagina
wait = WebDriverWait(driver, 20)  # tempo máximo de espera

# acessando Altaia
driver.get("https://altaia.internal.empresa.com.br/portal/altaia")

# ===inserir usuário
input_user = wait.until(EC.element_to_be_clickable((By.ID, "inputUsername")))
input_user.send_keys('F8091772')

# clique no next e aguarde o campo senha aparecer
botao_next = wait.until(EC.element_to_be_clickable((By.ID, "next")))
botao_next.click()

# --- aguardar o carregamento do campo senha (pode ter redirecionamento ou AJAX) ---
input_pass = wait.until(EC.visibility_of_element_located((By.ID, "inputPassword")))
input_pass.send_keys('Development@2025.3')

# --- clicar no login ---
botao_login = wait.until(EC.element_to_be_clickable((By.ID, "login")))
botao_login.click()

# tenta clicar em qualquer elemento cujo id comece com "simpleMenuToURL"
btn_redeServicos = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@id,'simpleMenuToURL')]")))
btn_redeServicos.click
#driver.execute_script("arguments[0].scrollIntoView(true);", btn_redeServicos)
driver.execute_script("arguments[0].click();", btn_redeServicos)
        
# tenta clicar em qualquer elemento by xpath
btn_select_find = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/altaia-contexts-select-box-tree/altaia-select-box-tree/nossisui-dropdown-panel/div/div/div/div/div/ul/li")))
#driver.execute_script("arguments[0].scrollIntoView(true);", btn_select_find)
driver.execute_script("arguments[0].click();", btn_select_find)

# tenta inserir dado no campo by xpath
input_fild = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/bs-dropdown-container/div/ul/li/div[1]/div/fx-searchbox/div/input")))
#driver.execute_script("arguments[0].scrollIntoView(true);", input_fild)
input_fild.send_keys('Core CS Movel')

# --- clicar no login ---
clicar_CS_MOVEL = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(),'CORE CS Movel')]")))
#driver.execute_script("arguments[0].scrollIntoView(true);", clicar_CS_MOVEL)
driver.execute_script("arguments[0].click();", clicar_CS_MOVEL)

# Clicar fora
click_out = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/nossisui-header-entity/div[1]/div/h1")))
#driver.execute_script("arguments[0].scrollIntoView(true);", click_out)
driver.execute_script("arguments[0].click();", click_out)

# clicar no campo novamente
click_btn_find = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/altaia-contexts-select-box-tree/altaia-select-box-tree/nossisui-dropdown-panel/div/div/div/div/div/ul/li")))
#driver.execute_script("arguments[0].scrollIntoView(true);", click_btn_find)
driver.execute_script("arguments[0].click();", click_btn_find)

# --- clicar no CUDB ---
clicar_CUDB = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(),'CUDB')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", clicar_CUDB)
driver.execute_script("arguments[0].click();", clicar_CUDB)

# tenta clicar em qualquer elemento by xpath
btn_explorar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-home/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/nossisui-button-dropdown/div/button")))
#driver.execute_script("arguments[0].scrollIntoView(true);", btn_explorar)
driver.execute_script("arguments[0].click();", btn_explorar)

# tenta clicar em qualquer elemento by xpath
clik_performance_Cockpits = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/bs-dropdown-container/div/ul/li[2]/a")))
#driver.execute_script("arguments[0].scrollIntoView(true);", clik_performance_Cockpits)
driver.execute_script("arguments[0].click();", clik_performance_Cockpits)

# Fechar o navegador
#driver.quit()
#time.sleep(10)
