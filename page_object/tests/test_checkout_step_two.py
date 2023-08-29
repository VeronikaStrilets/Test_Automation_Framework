def test_the_total_price(checkout_process, checkout_step_two_page):
    item_prices = checkout_step_two_page.get_total_prices()
    expected_total_price = sum(item_prices)
    actual_total_price = checkout_step_two_page.get_total_prices()
    assert sum(actual_total_price) == expected_total_price, (f"Expected total price: {expected_total_price}, "
                                                             f"actual: {sum(actual_total_price)}")


def test_cancel_button_redirect(checkout_process, checkout_step_two_page):
    checkout_step_two_page.click_cancel()
    expected_url = "https://www.saucedemo.com/inventory.html"
    current_url = checkout_step_two_page.get_current_url()
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_thank_you_message(checkout_process, checkout_step_two_page):
    checkout_step_two_page.click_finish()
    assert checkout_step_two_page.is_thank_you_message_present()


def test_finish_button_redirect(checkout_process, checkout_step_two_page):
    checkout_step_two_page.click_finish()
    expected_url = "https://www.saucedemo.com/checkout-complete.html"
    current_url = checkout_step_two_page.get_current_url()
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"
