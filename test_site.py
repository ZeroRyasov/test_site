import time

import selenium.webdriver.chrome.options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
# 1. Зайти на страницу
# 2. найти поля ввода логин
# 3. найти поля ввода пароля
# 4. ввести логин
# 5. ввести пароль
# 6. найти поля кнопку входа
# 7. нажать на неё


def get_driver():
        chrome_options = selenium.webdriver.chrome.options.Options()
        chrome_options.add_argument("--window-size=1920,800")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=chrome_options)
        driver.implicitly_wait(10)
        return driver

def open_browers(driver, URL):
        driver.get(URL)

def get_element_by_id(driver, locator):
        return driver.find_element(By.ID, locator)

def element_sum_case(element, text):
        element.send_keys(text)

def login_button_click(button):
        return button.click()

def login_into(login, password):
        element_sum_case(get_element_by_id(driver, id_login), LOGIN)
        element_sum_case(get_element_by_id(driver, id_password), PASSWORD)
        login_button_click(get_element_by_id(driver,id_login_button))


URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'
id_login = 'user-name'
id_password =  'password'
id_login_button =  'login-button'

driver = get_driver()
open_browers(driver, URL)
login_into( LOGIN, PASSWORD )


driver.quit()
