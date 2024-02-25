import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
        self.assertEqual("Google", self.driver.title)

if __name__ == '__main__':
    unittest.main()
