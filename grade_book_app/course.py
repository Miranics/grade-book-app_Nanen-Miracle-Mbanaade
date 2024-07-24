#!/usr/bin/env python3
class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __repr__(self):
        # String representation of the course
        return f"{self.name} ({self.trimester}, {self.credits} credits)"

    def to_dict(self):
        # Convert course object to a dictionary for JSON serialization
        return {
            "name": self.name,
            "trimester": self.trimester,
            "credits": self.credits
        }

    @staticmethod
    def from_dict(data):
        # Convert a dictionary back to a Course object
        return Course(data["name"], data["trimester"], data["credits"])

