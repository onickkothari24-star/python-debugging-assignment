"""
Question 3 practice exercise: Debug this script.

The script is intentionally incorrect. Find and fix the three bugs.
Do not delete the tests; use them to check your fixes.
"""


def calculate_average(numbers):
    # Bug 1: The denominator is incorrect.
    total = sum(numbers)
    return total / len(numbers)


def find_largest(numbers):
    # Bug 2: This starts with the wrong initial value for all-negative lists.
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def count_even(numbers):
    # Bug 3: The condition mistakenly counts odd numbers.
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    sample = [2, 4, 6, 8]
    print("Average:", calculate_average(sample))
    print("Largest:", find_largest(sample))
    print("Even count:", count_even(sample))
