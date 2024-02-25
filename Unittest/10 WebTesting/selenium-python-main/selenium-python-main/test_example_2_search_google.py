import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Example2GoogleSearchTest(unittest.TestCase):

    def test_search_google(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://google.co.th")
        driver.implicitly_wait(0.5)

        search_box = driver.find_element(by=By.NAME, value="q")
        search_button = driver.find_element(by=By.NAME, value="btnK")

        search_box.send_keys("Selenium")
        search_button.click()

        search_box = driver.find_element(by=By.NAME, value="q")
        self.assertEqual("Selenium", search_box.get_attribute("value"))

        driver.quit()

if __name__ == '__main__':
    unittest.main()

