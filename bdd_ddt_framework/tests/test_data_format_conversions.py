import json

from pytest_bdd import given, when, then, parsers, scenarios
from bdd_ddt_framework.utils.file_utils import read_data_file

scenarios("data_format_conversions.feature")


# Given step
@given(parsers.parse('a JSON file {json_file}'), target_fixture="context")
def prepare_JSON_file(json_file, context):
    input_data = read_data_file(f"json/{json_file}")
    context["json"] = input_data
    return context


@given(parsers.parse('a JSON file {json_file}'), target_fixture="json_file")
def prepare_JSON_file(json_file, context):
    input_data = read_data_file(f"json/{json_file}")
    context["json"] = input_data
    return context


@given(parsers.parse('a YAML file {yaml_file}'), target_fixture="context")
def prepare_YAML_file(yaml_file, context):
    input_data = read_data_file(f"yaml/{yaml_file}")
    context["yaml"] = input_data
    return context


@given(parsers.parse('a XML file {xml_file}'), target_fixture="context")
def prepare_XML_file(context, lambdatest_service, xml_file):
    expected_xml = read_data_file(f"xml/{xml_file}")
    mini_expected_xml = lambdatest_service.minify_xml(expected_xml)
    context["mini_expected_xml"] = mini_expected_xml
    return context


@given(parsers.parse('a TXT file {txt_file}'), target_fixture="context")
def prepare_TXT_file(txt_file, context):
    expected_txt = read_data_file(f"txt/{txt_file}")
    context["expected_txt"] = expected_txt
    return context


@given(parsers.parse('a XML input_file {xml_file}'), target_fixture="context")
def prepare_XML_input_file(xml_file, context):
    input_data = read_data_file(f"xml/{xml_file}")
    context["xml"] = input_data
    return context


# When step
@when('convert data from JSON to XML via API', target_fixture="context")
def convert_data_from_json_to_xml(context, lambdatest_service):
    actual_xml = lambdatest_service.json_to_xml(context["json"])
    mini_actual_xml = lambdatest_service.minify_xml(actual_xml)
    context["mini_actual_xml"] = mini_actual_xml
    return context


@when('extract text from JSON via API', target_fixture="context")
def extract_text_from_json(context, lambdatest_service):
    actual_txt = lambdatest_service.extract_text_from_json(context["json"])
    context["actual_txt"] = actual_txt
    return context


@when('validate the YAML using the YAML validator', target_fixture="context")
def validate_yaml(context, lambdatest_service):
    response = lambdatest_service.yaml_validator(context["yaml"])
    context["response"] = response
    return context


@when('convert data from JSON to YAML via API', target_fixture="context")
def convert_data_from_json_to_yaml(context, lambdatest_service):
    context["json"] = json.loads(context["json"])
    context["actual_yaml"] = lambdatest_service.json_to_yaml(context["json"])  # Set actual_yaml here
    return context


@when('convert data from XML to YAML via API', target_fixture="context")
def convert_data_from_xml_to_yaml(context, lambdatest_service):
    actual_yaml = lambdatest_service.xml_to_yaml(context["xml"])
    context["actual_yaml"] = actual_yaml
    return context


@when('convert data from YAML to JSON via API', target_fixture="context")
def convert_data_from_yaml_to_json(context, lambdatest_service):
    actual_json = lambdatest_service.yaml_to_json(context["yaml"])
    context["actual_json"] = json.dumps(actual_json)
    return context


# Then step
@then('compare expected and actual XML file', target_fixture="context")
def compare_expected_and_actual_XML(context):
    assert context["mini_expected_xml"] == context["mini_actual_xml"]


@then('compare the extracted text with the expected text', target_fixture="context")
def compare_expected_and_actual_TXT(context):
    actual_txt = context["actual_txt"].strip().replace(" ", "").replace("\n", "")
    expected_txt = context["expected_txt"].strip().replace(" ", "").replace("\n", "")
    assert actual_txt == expected_txt


@then('validate the result', target_fixture="context")
def validate_yaml_result(context):
    assert context["response"] == "Valid YAML"


@then('compare expected and actual YAML file', target_fixture="context")
def compare_yaml(context):
    expected_yaml = context["yaml"].strip()
    actual_yaml = context["actual_yaml"].strip()
    assert expected_yaml == actual_yaml


@then('compare expected and actual XML file', target_fixture="context")
def compare_expected_and_actual_XML(context):
    assert context["mini_actual_xml"] == context["mini_expected_xml"]


@then('compare expected and actual JSON file', target_fixture="context")
def compare_expected_and_actual_json(context):
    expected_json = json.loads(context["json"])
    actual_json = json.loads(context["actual_json"])
    assert expected_json == actual_json
