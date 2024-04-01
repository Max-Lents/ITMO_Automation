import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
time.sleep(3)

button = driver.find_element(By.CSS_SELECTOR, 'form > input#login-button')
if button is None:
    print('Элеммент не найден')
else:
    print('Элемент найден')

username = driver.find_element(By.CSS_SELECTOR, 'form > .form_group input#user-name')
if username is None:
    print('Элеммент не найден')
else:
    print('Элемент найден')

password = driver.find_element(By.CSS_SELECTOR, 'form > .form_group input#password')
if password is None:
    print('Элеммент не найден')
else:
    print('Элемент найден')