from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPageNavigator:
    def __init__(self, driver_path, initial_url):
        self.driver_path = driver_path = "/usr/bin/chromedriver"
        self.initial_url = initial_url
        self.driver = None

    def open(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.initial_url)

    def navigate_to(self, url):
        if self.driver:
            self.driver.get(url)

    def click_element(self, by, value):
        if self.driver:
            element = self.driver.find_element(by, value)
            element.click()

    def enter_text(self, by, value, text):
        if self.driver:
            element = self.driver.find_element(by, value)
            element.clear()
            element.send_keys(text)

    def submit_form(self, by, value):
        if self.driver:
            element = self.driver.find_element(by, value)
            element.submit()

    def wait_for_element(self, by, value, timeout=10):
        if self.driver:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located((by, value)))

    def close(self):
        if self.driver:
            self.driver.quit()

# Example usage
if __name__ == "__main__":
    driver_path = "/path/to/chromedriver"  # Provide the path to your ChromeDriver
    initial_url = "https://example.com"
    navigator = WebPageNavigator(driver_path, initial_url)

    try:
        navigator.open()
        navigator.open()

        navigator.navigate_to("https://google.com")
        navigator.enter_text(By.NAME, "search", "web scraping")
        navigator.submit_form(By.ID, "search-form")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        navigator.close()
