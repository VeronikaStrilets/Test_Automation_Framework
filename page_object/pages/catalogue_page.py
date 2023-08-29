from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.pages.base_page import BasePage


class CataloguePage(BasePage):
    ADD_TO_CART_TEMPLATE = (By.XPATH, "//*[@id='add-to-cart-{}']")
    PRODUCT_IMAGE = (By.XPATH, "//*[@id='item_{}_img_link']/img")
    PRODUCT_TITLE = (By.XPATH, "//*[@id='item_{}_title_link']/div")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORTING_CONTAINER = (By.XPATH, "//*[@id='header_container']/div[2]/div/span")
    SORT_NAME_OPTION_A_TO_Z = (By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[1]")
    SORT_NAME_OPTION_Z_TO_A = (By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[2]")
    SORT_PRICE_OPTION_LOW_TO_HIGH = (By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[3]")
    SORT_PRICE_OPTION_HIGH_TO_LOW = (By.XPATH, "//*[@id='header_container']/div[2]/div/span/select/option[4]")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    TWITTER_ICON_LINK = (By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[1]/a")
    FACEBOOK_ICON_LINK = (By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[2]/a")
    LINKEDIN_ICON_LINK = (By.XPATH, "//*[@id='page_wrapper']/footer/ul/li[3]/a")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    URL = "https://www.saucedemo.com/inventory.html"
    ITEM1 = (By.ID, "add-to-cart-sauce-labs-backpack")
    ITEM2 = (By.ID, "add-to-cart-sauce-labs-bike-light")

    def add_to_cart(self, product_name):
        add_to_cart_locator = (By.XPATH, self.ADD_TO_CART_TEMPLATE[1].format(product_name))
        add_to_cart_button = self.driver.find_element(*add_to_cart_locator)
        add_to_cart_button.click()

    def is_cart_badge_displayed(self):
        cart_indicator = self.find(self.SHOPPING_CART_BADGE)
        return cart_indicator.is_displayed()

    def click_on_product_image(self, item_number):
        product_image_locator = (By.XPATH, self.PRODUCT_IMAGE[1].format(item_number))
        self.find(product_image_locator).click()

    def click_on_product_title(self, item_number):
        product_image_locator = (By.XPATH, self.PRODUCT_TITLE[1].format(item_number))
        self.find(product_image_locator).click()

    def get_product_prices(self, as_numeric=False):
        price_elements = self.find_all(self.PRODUCT_PRICE)
        if as_numeric:
            return [float(price.text.strip('$')) for price in price_elements]
        else:
            return [price.text for price in price_elements]

    def sort_by_price_low_to_high(self):
        sorting_container = self.find(self.SORTING_CONTAINER)
        sorting_container.click()
        price_option = self.find(self.SORT_PRICE_OPTION_LOW_TO_HIGH)
        price_option.click()

    def sort_by_price_high_to_low(self):
        sorting_container = self.find(self.SORTING_CONTAINER)
        sorting_container.click()
        price_option = self.find(self.SORT_PRICE_OPTION_HIGH_TO_LOW)
        price_option.click()

    def get_product_names(self):
        product_name_elements = self.find_all(self.PRODUCT_TITLE)
        return [name.text for name in product_name_elements]

    def sort_by_name_a_to_z(self):
        sorting_container = self.find(self.SORTING_CONTAINER)
        sorting_container.click()
        name_option = self.find(self.SORT_NAME_OPTION_A_TO_Z)
        name_option.click()

    def sort_by_name_z_to_a(self):
        sorting_container = self.find(self.SORTING_CONTAINER)
        sorting_container.click()
        name_option = self.find(self.SORT_NAME_OPTION_Z_TO_A)
        name_option.click()

    def click_icon_link_and_wait_for_url(self, icon_link_locator, expected_url, timeout=20):
        self.click(icon_link_locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def go_to_cart(self):
        shopping_cart_icon = self.driver.find_element(*self.SHOPPING_CART)
        shopping_cart_icon.click()

    def add_two_items(self):
        self.driver.find_element(*self.ITEM1).click()
        self.driver.find_element(*self.ITEM2).click()
