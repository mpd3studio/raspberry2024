print("start")
import time
import random
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--incognito")
options.add_argument("--lang=pt-BR")
options.add_experimental_option("mobileEmulation", {
    "deviceMetrics": {"width": 414, "height": 896, "pixelRatio": 3},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
})
options.add_argument('--headless')

driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
driver.implicitly_wait(5)

contador = 1

while (True):
    try:
        driver.get("https://www.google.com.br/")
        
        palavrabusca = [
            # Your list of search terms
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
