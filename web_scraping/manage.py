from browser_bot.opening_browser import BrowserBot
from instagram.instagram_login import InstagramBot
from instagram.find_user import FindUser


# Gather information
user_username = input("Enter your Instagram username: ")
user_password = input("Enter your Instagram password: ")
username_to_find = input("Enter the username to find: ")

# Create objects
browser = BrowserBot()
instagram = InstagramBot(browser)
find_user = FindUser(browser)


if __name__ == "__main__":
    browser.open_chrome()
    instagram.open_instagram()
    instagram.login(user_username, user_password)
    find_user.instagram_find_user(username_to_find)
    
    input("Press Enter to exit...")
