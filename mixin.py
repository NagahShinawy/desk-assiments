"""
created by Nagaj at 27/04/2021
"""
from db import JsonFile


class JsonHandler(JsonFile):
    DATEFORMAT = "%Y-%m-%d"

    def _to_json(self):
        return self

    def _date_tostring(self, dateobj):
        return dateobj.strftime(self.DATEFORMAT)
