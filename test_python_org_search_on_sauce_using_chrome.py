import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.sauce = SauceRest(
        username="guillemhs",
        password="cb7e8aba-a39f-4456-92d4-abe76dc87021",
        )
        caps = webdriver.DesiredCapabilities.CHROME
        caps['platform'] = "Windows 7"
        caps['version'] = ""
        self.driver = driver = webdriver.Remote(command_executor='http://guillemhs:cb7e8aba-a39f-4456-92d4-abe76dc87021@ondemand.saucelabs.com:80/wd/hub',desired_capabilities=caps)
        self.jobId = self.driver.getSession()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Google", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()