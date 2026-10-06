from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import traceback

def preencher_campo_com_fallback(driver, elemento, valor):
    
    try:
        elemento.click()
        elemento.clear()
        elemento.send_keys(valor)
        # pequena pausa para garantir que o JS que escuta 'input' capture a mudança
        time.sleep(0.2)
        # checar se valor foi inserido (algumas páginas transformam o valor)
        if elemento.get_attribute('value') != valor:
            # fallback: setar via JS e disparar eventos
            driver.execute_script(
                "arguments[0].value = arguments[1];"
                "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));"
                "arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
                elemento, valor
            )
            time.sleep(0.1)
    except Exception:
        # se algo falhar aqui, relança pra ser capturado pelo bloco externo
        raise

def main():
    try:
        # edge_options = Options()
        # edge_options.add_experimental_option('detach', True)
        # edge_options.add_argument("--start-maximized")
        # # opcional: rodar sem UI para testes: chrome_options.add_argument("--headless=new")

        # servico = Service(EdgeChromiumDriverManager().install())
        navegador = webdriver.Edge 
        # (service=servico, options=edge_options)

        wait = WebDriverWait(navegador, 20)  # tempo máximo de espera

        navegador.get('https://altaia-interno.internal.timbrasil.com.br/idp/login')

        # --- esperar e preencher usuário ---
        input_user = wait.until(EC.element_to_be_clickable((By.ID, "inputUsername")))
        preencher_campo_com_fallback(navegador, input_user, 'F8091772')

        # clique no next e aguarde o campo senha aparecer
        botao_next = wait.until(EC.element_to_be_clickable((By.ID, "next")))
        botao_next.click()

        # --- aguardar o carregamento do campo senha (pode ter redirecionamento ou AJAX) ---
        input_pass = wait.until(EC.visibility_of_element_located((By.ID, "inputPassword")))
        preencher_campo_com_fallback(navegador, input_pass, 'Development@2025.3')

        # --- clicar no login ---
        botao_login = wait.until(EC.element_to_be_clickable((By.ID, "login")))
        botao_login.click()

        # tenta clicar em qualquer elemento cujo id comece com "simpleMenuToURL"
        btn_redeServicos = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[starts-with(@id,'simpleMenuToURL')]")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", btn_redeServicos)
        navegador.execute_script("arguments[0].click();", btn_redeServicos)
        
        # tenta clicar em qualquer elemento by xpath
        btn_select_find = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/altaia-quality-management-home/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/altaia-contexts-select-box-tree/altaia-select-box-tree/nossisui-dropdown-panel/div/div/div/div/div/ul/li")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", btn_select_find)
        navegador.execute_script("arguments[0].click();", btn_select_find)

        # tenta inserir dado no campo by xpath
        input_fild = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/bs-dropdown-container/div/ul/li/div[1]/div/fx-searchbox/div/input")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", input_fild)
        preencher_campo_com_fallback(navegador, input_fild, 'Core CS Movel')

         # --- clicar no login ---
        clicar_CS_MOVEL = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(),'CORE CS Movel')]")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", clicar_CS_MOVEL)
        navegador.execute_script("arguments[0].click();", clicar_CS_MOVEL)

        # tenta clicar em qualquer elemento by xpath
        click_out = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/altaia-quality-management-home/nossisui-header-entity/div[1]/div/h1")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", click_out)
        navegador.execute_script("arguments[0].click();", click_out)

        # tenta clicar em qualquer elemento by xpath
        click_btn_find = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/altaia-quality-management-home/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/altaia-contexts-select-box-tree/altaia-select-box-tree/nossisui-dropdown-panel/div/div/div/div/div/ul/li")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", click_btn_find)
        navegador.execute_script("arguments[0].click();", click_btn_find)

         # --- clicar no login ---
        clicar_CUDB = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(),'CUDB')]")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", clicar_CUDB)
        navegador.execute_script("arguments[0].click();", clicar_CUDB)

        # tenta clicar em qualquer elemento by xpath
        btn_explorar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/altaia-quality-management-home/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/nossisui-button-dropdown/div/button")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", btn_explorar)
        navegador.execute_script("arguments[0].click();", btn_explorar)

        # tenta clicar em qualquer elemento by xpath
        clik_performance_Cockpits = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/bs-dropdown-container/div/ul/li[2]/a")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", clik_performance_Cockpits)
        navegador.execute_script("arguments[0].click();", clik_performance_Cockpits)

        # # tenta clicar em qualquer elemento by xpath
        # btn_select_find = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/altaia-app/altaia-quality-management-main/altaia-quality-management-home/div[1]/altaia-quality-management-context-explorer/altaia-context-explorer/div/div/altaia-contexts-select-box-tree/altaia-select-box-tree/nossisui-dropdown-panel/div/div/div/div/div/ul/li")))
        # navegador.execute_script("arguments[0].scrollIntoView(true);", btn_select_find)
        # navegador.execute_script("arguments[0].click();", btn_select_find)

        

        # # tenta clicar em qualquer elemento by xpath
        # btn_select_find = wait.until(EC.element_to_be_clickable((By.XPATH, "")))
        # navegador.execute_script("arguments[0].scrollIntoView(true);", btn_select_find)
        # navegador.execute_script("arguments[0].click();", btn_select_find)


        # opcional: aguardar uma condição que indica sucesso (ex.: URL muda ou elemento do dashboard)
        # wait.until(EC.url_contains("seu-dashboard-ou-outra-parte-da-app"))

    except Exception as e:
        print("Erro durante automação:", e)
        traceback.print_exc()
        try:
            # salva screenshot para análise
            navegador.save_screenshot("erro_altaia.png")
            print("Screenshot salva como erro_altaia.png")
        except Exception as se:
            print("Não foi possível salvar screenshot:", se)
    finally:
        # não fecha o navegador por causa do detach
        pass

if __name__ == "__main__":
    main()
