from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage
from page_object.utils.utils import get_rand_value, get_rand_postcode


class CheckoutStepOnePage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    def fill_personal_info(self):
        uniq_first_name = get_rand_value()
        uniq_last_name = get_rand_value()
        uniq_postcode = get_rand_postcode()

        first_name_field = self.find(self.FIRST_NAME_INPUT)
        last_name_field = self.find(self.LAST_NAME_INPUT)
        postal_code_field = self.find(self.POSTAL_CODE_INPUT)

        first_name_field.clear()
        first_name_field.send_keys(uniq_first_name)
        last_name_field.clear()
        last_name_field.send_keys(uniq_last_name)
        postal_code_field.clear()
        postal_code_field.send_keys(uniq_postcode)

    def click_continue(self):
        continue_button = self.find(self.CONTINUE_BUTTON)
        continue_button.click()

    def click_cancel(self):
        cancel_button = self.find(self.CANCEL_BUTTON)
        cancel_button.click()

    def is_error_message_present(self):
        return self.is_error_element_present(By.CLASS_NAME, "error-button")
