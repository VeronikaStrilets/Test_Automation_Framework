import pytest
from selenium.webdriver import Chrome

from page_object.pages.sign_in_page import SignInPage
from page_object.pages.catalogue_page import CataloguePage
from page_object.pages.cart_page import CartPage
from page_object.pages.checkout_step_one_page import CheckoutStepOnePage
from page_object.pages.checkout_step_two_page import CheckoutStepTwoPage
from page_object.utils.utils import get_rand_value, get_rand_num, get_rand_postcode


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def username():
    return "standard_user"


@pytest.fixture(scope="session")
def password():
    return "secret_sauce"


@pytest.fixture
def logged_in_catalog_page(driver, username, password):
    sign_in_page = SignInPage(driver)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password(password)
    sign_in_page.click_login()
    catalog_page = CataloguePage(driver)
    return catalog_page


@pytest.fixture
def cart_with_added_products(logged_in_catalog_page, driver):
    product_names = ["sauce-labs-backpack", "sauce-labs-bike-light"]
    for product_name in product_names:
        logged_in_catalog_page.add_to_cart(product_name)
    logged_in_catalog_page.go_to_cart()
    cart_page = CartPage(driver)
    yield cart_page


@pytest.fixture
def checkout_step_one_page(driver):
    return CheckoutStepOnePage(driver)


@pytest.fixture
def checkout_step_two_page(driver):
    return CheckoutStepTwoPage(driver)


@pytest.fixture
def setup_checkout_process(cart_with_added_products, checkout_step_one_page):
    cart_with_added_products.click_checkout()
    checkout_step_one_page.fill_personal_info()

@pytest.fixture
def checkout_process(cart_with_added_products, checkout_step_one_page):
    cart_with_added_products.click_checkout()
    checkout_step_one_page.fill_personal_info()
    checkout_step_one_page.click_continue()


@pytest.fixture
def uniq_first_name():
    return get_rand_value()


@pytest.fixture
def uniq_last_name():
    return get_rand_num()


@pytest.fixture
def uniq_postcode():
    return get_rand_postcode()
