import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.softonic.com")
        self.assertIn("Softonic", driver.title)
        searchBox = driver.find_element_by_id("search_input")
        searchButton = driver.find_element_by_xpath(".//*[@id='search_form_top']/fieldset/button")
        searchBox.send_keys("Ares")
        searchButton.click()
        self.assertIn("ares", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()