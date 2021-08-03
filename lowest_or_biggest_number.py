# Given a list of numbers, write a method to find the lowest or highest number

def lowest_number(numbers):
    """Method to find the lowest number"""
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    print(f'The lowest number is {lowest}')


def highest_number(numbers):
    """Method to find the highest number"""
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    print(f'The highest number is {highest}')


numbers = [123, 4, 6742, 1, -421, 6, 8923, 455, 44, 90, -1, 872]
lowest_number(numbers)
highest_number(numbers)
