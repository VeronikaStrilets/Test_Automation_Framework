def test_item_displayed_in_cart(cart_with_added_products):
    item_quantity = cart_with_added_products.get_item_quantity()
    assert item_quantity == 2, f"Expected item quantity: 1, actual quantity: {item_quantity}"


def test_remove_item_from_cart(cart_with_added_products):
    product_name = "sauce-labs-backpack"
    cart_with_added_products.remove_from_cart(product_name)
    remaining_items = cart_with_added_products.get_item_quantity()
    assert remaining_items == 1, f"Expected remaining items: 1, actual remaining items: {remaining_items}"


def test_remove_items_from_cart(cart_with_added_products):
    product_names = ["sauce-labs-backpack", "sauce-labs-bike-light"]
    for product_name in product_names:
        cart_with_added_products.remove_from_cart(product_name)
    assert cart_with_added_products.is_cart_empty(), "Cart is not empty."


def test_continue_shopping(cart_with_added_products):
    cart_with_added_products.click_continue_shopping()
    expected_url = "https://www.saucedemo.com/inventory.html"
    current_url = cart_with_added_products.get_current_url()
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_click_checkout(cart_with_added_products, logged_in_catalog_page):
    cart_with_added_products.click_checkout()
    expected_url = "https://www.saucedemo.com/checkout-step-one.html"
    current_url = logged_in_catalog_page.get_current_url()
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"
