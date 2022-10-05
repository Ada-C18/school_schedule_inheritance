from .student import Student

# add HighSchoolStudent here
class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes,
        has_parking_privileges=False, clubs=None):
        
        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs if clubs is not None else []

    def join_club(self, club_name):
        self.clubs.append(club_name)

    def summary(self):
        student_summary = super().summary()
        parking_status = "has" if self.has_parking_privileges else "doesn't have"
        
        if not self.clubs:
            club_memberships = "hasn't joined a club yet." 
        else:
            club_memberships = f"is a member of: {', '.join(self.clubs)}"

        return (f"{student_summary}\n{self.name} {parking_status} parking privileges\n"
            f"{self.name} {club_memberships}")