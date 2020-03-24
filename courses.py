#!/usr/bin/env python3

__author__="Tyler Westland"

import argparse
import os

# Course class
class Course:
    def __init__(self, department, number, name, credits,  grade, term, year):
        self.credits = credits
        self.department = department
        self.grade = grade
        self.name = name
        self.number = number
        self.term = term
        self.year = year


    def __add__(self, other):
        return self.credits + other

    def __radd__(self, other):
        return self.credits + other


    def __str__(self):
        return "{self.department}{self.number} -- {self.name} -- "\
                "{self.credits} -- {self.grade} -- {self.term}-{self.year}"\
                .format(self=self)



class CompletedCourses:
    def __init__(self, completed):
        self.completed = completed

    def credit_hours(self, _filter=None):
        """Return the number of credits completed, within the filter

        Arguments:
        _filter: Filter to apply to the courses when counting. 
            The default 'None' means no filter.
        """
        if _filter is None:
            applicable = self.completed
        else:
            applicable = filter(_filter, self.completed)

        return sum(applicable)



COMPLETED = CompletedCourses([
    # Fall 2018
    Course("CS", 6052, "INTLDATAANALYSIS", 3.0, "B+", "fall", 2018),
    Course("CS", 6070, "AUTOMATA", 3.0, "B+", "fall", 2018),
    Course("CS", 6097, "WIRELESS NET", 3.0, "B+", "fall", 2018),
    Course("CS", 7001, "CS SEMINAR I", 1.0, "P", "fall", 2018),
    Course("CS", 7080, "SELF STUDY RESEARCH", 5.0, "P", "fall", 2018),
    # Spring 2019
    Course("CS", 6038, "MALWARE ANALYSIS", 3.0, "A", "spring", 2019),
    Course("CS", 7002, "CS SEMINAR II", 1.0, "P", "spring", 2019),
    Course("CS", 7080, "SELF STUDY RESEARCH", 4.0, "P", "spring", 2019),
    Course("EECE", 7004, "PRACTICAL EXPER", 1.0, "P", "spring", 2019),
    Course("EECE", 7019, "BIO-INSPIRED ROBOTICS", 3.0, "A", "spring", 2019),
    Course("EECE", 7065, "COMPLEX SYS/NETWORKS", 3.0, "A", "spring", 2019),
    # Fall 2019
    Course("CS", 6054, "INFO RETRIEVAL", 3.0, "B", "fall", 2019),
    Course("CS", 7081, "ADV. ALGORITHMS I", 3.0, "A-", "fall", 2019),
    Course("EECE", 6036, "INTELLIGENT SYSTEMS", 3.0, "C", "fall", 2019),
    Course("EECE", 9089, "THESIS/DIS RESEARCH", 6.0, "P", "fall", 2019)
])

INPROGRESS = [
    # Spring 2020
    Course("CS", 6053, "NETWORK SECURITY", 3.0, "A", "spring", 2020),
    Course("CS", 8035, "ADV. TP DATA SECURITY/PRIVACY", 3.0, "A", "spring",
        2020),
    Course("EECE", 9089, "THESIS/DIS RESEARCH", 6.0, "P", "spring", 2020),
    # Fall 2020
    Course("EECE", 7095, "INTRO COMPUTER ARCH", 3.0, "A", "fall", 2020),
    Course("EECE", 9089, "THESIS/DIS RESEARCH", 15.0, "P", "fall", 2020)
    ]

def main(args=None):
    """Main function of this file

    Arguments:
    args: List of strings to be parsed by argparse.
        None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args(args=args)

    for course in COMPLETED.completed:
        print(course)

    print("Total Credit Hours: {}".format(COMPLETED.credit_hours()))

    # Return success code
    return 0


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    exit(main())

