from datetime import date

current_date = date.today()

birthday = (input('What is your date of birth (yy-mm-dd) : '))

days_from = abs(current_date - birthday)

print(f'You have been alive {days_from} days' )
