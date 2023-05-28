import json


class Checking:

    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print('Correct status code:', status_code)

    @staticmethod
    def check_required_fields(result, required_fields):
        result_fields = json.loads(result.text)
        assert required_fields == list(result_fields)
        print('All required fields are present:', required_fields)

    @staticmethod
    def check_field_value(result, field, value):
        result_info = result.json()
        check_field_value = result_info.get(field)
        assert check_field_value == value
        print('Field: "' + field + '"' + ', has correct value: "' + check_field_value + '"')
