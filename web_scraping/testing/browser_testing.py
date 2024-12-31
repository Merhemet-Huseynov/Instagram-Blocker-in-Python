import unittest
from unittest.mock import patch, MagicMock
from browser_bot.opening_browser import BrowserBot

class TestBrowserBot(unittest.TestCase):

    @patch("browser_bot.opening_browser.ChromeDriverManager.install")
    @patch("browser_bot.opening_browser.webdriver.Chrome")
    def test_open_chrome(self, mock_chrome, mock_install):
       # Checks the installation process and browser driver
        mock_install.return_value = "fake_path"
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        bot = BrowserBot()
        driver = bot.open_chrome()

       # Checks if the driver is started correctly
        self.assertEqual(driver, mock_driver)
        mock_chrome.assert_called_once()
        mock_install.assert_called_once()
        
    def test_get_driver(self):
        bot = BrowserBot()
        
        # Checks if an exception is raised when the driver is not started
        with self.assertRaises(Exception):
            bot.get_driver()
        
        # Checks if the driver is returned when it is started
        bot.open_chrome()
        driver = bot.get_driver()
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.main()
