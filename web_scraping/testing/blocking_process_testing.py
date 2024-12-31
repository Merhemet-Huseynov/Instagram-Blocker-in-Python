import logging

class InstagramBlocking:
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.get_driver()
        self.logger = logging.getLogger("root")

    def block_user(self, username):
        try:
            # Searching for the "Options" button and blocking the user
            self.logger.info(f"Searching for Options button...")
            options_button = self.driver.find_element(By.CSS_SELECTOR, "svg[aria-label=\"Options\"]")
            options_button.click()
            
            # Presses the first block button
            block_button_1 = self.driver.find_element(By.XPATH, "(//button[normalize-space()=\"Block\"])[1]")
            block_button_1.click()

            # Presses the second block confirmation button
            block_button_2 = self.driver.find_element(By.XPATH, "(//button[normalize-space()=\"Block\"])[2]")
            block_button_2.click()
            
            self.logger.info(f"User {username} has been blocked!")

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
