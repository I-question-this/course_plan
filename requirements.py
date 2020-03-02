#!/usr/bin/env python3

__author__="Tyler Westland"

import argparse
import os

from courses import COMPLETED

# The blank requirements class and list
class Requirement:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def completion(self, completed_courses):
        """Return True or False if completed"""
        raise NotImplemented
REQUIREMENTS = []



# The actual requirements, each added to the list
class PostBachelorsCredits(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Post Bachelors Credits", "93 credit hours")

    def completion(self, completed_courses):
        return 93 <= completed_courses.credit_hours()
REQUIREMENTS.append(PostBachelorsCredits())



class AdvancedGraduateCoursework(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Advanced Graduate Coursework",
                "15 7XXX+")

    def completion(self, completed_courses):
        def course_filter(course):
            if course.number >= 7000:
                if course.grade != "P":
                    return True
            return False
        return 15 <= completed_courses.credit_hours(course_filter)
REQUIREMENTS.append(AdvancedGraduateCoursework())


def main(args=None):
    """Main function of this file

    Arguments:
    args: List of strings to be parsed by argparse.
        None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args(args=args)

    for req in REQUIREMENTS:
        print("{req.name} -- {req.description} -- {completion}".format(req=req,
            completion=req.completion(COMPLETED)))

    # Return success code
    return 0


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    exit(main())

