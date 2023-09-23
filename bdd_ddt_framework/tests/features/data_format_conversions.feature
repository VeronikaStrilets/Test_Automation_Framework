Feature: Data Format Conversion

  Scenario Outline: Convert data from JSON to XML via API
    Given a JSON file <json_file>
    And a XML file <xml_file>
    When convert data from JSON to XML via API
    Then compare expected and actual XML file

    Examples:
      | json_file  | xml_file    |
      | 1.json     | 1.xml       |
      | 2.json     | 3.xml       |

  Scenario Outline: Extract text from JSON via API
    Given a JSON file <json_file>
    And a TXT file <txt_file>
    When extract text from JSON via API
    Then compare the extracted text with the expected text

    Examples:
      | json_file  | txt_file    |
      | 1.json     | 1.txt       |
      | 2.json     | 2.txt       |


  Scenario Outline: Validate YAML input file
    Given a YAML file <yaml_file>
    When validate the YAML using the YAML validator
    Then validate the result

    Examples:
      | yaml_file |
      | 1.yaml    |
      | 2.yaml    |


  Scenario Outline: Convert JSON to YAML
    Given a JSON file <json_file>
    And a YAML file <yaml_file>
    When convert data from JSON to YAML via API
    Then compare expected and actual YAML file

    Examples:
      | json_file  | yaml_file   |
      | 1.json     | 1.yaml      |
      | 2.json     | 2.yaml      |

  Scenario Outline: Convert XML to YAML
    Given a XML input_file <xml_file>
    And a YAML file <yaml_file>
    When convert data from XML to YAML via API
    Then compare expected and actual YAML file

    Examples:
      | xml_file  | yaml_file   |
      | 1.xml     | 1.yaml      |
      | 3.xml     | 3.yaml      |

  Scenario Outline: Convert YAML to JSON
    Given a YAML file <yaml_file>
    And a JSON file <json_file>
    When convert data from YAML to JSON via API
    Then compare expected and actual JSON file

    Examples:
      | yaml_file  | json_file   |
      | 1.yaml     | 1.json      |
      | 2.yaml     | 2.json      |
