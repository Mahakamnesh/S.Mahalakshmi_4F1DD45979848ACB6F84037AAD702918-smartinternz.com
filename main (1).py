year = 2024

# Check if the year is a leap year
is_leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

# Print the result
print(is_leap_year)