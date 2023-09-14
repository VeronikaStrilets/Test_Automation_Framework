import pytest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@pytest.mark.smoke
def test_checkboxes(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[6]/a').click()
    checkbox_1 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
    checkbox_1.click()
    checkbox_2 = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')
    checkbox_2.click()
    assert checkbox_1.get_attribute("checked") == "true", "Checkbox 1 is not checked"
    assert not checkbox_2.get_attribute("checked"), "Checkbox 2 is checked, but it shouldn't be"


@pytest.mark.functional
def test_context_menu(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[7]/a').click()
    hot_spot = driver.find_element(By.ID, 'hot-spot')
    actions = ActionChains(driver)
    actions.context_click(hot_spot).perform()
    alert = driver.switch_to.alert
    alert.accept()
    assert not EC.alert_is_present()(driver), "Alert is still present"


@pytest.mark.smoke
def test_dropdown(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a').click()
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")
    assert driver.find_element(By.XPATH, '//*[@id="dropdown"]/option[3]').is_selected(), \
        "Option is not selected"


@pytest.mark.smoke
def test_entry_ad(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[15]/a').click()
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')))
    driver.execute_script("arguments[0].click();", close_button)
    driver.find_element(By.ID, "restart-ad").click()
    assert not driver.find_element(By.ID, "modal").is_displayed(), "Entry Ad modal is still present"
    expected_url = "http://the-internet.herokuapp.com/entry_ad"
    assert driver.current_url == expected_url, f"Expected URL {expected_url}, but got {driver.current_url}"


@pytest.mark.smoke
def test_form_authentication(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
    flash_message = "You logged into a secure area!"
    assert flash_message in driver.find_element(By.ID, "flash").text, f"Expected message '{flash_message}' " \
                                                                      f"is not found on the page"


@pytest.mark.functional
def test_test_frame(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[22]/a').click()
    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/a').click()
    iframe_element = driver.find_element(By.ID, 'mce_0_ifr')
    driver.switch_to.frame(iframe_element)
    iframe_body = driver.find_element(By.CSS_SELECTOR, "body")
    iframe_body.clear()
    entered_text = "To be or not to be?"
    iframe_body.send_keys(entered_text)
    iframe_body_text = iframe_body.text
    assert entered_text == iframe_body_text, f"Text '{entered_text}' is not found in the iframe's body"


@pytest.mark.functional
def test_horizontal_slider(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[24]/a').click()
    slider = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/input')
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider, 50, 0).perform()
    actions.send_keys(Keys.ARROW_LEFT * 3).perform()
    slider_value = driver.find_element(By.ID, "range").text
    assert slider_value == "3", f"Expected slider value '3', but got '{slider_value}'"


@pytest.mark.functional
def test_hovers(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[25]/a').click()
    hover_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/img')
    actions = ActionChains(driver)
    actions.move_to_element(hover_element).perform()
    view_profile_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/a')
    view_profile_link.click()
    body_text = driver.find_element(By.XPATH, '/html/body/h1')
    assert body_text.is_displayed(), "Expected 'Not Found' text is not found on the page"


@pytest.mark.functional
def test_inputs(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[27]/a').click()
    input_field = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')
    input_field.send_keys("2023")
    entered_value = input_field.get_attribute("value")
    assert entered_value == "2023", f"Expected input value: 2023, but got: '{entered_value}'"


@pytest.mark.functional
def test_key_presses(driver):
    driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[31]/a').click()
    input_field = driver.find_element(By.ID, "target")
    input_field.send_keys(Keys.SPACE)
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: SPACE", f"Expected result text not found on the page"
