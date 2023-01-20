import time , requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

t=time.time()


chromedriver = "chromedriver"
option = webdriver.ChromeOptions()
#option.add_argument('headless')

caps = DesiredCapabilities().CHROME

#caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
caps["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(desired_capabilities=caps,options=option)

coins = ['ETH' , 'BTC' , 'SHIB' , 'DOGE' , 'TRX' , 'TON' , 'LTC' , 'XRP' , 'ADA' ]
times = [10,25,16,145,85,45,95,80,90,10]

link="https://www.kucoin.com/price/"

for i in coins :
    print(i)
    driver.execute_script("window.open('about:blank','"+i+"');")
    driver.switch_to.window(i)
    driver.get(link+i)
    time.sleep(3)
time.sleep(5)
print(coins)

prisid='//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/h2'
for i in range (100):
    time.sleep(0.5)
    txt=''
    for i in coins :
        driver.switch_to.window(i)
        time.sleep(1)
        try:
            ptxt=driver.find_element(By.XPATH,prisid)
            txt += ptxt.text.split('\n')[0].replace("$ ","").replace(",","") + '  ,  '
        except BaseException as er:
            print(er)
        #print(ptxt.text.split('\n')[0][2:])
    print(txt)
   