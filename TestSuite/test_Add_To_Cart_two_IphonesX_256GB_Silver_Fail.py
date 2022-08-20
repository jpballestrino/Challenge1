import os
import time
import unittest
from selenium.webdriver.common.by import By
from config import initialize
from selenium.webdriver.common.keys import Keys

os.environ['GH_TOKEN'] = "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"  # In order to use Firefox with .intall() process you need a token to download the driver (github)

class amazon_cart(unittest.TestCase):
    global prices
    prices=[]
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session and maximize window
        inst.driver = initialize.explorer("chrome") # Choose the explorer that you want to use for the test runs: "chrome", "firefox" or "edge"
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_001_buy_2_iphones_silver_256GB(self):
        self.driver.get("https://www.amazon.com/ref=nav_logo?language=en_US&currency=USD")

        self.search_field = self.driver.find_element(by=By.ID, value='twotabsearchtextbox')
        self.search_field.send_keys('Iphone X')
        self.search_field.send_keys(Keys.ENTER)

        self.driver.find_element(By.LINK_TEXT, value="Apple iPhone X, US Version, 64GB, Space Gray - Fully Unlocked (Renewed)").click()
        self.driver.find_element(By.XPATH, value="//li[@title='Click to select 256GB']").click() #SELECT 256 GB
        self.driver.find_element(By.XPATH, value="//li[@title='Click to select Silver']").click() #SELECT silver
        time.sleep(2)

        price_for_1=self.driver.find_element(By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]').text
        prices.append(price_for_1)
        add_to_cart= self.driver.find_element(By.XPATH, value='//*[@id="add-to-cart-button"]')
        add_to_cart.click()

        self.driver.find_element(By.LINK_TEXT, value="Go to Cart").click()

    def test_002_check_price_and_quantity(self):

        quantity=self.driver.find_element(By.XPATH, value='//*[@id="a-autoid-0-announce"]/span[2]').text
        total_price=self.driver.find_element(By.XPATH, value='//*[@id="sc-subtotal-amount-activecart"]/span').text
        self.assertEquals([quantity,float(prices[0][1::])*int(quantity)],["2",float(total_price[1::])])

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
