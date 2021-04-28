"""
created by Nagaj at 27/04/2021
"""
from developers import Developer, TechnicalLead
from team import Team


def main():
    backend_team = Team("Backend")
    java_team = Team("Java Team")
    james = TechnicalLead("James", "1990-03-05", "Back-end Team Lead")
    nagah = Developer("Nagah", "1995-12-30", "Back-end Developer")
    leon = Developer("Leon", "1995-12-12", "Back-end Developer")
    john = Developer("John", "1995-12-14", "Back-end Developer")
    sara = Developer("Sara", "1995-12-15", "Java Developer")
    smith = Developer("Smith", "1995-12-16", "Java Developer")
    test = TechnicalLead("test", "1995-12-17", "Java Tech Lead")

    #########################

    backend_members = [james, leon, nagah, john]
    for member in backend_members:
        member.join_member_to_team(backend_team)

    #########################

    java_members = [test, sara, smith]
    for member in java_members:
        member.join_member_to_team(java_team)

    for member in backend_team:
        member.show_info()
        print("#" * 50)

    #########################


if __name__ == '__main__':
    main()
