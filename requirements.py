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
        # The doctoral proposal can only be counted for up to 6 credits
        def non_doctoral_proposal_course_filter(course):
            return course.number != 9080
        non_doctoral_credits = completed_courses.credit_hours(
                non_doctoral_proposal_course_filter)

        def doctoral_course_proposal_filter(course):
            return course.number == 9080
        doctoral_credits = completed_courses.credit_hours(
                doctoral_course_proposal_filter)

        return 93 <= non_doctoral_credits + min(6, doctoral_credits)
REQUIREMENTS.append(PostBachelorsCredits())



class ResearchHours(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Research Hours", "60 credit hours")

    def completion(self, completed_courses):
        def course_filter(course):
            if course.department == "CS" and course.number == 8089:
                return True
            elif course.department == "EECE" and course.number == 9089:
                return True
            else:
                return False
        return 60 <= completed_courses.credit_hours(course_filter)
REQUIREMENTS.append(ResearchHours())



class CourseWorkCredits(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Course Work Credits", "30 credit hours")

    def completion(self, completed_courses):
        def course_filter(course):
            return course.grade != "P"
        return 30 <= completed_courses.credit_hours()
REQUIREMENTS.append(CourseWorkCredits())



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



class GeneralComputerScienceTrack(Requirement):
    def __init__(self):
        Requirement.__init__(self, "General Computer Science Track",
                "CS6070 and CS7081")

    def completion(self, completed_courses):
        def course_filter(course):
            if course.department == "CS" and course.number == 6070:
                return True
            elif course.department == "CS" and course.number == 7081:
                return True
            else:
                return False
        return 2 <= completed_courses.credit_hours(course_filter)
REQUIREMENTS.append(GeneralComputerScienceTrack())



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

