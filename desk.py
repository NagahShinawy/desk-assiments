"""
created by Nagaj at 29/04/2021
"""
from utils import now
from mixin import JsonHandler


class Desk(JsonHandler):
    def __init__(self, location):
        self.location = location
        self.created = now
        self.developer = None

    def show_desk_info(self):
        print(f"Location: {self.location}")
        print(f"Created at: {self.created}")

    def activate_desk(self, developer):
        self.developer = developer
        super().save()

    def _to_json(self):
        return {
            "location": self.location,
            "created": self._date_tostring(self.created),
            "developer": self.developer.name,
        }

    def __repr__(self):
        return f"<Desk><{self.location}>"
