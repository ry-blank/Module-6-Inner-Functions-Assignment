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
        if len(area_list) > 1:
            area_result = 1
            for l in area_list:
                area_result *= l
            return area_result
        else:
            area_squared = area_list[0] * area_list[0]
            return area_squared

    def perimeter(perimeter_list):
        if len(perimeter_list) > 1:
            perimeter_result = 0
            for l in perimeter_list:
                perimeter_result += l
            return perimeter_result * 2
        else:
            perimeter_squared = perimeter_list[0] * 4
            return perimeter_squared

    area = area(measurement_list)
    perimeter = perimeter(measurement_list)
    return "Perimeter = " + str(perimeter) + " Area = " + str(area)


if __name__ == '__main__':
    print(measurements([0, 0]))
