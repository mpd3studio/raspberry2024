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
            "cidade perdida de ratanaba memes",
            "nove lendas urbanas famosas na Amazônia",
            "proprietário tenta recuperar revólver 357 Magnum",
            "festa das novinhas Vilhena",
            "plantio sem solo primeira produção hidropônica de Rondônia",
            "lenda do Uirapuru misticismo folclore",
            "Mini Atlas Marajoara",
            "livro imagens raras da Amazônia",
            "lendas esquecidas do folclore amazonico",
            "quem são as 4 musas no Musas do Teatro Amazonas",
            "meme apocalíptico o que significa e como surgiu",
            "Cinema Brasileiro filmes inspirados nos Estados da Região Norte",
            "cachoeira do rio Mandi Rondônia",
            "cine Super K o último cinema de rua de Boa Vista",
            "\"descubra de quem é o whatsapp\"",
            "\"Conheça a versatilidade culinária da ora-pro-nóbis amazônica\"",
            "\"Memórias Curiosas de Porto Velho\"",
            "\"Como preparar um autêntico Pato no Tucupi\"",
            "\"Café Robusta Amazônico Recebe Título de Patrimônio Cultural em Rondônia\"",
            "mari-mari fruta benefícios"
        ]
        
        buscasorteada = (random.choice(palavrabusca))
        
        rTime = random.randint(1, 2)
        time.sleep(rTime)
        
        search_input = driver.find_element(by=By.NAME, value='q')
        
        rTime = random.randint(1, 2)
        time.sleep(rTime)
        
        search_input.send_keys(buscasorteada)        
        
        rTime = random.randint(1, 2)
        time.sleep(rTime)

        search_input.send_keys(Keys.RETURN)
        
        rTime = random.randint(1, 2)
        time.sleep(rTime)

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
