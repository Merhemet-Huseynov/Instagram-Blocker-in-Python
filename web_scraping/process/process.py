from instagram.blocking_process import InstagramBlocking
from browser_bot.opening_browser import BrowserBot
from instagram.instagram_login import InstagramBot
from instagram.to_unblock import ToUnblock
from instagram.find_user import FindUser

def gather_information() -> tuple:
    """Collects data for the execution of the operation."""
    user_username = input("Enter your Instagram username: ").strip()
    user_password = input("Enter your Instagram password: ").strip()
    username_to_find = input("Enter the username to find: ").strip()
    option = input("Enter for block or unblock operation (example: block): ").lower().strip()
    return user_username, user_password, username_to_find, option

def create_objects() -> tuple:
    """Initializes and returns instances of required 
       classes for browser and Instagram operations."""
    browser = BrowserBot()
    instagram = InstagramBot(browser)
    find_user = FindUser(browser)
    blocking = InstagramBlocking(browser)
    to_unblock = ToUnblock(browser)
    return browser, instagram, find_user, blocking, to_unblock

def handle_instagram_user() -> None:
    """Executes the block or unblock operation on the target 
        Instagram user based on the provided option."""

    # The collect_data() and the create_objects() function is called.
    user_username, user_password, username_to_find, option = gather_information()
    browser, instagram, find_user, blocking, to_unblock = create_objects()
    
    browser.open_chrome()
    instagram.open_instagram()
    instagram.login(user_username, user_password)
    find_user.instagram_find_user(username_to_find)

    if option == "unblock":
        to_unblock.unblock_instagram(username_to_find)
    else:
        blocking.block_user(username_to_find)
