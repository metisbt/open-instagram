import time
from info import username, password, backup_code
from browser import Browser, write_in_element
from selenium.webdriver.common.by import By
from xpath import get_xpath

def main():
    main_url = 'https://www.instagram.com/'
    mybrowser = Browser()  # ایجاد یک نمونه از کلاس Browser
    mybrowser.change_url(main_url)  # فراخوانی متد change_url
    user_element = mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'username'))  # استفاده از By.XPATH برای یافتن المان
    password_element = mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'password'))  # استفاده از By.XPATH برای یافتن المان
    write_in_element(username, user_element)
    write_in_element(password, password_element)
    time.sleep(3)
    mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'submit')).click()
    mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'backup_button')).click()
    time.sleep(3)
    bachkup_code__element = mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'verification'))  # استفاده از By.XPATH برای یافتن المان
    write_in_element(backup_code, bachkup_code__element)
    time.sleep(3)
    mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'confirm_button')).click()
    time.sleep(15)
    mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'save_login_button')).click()
    time.sleep(15)
    mybrowser.driver.find_element(By.XPATH, get_xpath('login', 'notif_button')).click()




if __name__ == '__main__':
    main()