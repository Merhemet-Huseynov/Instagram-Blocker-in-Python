from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging_info.logging_config import setup_logging
import logging

# Initialize
setup_logging()

class ToUnblock:
    def __init__(self, browser):
        self.browser = browser
    
    def unblock_instagram(self, username_to_unblock):
        driver = self.browser.get_driver()
        wait = WebDriverWait(driver, 30)
    
        try:
            logging.info("Searching for Unblock button...(first button)")
            # Looking for the "Unblock" button
            unblock_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//div[@class=\"_ap3a _aaco _aacw _aad6 _aade\"])[1]")
                ))
            unblock_button.click()
            logging.info("The Unblock button was pressed.")

            # Looking for the "Unblock" button
            logging.info("Searching for Unblock button...(second button)")
            confirm_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, """/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]
                                /div[1]/div[1]/div[1]/div[1]/div[1]
                                    /div[1]/div[2]/button[1]""")
                ))
            confirm_button.click()
            logging.info(f"User {username_to_unblock} has been unblocked!")

        except Exception as e:
            logging.error(f"An error occurred: {e}")


