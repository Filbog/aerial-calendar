import calendar


def generate_yearly_calendar(year):
    print(calendar)
    cal = calendar.Calendar(firstweekday=0)
    yearly_calendar = {}

    for month in range(1, 13):
        # generate all weeks in the month
        weeks = cal.monthdatescalendar(year, month)
        # the function above returns a 2D array of "full" weeks,so there are also days of the next month to make the week "full". I want to filter those out
        filtered_weeks = [[day for day in week if day.month == month] for week in weeks]
        monthly_calendar = {"name": calendar.month_name[month], "weeks": filtered_weeks}
        yearly_calendar[month] = monthly_calendar

    # print(yearly_calendar)
    return yearly_calendar


print(generate_yearly_calendar(2024)[1])
