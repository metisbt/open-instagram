from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

class Browser:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(180)

    def change_url(self, url):
        if self.driver.current_url != url:
            try:
                self.driver.get(url)
            except Exception as url_err:
                print(f"Error: {url_err}")
                return False
        return True

    def close(self):
        self.driver.close()
        self.driver.quit()

    def save_cookies(self, username):
        try:
            with open (f'cookies/{username}.pkl', 'wb') as cookeis_file:
                pickle.dump(self.driver.get_cookies(), cookeis_file)

            return True
        except Exception as error:
            print(f"Error: {error}")
            return False
    
    def load_cookies(self, username):
        with open (f'cookies/{username}.pkl', 'rb') as cookeis_file:
            cookies = pickle.load(cookeis_file)

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()


def not_now(browser, element):
    time.sleep(1)
    button = browser.find_element(By.XPATH, element)
    button.click()

def write_in_element(text, element):
    for char in text:
        element.send_keys(char)
        time.sleep(0.07)