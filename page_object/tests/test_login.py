from page_object.pages.sign_in_page import SignInPage


def test_log_in(driver, username, password):
    log_in_page = SignInPage(driver)
    log_in_page.enter_username(username)
    log_in_page.enter_password(password)
    log_in_page.click_login()
    catalog_page = driver.current_url
    assert catalog_page in "https://www.saucedemo.com/inventory.html"
