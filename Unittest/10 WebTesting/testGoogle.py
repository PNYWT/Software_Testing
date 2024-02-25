import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

class Example1WebDriverSetupTest(unittest.TestCase):

    def setUp(self) -> None:
        edge_service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=edge_service)

        return super().setUp()
    
    def tearDown(self) -> None:
        import time
        time.sleep(3)
        self.driver.quit()
        return super().tearDown()

    def test_driver_manager_edge(self):
        self.driver.get("https://google.co.th")
        self.driver.implicitly_wait(0.5)
        search_box = self.driver.find_element(by=By.NAME, value="q")
        search_button = self.driver.find_element(by=By.NAME, value="btnK")
        search_box.send_keys("Selenium")
        search_box.click()
        search_box = self.driver.find_element(by=By.NAME, value="q")
        self.assertEqual("Selenium", search_box.get_attribute("value"))

if __name__ == '__main__':
    unittest.main()
