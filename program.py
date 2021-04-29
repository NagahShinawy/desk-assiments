"""
created by Nagaj at 27/04/2021
"""
from developers import Developer, TechnicalLead
from team import Team
from desk import Desk


def main():
    # teams & members

    backend_team = Team("Backend")
    java_team = Team("Java Team")
    james = TechnicalLead("James", "1990-03-05", "Back-end Team Lead")
    nagah = Developer("Nagah", "1995-12-30", "Back-end Developer")
    leon = Developer("Leon", "1995-12-12", "Back-end Developer")
    john = Developer("John", "1995-12-14", "Back-end Developer")
    sara = Developer("Sara", "1995-12-15", "Java Developer")
    smith = Developer("Smith", "1995-12-16", "Java Developer")
    test = TechnicalLead("test", "1995-12-17", "Java Tech Lead")

    # ########### Desks  #############

    c101 = Desk("C101")
    c202 = Desk("C202")
    c303 = Desk("C303")
    c404 = Desk("C404")
    c505 = Desk("C505")
    c606 = Desk("C606")
    c707 = Desk("C707")

    # #######  join members to team #####################

    backend_members = [(james, c101), (leon, c202), (nagah, c303), (john, c404)]
    for member, desk in backend_members:
        member.join_member_to_team(backend_team, desk)

    #########################

    java_members = [(test, c505), (smith, c606), (sara, c707)]
    for member, desk in java_members:
        member.join_member_to_team(java_team, desk)

    for member in backend_team:
        member.show_info()
        print("#" * 50)

    #########################
    employees = [sara, nagah, leon, test, james]
    for emp in employees:
        print(emp, emp in backend_team)


if __name__ == '__main__':
    main()
