from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox()

driver.get('https://google.com')
time.sleep(10)
driver.close()