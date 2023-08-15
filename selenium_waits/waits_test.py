import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.explicitlywait
def test_alert(driver):
    driver.find_element(By.ID, "alert").click()
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    expected_text = "I got opened after 5 secods"
    assert expected_text == alert.text, f"Expected text '{expected_text}' but got '{alert.text}'"
    alert.accept()


@pytest.mark.explicitlywait
def test_populate_text(driver):
    driver.find_element(By.ID, "populate-text").click()
    wait = WebDriverWait(driver, 15)
    text_present = wait.until(EC.text_to_be_present_in_element((By.ID, "h2"), "Selenium Webdriver"))
    assert text_present, f"Expected text 'Selenium Webdriver' is not present in the element"


@pytest.mark.explicitlywait
def test_hidden_button(driver):
    driver.find_element(By.ID, "display-other-button").click()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.ID, "hidden")))
    hidden_button = driver.find_element(By.ID, "disable")
    assert hidden_button.is_displayed(), "Button is expected to bu displayed"


@pytest.mark.explicitlywait
def test_enable_button(driver):
    driver.find_element(By.ID, "enable-button").click()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "disable")))
    disable_button = driver.find_element(By.ID, "disable")
    assert disable_button.is_enabled(), "Button is not enabled"


@pytest.mark.explicitlywait
def test_checkbox(driver):
    driver.find_element(By.ID, "checkbox").click()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_located_to_be_selected((By.ID, "ch")))
    checkbox = driver.find_element(By.ID, "ch")
    assert checkbox.is_selected(), "Checkbox should be checked after clicking"
