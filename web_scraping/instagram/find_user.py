from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_info.logging_config import setup_logging
import logging

# Initialize
setup_logging()

class FindUser:
    def __init__(self, browser):
        self.browser = browser

    def instagram_find_user(self, username):
        driver = self.browser.get_driver()
        logging.info(f"Logging in to the user page: https://www.instagram.com/{username}/")
        driver.get(f"https://www.instagram.com/{username}/")

        # Wait for the page to fully load
        wait = WebDriverWait(driver, 20)
        logging.info("Waiting for the page to fully load...")

        # Wait for the dynamic profile element
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        logging.info(f"{username} user found!")
