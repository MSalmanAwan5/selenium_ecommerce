from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class AddToCartTest(unittest.TestCase):
    # driver = webdriver.Chrome()
    # def setUp(self):
    #     self.driver =  webdriver.Chrome(executable_path=r"C:\Users\Muhammad Salman\Downloads\Compressed\chromedriver.exe")
    # def tearDown(self):
    #     self.driver.quit()

    def add_product_to_cart(self):
        # self.setUp()
        driver = webdriver.Chrome(executable_path=r"C:\Users\Muhammad Salman\Downloads\Compressed\chromedriver.exe")
        driver.get("http://localhost:8000/products")

        assert "eCommerce" in driver.title

        gotoProduct = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/h4/a')
        gotoProduct.click()

        quantity = driver.find_element_by_xpath('//*[@id="add-form"]/input[2]')
        quantity.clear()
        quantity.send_keys("2")
        addButton = driver.find_element_by_id("submit-btn")
        addButton.click()
        assert "Successfully added to the cart" not in driver.page_source
        driver.quit()
        # self.tearDown()

add = AddToCartTest()
add.add_product_to_cart()