"""
created by Nagaj at 27/04/2021
"""
from db import JsonFile


class JsonHandler(JsonFile):

    def _to_json(self):
        return self
