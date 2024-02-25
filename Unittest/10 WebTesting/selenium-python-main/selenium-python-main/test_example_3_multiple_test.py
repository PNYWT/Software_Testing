import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Example3MultipleGoogleTest(unittest.TestCase):

    def setUp(self):
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://google.co.th")
        self.driver.implicitly_wait(0.5)   

    def test_google_title(self):
        self.assertEqual("Google", self.driver.title)        

    def test_search_google(self):
        search_box = self.driver.find_element(by=By.NAME, value="q")
        search_button = self.driver.find_element(by=By.NAME, value="btnK")

        search_box.send_keys("Selenium")
        search_button.click()

        search_box = self.driver.find_element(by=By.NAME, value="q")
        self.assertEqual("Selenium", search_box.get_attribute("value"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
