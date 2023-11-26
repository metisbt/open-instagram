from selenium import webdriver
import time

class Browser:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(180)

    def change_url(self, url: str):
        if self.driver.current_url != url:
            try:
                self.driver.get(url)
            except Exception:
                print("Url not found!")
                return False
        return True

    def close(self):
        self.driver.close()
        self.driver.quit()


def write_in_element(text, element):
    for char in text:
        element.send_keys(char)
        time.sleep(0.07)