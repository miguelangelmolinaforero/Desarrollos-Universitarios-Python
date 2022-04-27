import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.latam.com/es_co/apps/personas/booking?fecha1_dia=01&fecha1_anomes=2020-12&fecha2_dia=31&fecha2_anomes=2020-12&from_city2=CLO&to_city2=BOG&auAvailability=1&ida_vuelta=ida_vuelta&vuelos_origen=Bogot%C3%A1&from_city1=BOG&vuelos_destino=Cali&to_city1=CLO&flex=1&vuelos_fecha_salida_ddmmaaaa=01/12/2020&vuelos_fecha_regreso_ddmmaaaa=31/12/2020&cabina=Y&nadults=1&nchildren=0&ninfants=0&cod_promo=&stopover_outbound_days=0&stopover_inbound_days=0#/'
agent = {'User-Agent':'Chrome/85.0'}
r = requests.get(url, headers=agent)

driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=r'C:\Users\mikem\.wdm\drivers\chromedriver\win32\85.0.4183.87\chromedriver.exe')
driver.get(url)

time.sleep(25)

vuelos = driver.find_elements_by_xpath('//li[@class="flight"]')
vuelo = vuelos[0]
salida = vuelo.find_element_by_xpath('.//div[@class="departure"]/time').get_attribute('datetime')
print("Cargando vuelos...")
print()
print(salida)
