from selenium import webdriver

class Browser:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

    def change_url(self, url):
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