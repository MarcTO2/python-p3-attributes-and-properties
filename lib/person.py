#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name  # Use the setter for validation
        self.job = job  # Use the setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
    pass
