# Prompt for a number.
number = int(input("Enter a number: "))

# Use if-else to check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Prompt the user for a year
year = int(input("Enter a year (yyyy): "))

# Leap year check
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")