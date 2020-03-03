#!/usr/bin/env python3

__author__="Tyler Westland"

import argparse
import os

from courses import COMPLETED, INPROGRESS

# The blank requirements class and list
class Requirement:
    def __init__(self, name, description, required_ammount):
        self.name = name
        self.description = description
        self.required_ammount = required_ammount


    def completed(self, completed_courses):
        """Amount"""
        raise NotImplemented


    def completion(self, completed_courses):
        """Return True or False if completed"""
        return self.required_ammount <= self.completed(completed_courses)


    def progress(self, completed_courses):
        """Return string describing progress"""
        return "{completed}/{required} credits completed".format(
                completed=int(self.completed(completed_courses)),
                required=self.required_ammount)
REQUIREMENTS = []



def doctoral_course_proposal_filter(course):
    if course.department == "EECE" and course.number == 9080:
        return True
    elif course.department == "CS" and course.number == 8080:
        return True
    else:
        return False


def non_doctoral_proposal_course_filter(course):
    return not doctoral_course_proposal_filter(course)


# The actual requirements, each added to the list
class PostBachelorsCredits(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Post Bachelors Credits", "93 credit hours",
                93)

    def completed(self, completed_courses):
        # The doctoral proposal can only be counted for up to 6 credits
        
        non_doctoral_credits = completed_courses.credit_hours(
                non_doctoral_proposal_course_filter)
        doctoral_credits = completed_courses.credit_hours(
                doctoral_course_proposal_filter)

        # Only 6 credits of doctoral proposal count
        return non_doctoral_credits + min(6, doctoral_credits)


REQUIREMENTS.append(PostBachelorsCredits())



class ResearchHours(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Research Hours", "60 credit hours",
                60)

    def completed(self, completed_courses):
        doctoral_credits = completed_courses.credit_hours(
                doctoral_course_proposal_filter)

        def course_filter(course):
            if course.department == "CS" and course.number == 8089:
                return True
            elif course.department == "EECE" and course.number == 9089:
                return True
            else:
                return False

        research_credits = completed_courses.credit_hours(course_filter)
        # Only 6 credits of doctoral proposal count
        return research_credits + min(6, doctoral_credits)
REQUIREMENTS.append(ResearchHours())



class CourseWorkCredits(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Course Work Credits", "30 credit hours",
                30)

    def completed(self, completed_courses):
        def course_filter(course):
            return course.grade != "P"
        return completed_courses.credit_hours()
REQUIREMENTS.append(CourseWorkCredits())



class AdvancedGraduateCoursework(Requirement):
    def __init__(self):
        Requirement.__init__(self, "Advanced Graduate Coursework",
                "15 7XXX+", 15)

    def completed(self, completed_courses):
        def course_filter(course):
            if course.number >= 7000:
                if course.grade != "P":
                    return True
            return False
        return completed_courses.credit_hours(course_filter)
REQUIREMENTS.append(AdvancedGraduateCoursework())



class GeneralComputerScienceTrack(Requirement):
    def __init__(self):
        Requirement.__init__(self, "General Computer Science Track",
                "CS6070 and CS7081", 6)

    def completed(self, completed_courses):
        def course_filter(course):
            if course.department == "CS" and course.number == 6070:
                return True
            elif course.department == "CS" and course.number == 7081:
                return True
            else:
                return False
        return completed_courses.credit_hours(course_filter)
REQUIREMENTS.append(GeneralComputerScienceTrack())



def main(args=None):
    """Main function of this file

    Arguments:
    args: List of strings to be parsed by argparse.
        None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--what_if", help="If set then in progress "\
            "courses will be included in the calculations", default=False,
            action="store_true")
    args = parser.parse_args(args=args)

    if args.what_if:
        COMPLETED.completed.extend(INPROGRESS)

    for req in REQUIREMENTS:
        print("{req.name} -- {req.description} -- {completion}".format(req=req,
            completion=req.completion(COMPLETED)))
        print("\tProgress: {progress}".format(progress=req.progress(COMPLETED)))

    # Return success code
    return 0


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    exit(main())

