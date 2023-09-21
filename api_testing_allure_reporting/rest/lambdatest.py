import allure
import requests


class LambdatestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    @allure.step("Send a POST request to {endpoint}")
    def _send_request(self, endpoint, input_key, input_str):
        url = self.BASE_URL + endpoint
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        return requests.post(url, data={input_key: input_str})

    @allure.step("Send a POST request to convert JSON to XML")
    def json_to_xml(self, input_str: str) -> str:
        response = self._send_request("json-to-xml", "input-str", input_str).text

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to minify XML")
    def minify_xml(self, input_str: str) -> str:
        response = self._send_request("minify-xml", "input-str", input_str).json()["minify_data"]

        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Minified XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to Extract Text from JSON")
    def extract_text_from_json(self, input_str: str) -> str:
        response = self._send_request("extract-text-json", "input-str", input_str).json()["data"]

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Extracted Text", allure.attachment_type.TEXT)

        return response

    @allure.step("Send a POST request to YAML validator")
    def yaml_validator(self, input_str: str) -> str:
        response = self._send_request("yaml-validator", "yaml-str", input_str).json()["message"]

        allure.attach(input_str, "Input Yaml", allure.attachment_type.YAML)
        allure.attach(response, "Output answer", allure.attachment_type.TEXT)

        return response

    @allure.step("Convert JSON to YAML")
    def json_to_yaml(self, input_str: str) -> str:
        response = self._send_request("json-to-yaml", "json-str", input_str).json()["data"]

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response.content, "Output YAML", allure.attachment_type.YAML)

        return response

    @allure.step("Convert XML to YAML")
    def xml_to_yaml(self, input_str: str) -> str:
        response = self._send_request("xml-to-yaml", "xml-str", input_str).json()["data"]

        allure.attach(input_str, "Input xml", allure.attachment_type.XML)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)

        return response

    @allure.step("Convert YAML to JSON")
    def yaml_to_json(self, input_yaml):
        response = self._send_request("yaml-to-json", "yaml-str", input_yaml)

        allure.attach(input_yaml, "Input YAML", allure.attachment_type.YAML)
        allure.attach(response.text, "Output JSON", allure.attachment_type.TEXT)

        return response.json()["data"]
