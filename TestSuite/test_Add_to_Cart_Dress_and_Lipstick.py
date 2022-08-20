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

    def test_001_add_1st_element(self):
        self.driver.get("https://www.amazon.com/ref=nav_logo?language=en_US&currency=USD")

        self.search_field = self.driver.find_element(by=By.ID, value='twotabsearchtextbox')
        self.search_field.send_keys('dress')
        self.search_field.send_keys(Keys.ENTER)

        self.driver.find_element(By.LINK_TEXT, value="Romwe Women's Short Sleeve V Neck All Over Print High Waist A Line Summer Short Dress").click()
        self.driver.find_element(By.XPATH, value='//*[@id="dropdown_selected_size_name"]/span/span').click()
        self.driver.find_element(By.XPATH, value='//*[@id="native_dropdown_selected_size_name_2"]').click() #SELECT SIZE
        time.sleep(2)

        whole_price=self.driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]').text
        price_fraction=self.driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[3]').text
        total_price_dress=int(whole_price)+int(price_fraction)/100
        prices.append(total_price_dress)
        add_to_cart= self.driver.find_element(By.XPATH, value='//*[@id="add-to-cart-button"]')
        add_to_cart.click()
        time.sleep(2)

    def test_002_add_2nd_element(self):

        self.search_field = self.driver.find_element(by=By.ID, value='twotabsearchtextbox')
        self.search_field.send_keys('women lipstick')
        self.search_field.send_keys(Keys.ENTER)

        lipstick = self.driver.find_element(By.LINK_TEXT,value='Clinique Pop Lip Colour + Primer Lipstick, 0.08 oz. Travel Size •• (Bare Pop 02)')
        lipstick.click()

        whole_price = self.driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]').text
        price_fraction = self.driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[3]').text
        total_price_lipstick = int(whole_price) + int(price_fraction) / 100
        prices.append(total_price_lipstick)

        add_to_cart = self.driver.find_element(By.XPATH, value='//*[@id="add-to-cart-button"]')
        add_to_cart.click()
        time.sleep(1)

    def test_003_checkout(self):
        self.driver.find_element(By.ID,value="sw-gtc").click()
        final_price=self.driver.find_element(By.XPATH, value='//*[@id="sc-subtotal-amount-activecart"]/span').text
        final_price=float(final_price[1::])
        self.assertEquals(prices[0]+prices[1],final_price)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
