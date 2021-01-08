from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options


r = requests.get("https://sv.dhcnhn.vn/training/appregister")
print(r.status_code)

options = Options()
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options,executable_path="./chromedriver")

driver.get('https://sv.dhcnhn.vn/training/appregister')

while r.status_code != 200:
    time.sleep(20)
    driver.refresh()
driver.quit()