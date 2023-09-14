import pytest

from api_testing_allure_reporting.rest.lambdatest import LambdatestService


@pytest.fixture(scope="session")
def lambdatest_service():
    return LambdatestService()
