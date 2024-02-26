# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:44:27 2024

@author: ziakh
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")
service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://laureltreepropertymanagement.nesthub.com')
driver.minimize_window()
page = driver.current_url

# print(driver.page_source)
ele = driver.find_element(By.CSS_SELECTOR,"h1")

for element in ele:
    print(element);