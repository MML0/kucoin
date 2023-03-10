import time , requests , datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chromedriver = "chromedriver"
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('log-level=3')
caps = DesiredCapabilities().CHROME

#caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(desired_capabilities=caps,options=option)



link="https://www.kucoin.com/markets"

driver.get(link)

time.sleep(10)


rowxpath='//*[@id="root"]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/table/tbody/tr[' #2]'
btnxpath = '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/nav/ul/li[11]/button'


chart_xpath = '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/table/tbody'
btn_1 = '//*[@id="root"]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/nav/ul/li[2]/button'

wait_time = 0.8
t=time.time()
all_data = [] 
csv_data = ''
for i in range (5):
    coins=[]
    prices = []
    for j in range (25):
        try:
            ptxt=driver.find_element(By.XPATH,chart_xpath)
            #print(len( ptxt.text.split('Details\nTrade')))
            txt = ptxt.text
            for k in range (30):
                if txt.split('Details\nTrade')[k].split('\n')[0] == '':
                    coins += [txt.split('Details\nTrade')[k].split('\n')[1]]#,txt.split('Details\nTrade')[k].split('\n')[3]]
                    prices += [[txt.split('Details\nTrade')[k].split('\n')[1],txt.split('Details\nTrade')[k].split('\n')[3].replace("$ ","").replace(",","")]]

                else:
                    coins += [txt.split('Details\nTrade')[k].split('\n')[0]]#,txt.split('Details\nTrade')[k].split('\n')[2]]
                    prices += [[txt.split('Details\nTrade')[k].split('\n')[0],txt.split('Details\nTrade')[k].split('\n')[2].replace("$ ","").replace(",","")]]
                csv_data += str(prices[-1][1].replace("$ ","").replace(",","")) + ','
            print(coins[-1])
            
            btn = driver.find_element(By.XPATH , btnxpath)
            btn.click()
            time.sleep(wait_time)
        except BaseException as er:
            print(er)
    csv_data += str(datetime.datetime.now()) + ',' + str(time.time()-t) + '\n'

    btn1 = driver.find_element(By.XPATH , btn_1)
    btn1.click()
    all_data += [prices,time.time()]
    time.sleep(2)

csv_data = str(coins)[1:-1] + ', time , time (s)\n' + csv_data



print(time.time()-t)

'''
a = open('data.txt','w')
a.write(str(coins)+'\n'+str(all_data)) 
a.close
'''
a = open('all_data.csv','w')
a.write(csv_data) 
a.close

print(len(coins))
print('set:',len(set(coins)))
#print(coins)
