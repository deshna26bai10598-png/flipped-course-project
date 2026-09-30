from datetime import date

def calculate_age(birth_date):
     today = date.today()
     age = today.year - birth_date.year
     if (today.month, today.day) < (birth_date.month, birth_date.day):
                 age -= 1
     return age

     year = int(input("Enter birth year (YYYY): "))
     month = int(input("Enter birth month (1-12): "))
     day = int(input("Enter birth day (1-31): "))
     dob = date(year, month, day)
     current_age = calculate_age(dob)
     print(f"\nYou are {current_age} years old.")