"""
created by Nagaj at 29/04/2021
"""
from utils import now


class Desk:

    def __init__(self, location):
        self.location = location
        self.created = now
        self.developer = None

    def show_desk_info(self):
        print(f"Location: {self.location}")
        print(f"Created at: {self.created}")

    def __repr__(self):
        return f"<Desk><{self.location}>"
