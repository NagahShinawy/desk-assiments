"""
created by Nagaj at 27/04/2021
"""
from datetime import date, datetime

from mixin import JsonHandler


class Member:
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

    def _date_tostring(self, dateobj):
        return dateobj.strftime(self.DATEFORMAT)

    def __calculate_age(self):
        today = date.today()
        return (
                today.year
                - self.dob.year
                - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )


class Developer(Member, JsonHandler):

    def __init__(self, name, dob, job):
        super().__init__(name, dob)
        self.job = job
        self.team = None
        self.desk = None

    def join_member_to_team(self, team, desk):
        self.team = team
        self.desk = desk
        team.members.append(self)
        self.save()

    def show_info(self):
        super().show_info()
        print(f"Job: {self.job}")
        print(f"team: {self.team}")

    def _to_json(self):
        join_datetime = self._date_tostring(datetime.now())
        desk = self.desk
        return {
            "name": self.name,
            "dob": self._date_tostring(self.dob),
            "age": self.age,
            "job": self.job,
            "team": self.team.team_name,
            "tl": {"tl_name": self.team.tl.name},
            "join_date": join_datetime,
            "desk": {"location": desk.location, "created": self._date_tostring(desk.created)}
        }


class TechnicalLead(Developer):

    def join_member_to_team(self, team, desk):
        super().join_member_to_team(team, desk)

    def save(self):
        self.team.tl = self
        super().save()
