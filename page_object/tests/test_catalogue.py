def test_add_to_cart(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    product_name = "sauce-labs-backpack"
    catalog_page.add_to_cart(product_name)
    assert catalog_page.is_cart_badge_displayed, f"Cart badge not displayed after adding '{product_name}' to the cart"


def test_click_on_product_image(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    item_number = 4
    catalog_page.click_on_product_image(item_number)
    current_url = catalog_page.get_current_url()
    expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_click_on_product_title(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    item_number = 4
    catalog_page.click_on_product_title(item_number)
    current_url = catalog_page.get_current_url()
    expected_url = "https://www.saucedemo.com/inventory-item.html?id=4"
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_click_on_shopping_cart(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    catalog_page.go_to_cart()
    current_url = catalog_page.get_current_url()
    expected_url = "https://www.saucedemo.com/cart.html"
    assert expected_url in current_url, f"Expected URL: {expected_url}, actual URL: {current_url}"


def test_sort_by_price_low_to_high(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    catalog_page.sort_by_price_low_to_high()
    numeric_prices = catalog_page.get_product_prices(as_numeric=True)
    assert numeric_prices == sorted(numeric_prices), "Products are not sorted by price low to high."
    lowest_price = numeric_prices[0]
    highest_price = numeric_prices[-1]
    assert lowest_price == 7.99, f"Expected lowest price: $7.99, actual: ${lowest_price}"
    assert highest_price == 49.99, f"Expected highest price: $49.99, actual: ${highest_price}"


def test_sort_by_price_high_to_low(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    catalog_page.sort_by_price_high_to_low()
    numeric_prices = catalog_page.get_product_prices(as_numeric=True)
    assert numeric_prices == sorted(numeric_prices, reverse=True), "Products are not sorted by price high to low."
    highest_price = numeric_prices[0]
    lowest_price = numeric_prices[-1]
    assert highest_price == 49.99, f"Expected highest price: $49.99, actual: ${highest_price}"
    assert lowest_price == 7.99, f"Expected lowest price: $7.99, actual: ${lowest_price}"


def test_sort_by_name_a_to_z(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    catalog_page.sort_by_name_a_to_z()
    product_names = catalog_page.get_product_names()
    assert product_names == sorted(product_names), "Products are not sorted by name in a to z order."


def test_sort_by_name_z_to_a(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    catalog_page.sort_by_name_z_to_a()
    product_names = catalog_page.get_product_names()
    assert product_names == sorted(product_names, reverse=True), "Products are not sorted by name in z to a order."


def test_twitter_icon_link(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    expected_url = "https://twitter.com/saucelabs"
    catalog_page.click_icon_link_and_wait_for_url(catalog_page.TWITTER_ICON_LINK, expected_url)
    assert expected_url in catalog_page.driver.current_url, (f"Expected URL: {expected_url}, "
                                                             f"actual URL: {catalog_page.driver.current_url}")


def test_facebook_icon_link(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    expected_url = "https://www.facebook.com/saucelabs"
    catalog_page.click_icon_link_and_wait_for_url(catalog_page.FACEBOOK_ICON_LINK, expected_url)
    assert expected_url == catalog_page.driver.current_url, (f"Expected URL: {expected_url}, "
                                                             f"actual URL: {catalog_page.driver.current_url}")


def test_linkedin_icon_link(logged_in_catalog_page):
    catalog_page = logged_in_catalog_page
    expected_url = "https://www.linkedin.com/company/sauce-labs/"
    catalog_page.click_icon_link_and_wait_for_url(catalog_page.LINKEDIN_ICON_LINK, expected_url)
    assert expected_url == catalog_page.driver.current_url, (f"Expected URL: {expected_url}, "
                                                             f"actual URL: {catalog_page.driver.current_url}")
