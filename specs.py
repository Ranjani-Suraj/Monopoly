from Major import Major
from Minor import Minor
from tkinter import *
class Specs :

    def __init__(self, major_name = "", minor_name = "", years = 0, list_of_interests = [], max_credits = 0, list_of_completed = [], current_year = 1, summer = False):
        self.major = Major(major_name)
        self.minor = Minor(minor_name)
        self.years = years
        self.list_of_interests = list_of_interests
        self.summer = summer
        self.current_year = current_year
        self.max_credits = max_credits
        self.list_of_completed = list_of_completed


