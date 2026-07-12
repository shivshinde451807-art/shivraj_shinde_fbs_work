#WAP to convert days into years, week and days,
days = int(input("enter the number of days:"))
years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) // 7
print("years",years)
print("weeks",weeks)
print("remaining_days",remaining_days)