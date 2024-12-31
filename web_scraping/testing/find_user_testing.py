import unittest
from unittest.mock import MagicMock
from instagram.find_user import FindUser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFindUser(unittest.TestCase):

    def test_instagram_find_user(self):
        # Create a mock browser object
        mock_browser = MagicMock()
        mock_driver = MagicMock()
        mock_browser.get_driver.return_value = mock_driver
        
        # Creates the FindUser object
        find_user = FindUser(mock_browser)
        
        # Simulates browser behavior
        mock_driver.get.return_value = None
        mock_driver.find_element.return_value = MagicMock()
        
        # Runs the method
        find_user.instagram_find_user("example_user")
        
        # Assertions to ensure expected behavior
        mock_driver.get.assert_called_once_with("https://www.instagram.com/example_user/")
        mock_browser.get_driver.assert_called_once()
        
        # Checks if the page is expected to load
        WebDriverWait(mock_driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

if __name__ == "__main__":
    unittest.main()
