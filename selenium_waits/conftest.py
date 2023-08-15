import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def test_driver():
    test_driver = webdriver.Chrome()
    yield test_driver
    test_driver.quit()


@pytest.fixture
def driver(test_driver):
    test_driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    return test_driver
