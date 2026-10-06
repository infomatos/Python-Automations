from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager;
from selenium.webdriver.chrome.service import Service;
from selenium.webdriver.chrome.options import Options;
from selenium.webdriver.common.by import By;

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get('https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_videoselenium&_gl=1*1yxxdxr*_gcl_au*MTUxNTQyMjc1OC4xNzYxMzExOTk0LjEzNzQ2MTI3NTQuMTc2MTc1NzE4NS4xNzYxNzU3MTg1')

navegador.find_element('xpath', '//*[@id="BotaoPopup2"]').click()

navegador.find_element('xpath', '//*[@id="firstname"]').send_keys('Elias Martins')

navegador.find_element('xpath', '//*[@id="email"]').send_keys("eliasmatos@ymail.com")

navegador.find_element('xpath', '//*[@id="phone"]').send_keys('2199999-8888')

navegador.find_element('xpath', '//*[@id="_form_1925_submit"]').click()