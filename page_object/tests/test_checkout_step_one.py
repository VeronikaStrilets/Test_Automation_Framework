def test_fill_personal_info_and_continue(cart_with_added_products, checkout_step_one_page):
    cart_with_added_products.click_checkout()
    checkout_step_one_page.fill_personal_info()
    checkout_step_one_page.click_continue()
    current_url = checkout_step_one_page.get_current_url()
    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_cancel(cart_with_added_products, checkout_step_one_page):
    cart_with_added_products.click_checkout()
    checkout_step_one_page.click_cancel()
    expected_url = "https://www.saucedemo.com/cart.html"
    current_url = checkout_step_one_page.get_current_url()
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_empty_personal_info(cart_with_added_products, checkout_step_one_page):
    cart_with_added_products.click_checkout()
    checkout_step_one_page.click_continue()
    assert checkout_step_one_page.is_error_message_present
