import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

class Example1WebDriverSetupTest(unittest.TestCase):

    def test_driver_manager_chrome(self):
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)
        
        driver.quit()

    def test_driver_manager_firefox(self):
        firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)

        driver.get("https://google.co.th")
        self.assertEqual("Google", driver.title)

        driver.quit()

if __name__ == '__main__':
    unittest.main()

