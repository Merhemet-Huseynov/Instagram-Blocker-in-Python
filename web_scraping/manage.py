from browser_bot.opening_browser import BrowserBot
from browser_bot.Instagram_link import InstagramBot

user_username = input("Enter your Instagram username: ")
user_password = input("Enter your Instagram password: ")

# Object is being created
browser = BrowserBot()
instagram = InstagramBot(browser)

if __name__ == "__main__":
    browser.open_chrome() 
    instagram.open_instagram()
    instagram.login(user_username, user_password)
    input()