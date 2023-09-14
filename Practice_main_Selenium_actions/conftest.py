import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def test_driver():
    test_driver = webdriver.Chrome()
    yield test_driver
    test_driver.quit()


@pytest.fixture
def driver(test_driver):
    test_driver.get("http://the-internet.herokuapp.com")
    return test_driver
