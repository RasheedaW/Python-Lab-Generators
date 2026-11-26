import calendar
import datetime

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    # Validate the month and year
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    if year < 1 or year > 9999:
        raise ValueError("Invalid year.")

    # Display the selected calendar
    print("\nMonthly Calendar:")
    print(calendar.month(year, month))

    # Check today's date
    today = datetime.date.today()

    if today.year == year and today.month == month:
        print("Today is", today.strftime("%B %d, %Y"))
    else:
        print("Today's date is not in the selected month.")
        print("Current date:", today.strftime("%B %d, %Y"))

except ValueError as error:
    print("Error:", error)
