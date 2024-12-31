from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from logging_info.logging_config import setup_logging
import logging

# Initialize
setup_logging()

class BrowserBot:
    def __init__(self):
        self.driver = None

    def open_chrome(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.google.com")
        logging.info("Google opened!")
        return self.driver

    def get_driver(self):
        if self.driver is None:
            raise Exception("Driver is not initialized. Call open_chrome first.")
        return self.driver