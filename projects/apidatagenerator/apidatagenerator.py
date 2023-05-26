import json
import re
import random


def generate_api_test_cases(json_structure):
    test_cases = {}
    field_type = None
    min_len = None
    max_len = None
    regex = None
    for field_name, validation_rules in json_structure.items():
        if type(validation_rules) == str:
            field_type, min_len, max_len, regex = validation_rules.split(",")
            min_len = int(min_len) if min_len else None
            max_len = int(max_len) if max_len else None
        test_cases.update(
            generate_test_data(field_name, field_type, min_len, max_len, regex)
        )
    return test_cases


def generate_test_data(field_name, field_type, min_len=None, max_len=None, regex=None):
    test_cases = {}

    # type testing
    if field_type == "string":
        test_cases[field_name + "_invalid_type"] = 12345
        test_cases[field_name + "_valid_string"] = "valid string"
        if regex:
            test_cases[field_name + "_invalid_regex"] = "invalid string"
    elif field_type == "integer":
        test_cases[field_name + "_invalid_type"] = "invalid string"
        test_cases[field_name + "_valid_integer"] = 12345
    elif field_type == "float":
        test_cases[field_name + "_invalid_type"] = "invalid string"
        test_cases[field_name + "_valid_float"] = 123.45

    # boundary value analysis
    if min_len and max_len:
        test_cases[field_name + "_below_min"] = "a" * (min_len - 1)
        test_cases[field_name + "_above_max"] = "a" * (max_len + 1)

    # regex testing
    if regex:
        test_cases[field_name + "_valid_regex"] = re.sub(
            regex, "valid string", "invalid string"
        )

    # naughty data
    test_cases[field_name + "_null"] = None
    test_cases[field_name + "_empty"] = ""
    test_cases[field_name + "_sql_injection"] = "'; DROP TABLE users;"
    test_cases[field_name + "_excessive_length"] = "a" * 10000
    test_cases[
        field_name + "_invalid_special_characters"
    ] = '<script>alert("XSS");</script>'
    test_cases[field_name + "_escape_characters"] = "\n\t\r"
    return test_cases


def test_cases(test_cases, output_file):
    with open(output_file, "w") as f:
        f.write(json.dumps(test_cases, indent=4))


# Test the above function with the sample input
field_rules = {}


def test_cases(test_cases, output_file):
    with open(output_file, "w") as f:
        f.write(json.dumps(test_cases, indent=4))


output_file = "projects/apidatagenerator/api_test_cases.json"
tests = generate_api_test_cases(field_rules)
test_cases(tests, output_file)
