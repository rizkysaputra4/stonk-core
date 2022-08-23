import json


class BaseResponse:
    def __init__(self, data, error=False, code="00"):
        self.data = data
        self.error = error
        self.code = code

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
