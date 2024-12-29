from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, browser_bot):
        self.browser_bot = browser_bot

    def open_instagram(self):
        driver = self.browser_bot.get_driver()  
        driver.get("https://www.instagram.com")
        print("Instagram opened!")
        time.sleep(5)
    
    def login(self, username, password):
        driver = self.browser_bot.get_driver()  
        time.sleep(5)

        # Enters username
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(username)
        
        # Enters password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        
        # Presses the Enter key.
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        print("Logged in to Instagram!")