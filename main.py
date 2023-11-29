from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# Careful with the --no-sandbox cmd as it can come with security concerns
# Limits the severity of bugs encountered in the headless selenium instance
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage') # uses /tmp instead of shared memory
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.scrapethissite.com/pages/simple/'

driver.get(url)

soup = BeautifulSoup(driver.page_source, features='lxml')

country_info = {}

capitals_scrap = soup.find_all(name='span', attrs={'class': 'country-capital'})
capitals_list = []
for c in capitals_scrap:
  c = ''.join(c)
  capitals_list.append(c) 
countries = soup.find_all(name='h3')

for index, key in enumerate(countries):
  key = list(key.stripped_strings)
  key = ''.join(key)
  country_info.update({key: capitals_list[index]})
print(country_info)

driver.quit()