"""A module to implement function that checks for leap year.
"""
import sys

def is_leap_year(year_local: int) -> bool:
    """A function that checks whether the passed argument is a leap year or not.
    """
    return (year_local % 4 == 0) and (year_local % 100 != 0 or year_local % 400 == 0)

if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("You must enter an integer. Please try again.", file=sys.stderr)
        sys.exit(1)

    if is_leap_year(year):
        print("It is a leap year.")
    else:
        print("It is not a leap year.")
