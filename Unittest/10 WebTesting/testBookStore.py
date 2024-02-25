import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

class Example1WebDriverSetupTest(unittest.TestCase):

    def setUp(self) -> None:
        edge_service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=edge_service)
        self.driver.implicitly_wait(0.5) 

        return super().setUp()

    def test_welcome(self):
        self.driver.get("http://localhost:8090/")
        heading = self.driver.find_element(by=By.TAG_NAME, value="h1")
        self.assertEqual("Welcome to Wisdom Book Website", heading.text)

    def test_add_book(self):
        self.driver.get("http://localhost:8090/book/add");
        name_field = self.driver.find_element(by=By.ID, value="nameInput")
        author_field = self.driver.find_element(by=By.ID, value="authorInput")
        price_field = self.driver.find_element(by=By.ID, value="priceInput")
        name_field.send_keys("Clean Code")
        author_field.send_keys("Robert Martin")
        price_field.send_keys("600")
        submit_button = self.driver.find_element(by=By.CLASS_NAME, value="btn")
        submit_button.click()
 
        name = self.driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[1]")
        author = self.driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[2]")
        price = self.driver.find_element(by=By.XPATH, value="//table/tbody/tr[1]/td[3]")
        self.assertEqual("Clean Code", name.text)
        self.assertEqual("Robert Martin", author.text)
        self.assertEqual("600.00", price.text)

    def tearDown(self) -> None:
        import time
        time.sleep(3)
        self.driver.quit()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
