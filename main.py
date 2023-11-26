import time
from info import username, password, backup_code
from browser import Browser, write_in_element, not_now
from selenium.webdriver.common.by import By
from xpath import get_xpath
from function import check_logged_in
import os.path

def login(browser):
    while True:
        try:
            user_element = browser.driver.find_element(By.XPATH, get_xpath('login', 'username'))  # استفاده از By.XPATH برای یافتن المان
            password_element = browser.driver.find_element(By.XPATH, get_xpath('login', 'password'))  # استفاده از By.XPATH برای یافتن المان
            write_in_element(username, user_element)
            write_in_element(password, password_element)
            time.sleep(3)
            browser.driver.find_element(By.XPATH, get_xpath('login', 'submit')).click()
            browser.driver.find_element(By.XPATH, get_xpath('login', 'backup_button')).click()
            time.sleep(3)
            bachkup_code__element = browser.driver.find_element(By.XPATH, get_xpath('login', 'verification'))  # استفاده از By.XPATH برای یافتن المان
            write_in_element(backup_code, bachkup_code__element)
            time.sleep(3)
            browser.driver.find_element(By.XPATH, get_xpath('login', 'confirm_button')).click()
            not_now(browser.driver, get_xpath('login', 'save_login_button'))
            not_now(browser.driver, get_xpath('login', 'notif_button'))
        except Exception as e:
            print(f"Error: {e}")
        else:
            browser.save_cookies(username)
            

def main():
    main_url = 'https://www.instagram.com/'
    mybrowser = Browser()  # ایجاد یک نمونه از کلاس Browser
    mybrowser.change_url(main_url)  # فراخوانی متد change_url

    if os.path.isfile(f'cookies/{username}.pkl'):
        mybrowser.load_cookies(username)
        not_now(mybrowser.driver, get_xpath('login', 'notif_button'))
        time.sleep(3)
        if check_logged_in(mybrowser):
            mybrowser.change_url('https://www.instagram.com/direct/inbox/')
        else:
            login(mybrowser)
    else:
        login(mybrowser)






if __name__ == '__main__':
    main()