from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    SIGN_IN = (By.ID, "login-button")
    SIGN_OUT = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 5)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def is_error_element_present(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
