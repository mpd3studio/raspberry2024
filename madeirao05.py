print("start")
import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--lang=pt-BR")
chrome_options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": {"width": 414, "height": 896, "pixelRatio": 3},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
})
chrome_options.add_argument('--headless')

driver_path = "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(5)

contador = 1

while (True):
    try:
        driver.get("https://www.google.com.br/")
        
        palavrabusca = [
            "santos protetores dos estados da Amazônia",
            "brasileiro rolls-royce cullinan black badge",
            "peixe cachorro pirandira",
            "Miss Bumbum Porto Velho",
            "vistoria reprovada por quilometragem",
            "Energisa atendimento whatsapp Rondônia",
            "Litorina da Estrada de Ferro Madeira-Mamoré",
            "amigo secreto pode ser ímpar",
            "cidade perdida de ratanaba memes",
            "madeiraoweb formula 1 ao vivo online live",
            "óleo de copaíba tuberculose",
            "bolo de tucumã com goiabada castanha e cumaru",
            "corpo esquartejado é jogado de carro",
            "nove lendas urbanas famosas na Amazônia",
            "proprietário tenta recuperar revólver 357 Magnum",
            "festa das novinhas vilhena",
            "plantio sem solo primeira produção hidropônica de Rondônia",
            "desafios da exploração de petróleo na bacia do Amapá",
            "escola no para cria estrategia para incentivo e formacao de leitores",
            "8 parques da Amazônia para entrar em contato com o meio ambiente",
            "menor morre baleada em cujubim durante discussao com o esposo",
            "lenda da mulher árvore",
            "farmacia popular acesso gratuito a medicamentos para diversos públicos",
            "mini atlas Marajoara"
        ]
        
        buscasorteada = (random.choice(palavrabusca))
        
        driver.find_element(by=By.XPATH, value='//*[@id="tsf"]/div[1]/div[1]/div[1]/div[1]/div/input').send_keys(buscasorteada)

        rTime = random.randint(1, 2)
        time.sleep(rTime)

        driver.find_element(by=By.XPATH, value='//*[@id="tsf"]/div[1]/div[1]/div[1]/div[1]/div/input').send_keys(Keys.RETURN)

        busca = 0
        while busca < 1:
            try:
                print(buscasorteada)
                
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                element = driver.find_element(by=By.XPATH, value='//a[contains(@href, "madeiraoweb")]')
                driver.execute_script("arguments[0].click();", element)
                
                rTime = random.randint(3, 59)
                time.sleep(rTime)
                
                nLink = random.randint(7, 26)
                actions = ActionChains(driver)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                actions.send_keys(Keys.TAB * nLink)
                actions.send_keys(Keys.RETURN)
                actions.perform()
                rTime = random.randint(3, 59)
                time.sleep(rTime)
                
                busca = 1

            except NoSuchElementException:
                
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                rTime = random.randint(1, 2)
                time.sleep(rTime)

                element = driver.find_element(by=By.XPATH, value='//*[@id="botstuff"]/div/div[2]/div[4]/a[1]/h3/div/span[2]')
                driver.execute_script("arguments[0].click();", element)

        driver.close()
        print(contador)
        hora = datetime.now()
        print(hora)
        print("********************************")
        contador = contador + 1
        
    except Exception as e:
        
        driver.close()
        print(contador)
        hora = datetime.now()
        print(hora)
        print("********************************###########error#")
        contador = contador + 1
