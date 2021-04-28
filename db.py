"""
created by Nagaj at 27/04/2021
"""
import json
import os


class JsonFile:

    @classmethod
    def load(cls):
        fname = cls.__name__ + ".json"
        if not os.path.isfile(os.path.join(os.getcwd(), fname)):
            return []
        with open(fname, "r") as f:
            data = json.load(f)
        return data

    def save(self):
        cls = self.__class__
        fname = cls.__name__ + ".json"
        data = cls.load()
        obj = self._to_json()
        if obj not in data:
            data.append(obj)
            with open(fname, "w") as f:
                json.dump(data, f, indent=4)
