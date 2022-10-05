from .high_school_student import HighSchoolStudent

class Freshman(HighSchoolStudent):
    def __init__(self, name, classes, has_parking_privileges=False, clubs=None):
        super().__init__(name, grade="Freshman",
            classes=classes,
            has_parking_privileges=has_parking_privileges,
            clubs=clubs)