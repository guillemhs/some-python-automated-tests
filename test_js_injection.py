import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        button_xpath = "/html/body/table[3]/tbody/tr/td[2]/table/tbody/tr/td/div[4]/form/input"
        js = """
            window.alert = function(message) {
            lastAlert = message;
            }
            """
        driver.get('http://www.tizag.com/javascriptT/javascriptalert.php')
        driver.execute_script("%s" % js)
        driver.find_element_by_xpath(button_xpath).click()
        #exception just occured
        driver.execute_script("return lastAlert")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()