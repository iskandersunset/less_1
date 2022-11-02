# from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages


class Response:
    """ Base methods."""

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        """ Validating schema json."""

        if isinstance(self.response_json, list):  # Без pydantic
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

        # if isinstance(self.response_json, list):  # Без pydantic
        #     for item in self.response_json:
        #         validate(item, schema)
        #         print("Schema - VALID!")
        # else:
        #     validate(self.response_json, schema)
        #     print("Schema - VALID!")

    def assert_status_code(self, status_code):
        """Assertion response status code."""

        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
