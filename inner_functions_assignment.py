"""
Program: inner_functions_assignment
Author: Ryan Blankenship
Last Date Modified: 10/1/2019

The purpose of this program is to calculate the
area and the perimeter of a rectangle from a
list of numbers.
"""


def measurements(measurement_list):
    def area(area_list):
        area_result = 1
        for i in area_list:
            area_result *= i
        return area_result

    def perimeter(perimeter_list):
        perimeter_result = 0
        for i in perimeter_list:
            perimeter_result += i
        return perimeter_result * 2

    area = area(measurement_list)
    perimeter = perimeter(measurement_list)
    return "Perimeter = " + str(perimeter) + " Area = " + str(area)


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
