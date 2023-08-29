import re

from selenium.webdriver.common.by import By
from page_object.pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    ITEM_TOTAL_PRICE = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    THANK_YOU_MESSAGE = (By.XPATH, "//*[@id='checkout_complete_container']/h2[text()='Thank you for your order!']")

    def get_total_prices(self):
        price_elements = self.find_all(self.ITEM_TOTAL_PRICE)
        total_prices = []
        for price_element in price_elements:
            price_text = price_element.text
            price_match = re.search(r'\$(\d+\.\d+)', price_text)
            if price_match:
                price_value = float(price_match.group(1))
                total_prices.append(price_value)
        return total_prices

    def click_cancel(self):
        cancel_button = self.find(self.CANCEL_BUTTON)
        cancel_button.click()

    def click_finish(self):
        finish_button = self.find(self.FINISH_BUTTON)
        finish_button.click()

    def is_thank_you_message_present(self):
        return self.is_element_present(self.THANK_YOU_MESSAGE)
