"""
created by Nagaj at 27/04/2021
"""
from datetime import date, datetime

from mixin import JsonHandler


class Person:
    DATEFORMAT = "%Y-%m-%d"

    def __init__(self, name, dob):
        self.name = name
        self.dob = datetime.strptime(dob, self.DATEFORMAT)
        self.age = self.__calculate_age()

    def __repr__(self):
        return f"<{self.name}>-<{self.dob}>"

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"DOB: {self._date_tostring}")
        print(f"Age: {self.age}")

    @property
    def _date_tostring(self):
        return self.dob.strftime(self.DATEFORMAT)

    def __calculate_age(self):
        today = date.today()
        return (
                today.year
                - self.dob.year
                - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )


class Developer(Person, JsonHandler):

    def __init__(self, name, dob, job):
        super().__init__(name, dob)
        self.job = job
        self.team = None

    def join_member_to_team(self, team):
        self.team = team
        team.members.append(self)
        self.save()

    def show_info(self):
        super().show_info()
        print(f"Job: {self.job}")
        print(f"team: {self.team}")

    def _to_json(self):
        return {
            "name": self.name,
            "dob": self._date_tostring,
            "age": self.age,
            "job": self.job,
            "team": self.team.team_name,
            "tl": {"tl_name": self.team.tl.name}
        }


class TechnicalLead(Developer):

    def join_member_to_team(self, team):
        super().join_member_to_team(team)

    def save(self):
        self.team.tl = self
        super().save()
