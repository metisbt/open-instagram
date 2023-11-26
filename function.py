from selenium.webdriver.common.by import By
from xpath import get_xpath
import time


def check_logged_in(browser):
    try:
        time.sleep(25)
        browser.driver.find_element(By.XPATH, get_xpath('home_page', 'direct_button'))
        return True
    except:
        print("you are not logged in!")
        return False