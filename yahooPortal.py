"""
This script is to test yahoo portal features
"""
import common
import HTMLTestRunner
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
import unittest

ser = Service('E:/Old_Python_projects/PycharmProjects/seleniumProject/chromedriver.exe')

# ser = Service(ChromeDriverManager().install())
print('Hello')


# class created for unittest calling test cases
class YahooPortal(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(service=ser)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def test_1_find_yahoo(self):
        self.driver.get(common.yahoo["url"])
        try:
            self.driver.find_element(by=By.ID, value= "ybar-logo").click()
        except NoSuchElementException as exception:
            print(exception)
            print("Element not found for username")

    def test_2_clickOn_signIn(self):
        self.driver.get(common.yahoo["url"])
        try:
            self.driver.find_element(By.ID,value= "ybarAccountProfile").click()
        except NoSuchElementException as exception:
            print(exception)
            print("Element not found for username")

    # Teardown class methode
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Done!!")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="Reports",
                                                           title='Test-Report',
                                                           description="Reports for Yahoo program"))
