import requests 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def run():

    url = 'https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_de_Conmebol_para_la_Copa_Mundial_de_F%C3%BAtbol_de_2022'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver=webdriver.Chrome(executable_path=r'C:\Users\mikem\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver.exe')
    driver.get(url)

    time.sleep(5)
    
    local = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[5]/th[1]/a').text
    visitante = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[5]/th[2]/a').text
    marcador = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[5]/td[4]/a/b').text
    
    print('Local: ' + str(local))
    print('Visitante: ' + str(visitante))
    print('Marcador: ' + str(marcador))

run()