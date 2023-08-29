from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class SignInPage(BasePage):
    FORM_USERNAME = (By.ID, "user-name")
    FORM_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def enter_username(self, username):
        username_field = self.find(self.FORM_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find(self.FORM_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.find(self.LOGIN_BTN).click()
