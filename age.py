import time

birthday_year = int(input("Write your birthday year hear: "))

year_now = time.strftime("%Y")

age = int(year_now) - birthday_year

print(f"Your age => {age}")