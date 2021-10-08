"""A module to implement function that checks for leap year.
"""
import sys

def is_leap_year(year: int) -> bool:
    """A function that checks whether the passed argument is a leap year or not.
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def main():
    """The main entry point function.
    """
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("You must enter an integer. Please try again.", file=sys.stderr)
        sys.exit(1)

    if is_leap_year(year):
        print("It is a leap year.")
    else:
        print("It is not a leap year.")

if __name__ == "__main__":
    main()
