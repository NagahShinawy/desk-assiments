"""
created by Nagaj at 27/04/2021
"""


class Team:

    def __init__(self, team_name, tl=None):
        self.team_name = team_name
        self.tl = tl
        self.members = []

    def __repr__(self):
        return f"<{self.team_name}>"

    def __getitem__(self, item):
        return self.members[item]

    def __contains__(self, item):
        return item in self.members
