from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from information.logging_config import setup_logging
import logging

# Initialize
setup_logging()

class InstagramBlocking:
    def __init__(self, browser):
        self.browser = browser

    def block_user(self, username_to_block):
        driver = self.browser.get_driver()
        wait = WebDriverWait(driver, 20)

        try:
            logging.info("Searching for Options button...")
            # Looking for the "Options" button
            more_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "svg[aria-label=\"Options\"]")
                ))
            more_button.click()
            logging.info("The Options button was pressed.")

            # Looking for the "Block" button
            logging.info("Searching for Block button...(first button)")
            block_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//button[normalize-space()=\"Block\"])[1]")))
            block_button.click()
            logging.info("The Block button was pressed.")

            # Looking for the "Block" button
            logging.info("Searching for Block button...(second button)")
            confirm_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//button[normalize-space()=\"Block\"])[2]")))
            confirm_button.click()
            logging.info(f"User {username_to_block} has been blocked!")

        except Exception as e:
            logging.error(f"An error occurred: {e}")
