import json

import allure
import pytest


from api_testing_allure_reporting.utils.file_utils import read_data_file


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.title("JSON to XML conversion")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_xml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_xml = read_data_file(f"xml/{file_name}.xml")
        mini_expected_xml = lambdatest_service.minify_xml(expected_xml)

    with allure.step("Convert JSON to XML via API"):
        actual_xml = lambdatest_service.json_to_xml(input_json)
        mini_actual_xml = lambdatest_service.minify_xml(actual_xml)

    with allure.step("Compare expected and actual XML"):
        assert mini_actual_xml == mini_expected_xml


@pytest.mark.xfail(reason="Bug in the API")
@allure.suite("Lambdatest API tests")
@allure.title("Extract text from JSON")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-text")
@allure.link("https://jira.com/TEST-1234")
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected and actual text.
""")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_extract_text_from_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_text = read_data_file(f"txt/{file_name}.txt")

    with allure.step("Extract text from JSON via API"):
        actual_text = lambdatest_service.extract_text_from_json(input_json)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Lambdatest API tests")
@allure.title("YAML validator testing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@allure.description("""
    This test case verifies the YAML validator service.
    Steps:
    1. Prepare test data.
    2. Send YAML data to the validator.
    3. Validate the response.
""")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_validator(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Send YAML data to the validator"):
        response = lambdatest_service.yaml_validator(input_yaml)

    with allure.step("Validate the response"):
        assert "Valid YAML" == response


@allure.suite("Lambdatest API tests")
@allure.title("JSON to YAML Converter testing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml-converter")
@allure.description("""
    This test case verifies the JSON to YAML converter service.
    Steps:
    1. Prepare test data.
    2. Convert JSON to YAML.
    3. Parse and compare generated yaml data.
""")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")
        expected_json = read_data_file(f"json/{file_name}.json")

    with allure.step("Convert YAML to JSON"):
        actual_json = lambdatest_service.yaml_to_json(input_yaml)

    with allure.step("Parse and compare generated JSON data"):
        expected_json_data = json.loads(expected_json)
        assert expected_json_data == actual_json


@allure.suite("Lambdatest API tests")
@allure.title("XML to YAML Converter testing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml-converter")
@allure.description("""
    This test case verifies the XML to YAML converter service.
    Steps:
    1. Prepare test data.
    2. Convert XML to YAML.
    3. Parse and compare generated yaml data.
""")
@pytest.mark.parametrize("file_name", ["1", "3"])
def test_xml_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        expected_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert XML to YAML"):
        actual_yaml = lambdatest_service.xml_to_yaml(input_xml)

    with allure.step("Compare expected_yaml and actual_yaml"):
        expected_yaml = expected_yaml.strip()
        actual_yaml = actual_yaml.strip()
        assert expected_yaml == actual_yaml


@allure.suite("Lambdatest API tests")
@allure.title("YAML to JSON Converter testing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_to_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yaml")

    with allure.step("Convert YAML to JSON"):
        actual_json = lambdatest_service.yaml_to_json(input_yaml)

    with allure.step("Read and load expected JSON"):
        expected_json_str = read_data_file(f"json/{file_name}.json")
        expected_json = json.loads(expected_json_str)

    with allure.step("Compare expected_json and actual_json"):
        assert expected_json == actual_json
