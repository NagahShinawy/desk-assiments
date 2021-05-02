"""
created by Nagaj at 27/04/2021
"""
from datetime import date, datetime

from mixin import JsonHandler


class Member(JsonHandler):
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

    def __calculate_age(self):
        today = date.today()
        return (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )


class Developer(Member, JsonHandler):
    is_tl = False

    def __init__(self, name, dob, job):
        super().__init__(name, dob)
        self.job = job
        self.team = None
        self.desk = None
        self.join_datetime = self._date_tostring(datetime.now())

    def join_member_to_team(self, team, dsk):
        self.team = team
        self.desk = dsk
        self.team.members.append(self)
        self.save()

    def show_info(self):
        super().show_info()
        print(f"Job: {self.job}")
        print(f"team: {self.team}")

    def _to_json(self):
        desk = self.desk
        member_data = {
            "name": self.name,
            "dob": self._date_tostring(self.dob),
            "age": self.age,
            "job": self.job,
            "team": self.team.team_name,
            "join_date": self.join_datetime,
            "desk": desk._to_json(),
            "is_tl": self.is_tl,
        }
        if not self.is_tl:
            tl_info = {
                "tl_name": self.team.tl.name,
                "tl_join_date": self.join_datetime,
                "tl_job": self.team.tl.job,
                "tl_desk": self.team.tl.desk._to_json(),
            }

            member_data.update({"tl": tl_info})

        return member_data


class TechnicalLead(Developer):
    is_tl = True

    def join_member_to_team(self, team, dsk):
        super().join_member_to_team(team, dsk)

    def save(self):
        self.team.tl = self
        super().save()
