import os

import allure
import yaml


# def read_data_file(file_path: str) -> str:
#     """Read a file in the data folder and return its content as a string."""
#     data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
#     file_path = os.path.join(data_folder, file_path)
#
#     with open(file_path, "r", encoding="utf-8") as file:
#         file_content = file.read()
#
#     return file_content
#
# import os

def read_data_file(file_path: str) -> str:
    """Read a file in the data folder and return its content as a string."""
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    file_path = os.path.join(data_folder, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return file_content



def read_yaml_file(file_path):
    """Read a YAML file, remove inappropriate signs, and return the data as a string."""
    data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
    file_path = os.path.join(data_folder, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        data = str(yaml.safe_load(f)).replace("'", "").replace("{", "").replace("}", ", ")

    return data


def get_attachment_type_by_file_extension(file_path):
    """Return attachment type by file extension."""
    match file_path.split(".")[-1].lower():
        case "json":
            return allure.attachment_type.JSON
        case "xml":
            return allure.attachment_type.XML
        case "yaml":
            return allure.attachment_type.YAML
        case _:
            return allure.attachment_type.TEXT
