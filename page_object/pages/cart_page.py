from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class CartPage(BasePage):
    REMOVE_FROM_CART_TEMPLATE = (By.XPATH, "//*[@id='remove-{}']")
    ITEM_QUANTITY = (By.XPATH, "//*[@class='cart_quantity']")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_item_quantity(self):
        cart_quantity_elements = self.find_all(self.ITEM_QUANTITY)
        total_quantity = 0
        for quantity_element in cart_quantity_elements:
            total_quantity += int(quantity_element.text.strip())
        return total_quantity

    def remove_from_cart(self, product_name):
        remove_button_locator = (By.XPATH, self.REMOVE_FROM_CART_TEMPLATE[1].format(product_name))
        remove_button = self.driver.find_element(*remove_button_locator)
        remove_button.click()

    def is_cart_empty(self):
        try:
            cart_quantity_element = self.find(self.ITEM_QUANTITY)
            cart_quantity = int(cart_quantity_element.text.strip())
            return cart_quantity == 0
        except NoSuchElementException:
            return True

    def click_continue_shopping(self):
        continue_shopping_button = self.find(self.CONTINUE_SHOPPING_BUTTON)
        continue_shopping_button.click()

    def click_checkout(self):
        checkout_button = self.find(self.CHECKOUT_BUTTON)
        checkout_button.click()
