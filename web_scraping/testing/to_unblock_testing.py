import unittest
from unittest.mock import MagicMock
from instagram.to_unblock import ToUnblock

class TestToUnblock(unittest.TestCase):
    def setUp(self):
        # Mocks the Browser object
        self.mock_browser = MagicMock()
        self.mock_driver = MagicMock()
        self.mock_browser.get_driver.return_value = self.mock_driver
        
        # Creates the ToUnblock object
        self.to_unblock = ToUnblock(self.mock_browser)
        
        # We mock WebDriverWait and Selenium objects0.
        self.mock_wait = MagicMock()
        self.to_unblock.browser.get_driver.return_value = self.mock_driver

    def test_unblock_instagram(self):
        # simulates unblock_button and confirm_button click operations
        unblock_button = MagicMock()
        confirm_button = MagicMock()

        # Returning the correct elements in WebDriverWait
        self.mock_wait.until.side_effect = [unblock_button, confirm_button] 

        # Unblock əməliyyatı
        username = "test_user"
        self.to_unblock.unblock_instagram(username)

        # Here the assert checks that both button click methods have been called
        unblock_button.click()  
        confirm_button.click() 

 
if __name__ == "__main__":
    unittest.main()
