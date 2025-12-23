import calendar

def show_calendar(year, month):
    print("\n📅 Calendar")
    print(calendar.month(year, month))


print("=== Python Calendar App ===")

try:
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1-12): "))

    if month < 1 or month > 12:
        print("❌ Invalid month")
    else:
        show_calendar(year, month)

except ValueError:
    print("❌ Please enter valid numbers")
