import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')
time.sleep(3)

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элеммент не найден')
else:
    print('Элемент найден')
