import unittest
from unittest.mock import MagicMock
from selenium.webdriver.common.by import By
from instagram.instagram_login import InstagramBot

class TestInstagramBot(unittest.TestCase):

    def setUp(self):
        # Installs a fake browser driver
        self.mock_browser = MagicMock()
        self.bot = InstagramBot(self.mock_browser)
        
    def test_open_instagram(self):
        # Testing the open_instagram method
        self.bot.open_instagram()
        self.mock_browser.get_driver().get.assert_called_with("https://www.instagram.com")
    
    def test_login(self):
        # Tests the input method
        username = "testuser"
        password = "testpassword"
        
        # Mocks the find_element and send_keys methods
        mock_find_element = MagicMock()
        self.mock_browser.get_driver().find_element = mock_find_element
        
        # Mock the send_keys method for username and password input
        mock_send_keys = MagicMock()
        mock_find_element.return_value.send_keys = mock_send_keys
        
        # Calls the login method
        self.bot.login(username, password)
        
        # Checks whether the username and password input was found and whether the keys were sent
        self.mock_browser.get_driver().find_element.assert_any_call(By.NAME, "username")
        self.mock_browser.get_driver().find_element.assert_any_call(By.NAME, "password")
        mock_send_keys.assert_any_call(username)
        mock_send_keys.assert_any_call(password)

if __name__ == "__main__":
    unittest.main()
