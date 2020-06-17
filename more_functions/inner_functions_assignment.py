"""
Program: inner_functions_assignment.py
Author: Paul Ford
Last date modified: 06/17/2020
Purpose: accepts a list of measurements
         for a rectangle and returns a
         string with perimeter and area
"""


def measurements(rect):
    def area(a_list):  # calculates the area
        if len(a_list) > 1:
            return a_list[0] * a_list[1]
        else:
            return a_list[0]**2

    def perimeter(a_list):  # calculates the perimeter
        if len(a_list) > 1:
            return 2 * ((a_list[0]) + (a_list[1]))
        else:
            return a_list[0] * 4

    return "Perimeter = {} Area = {}".format(perimeter(rect), area(rect))


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
