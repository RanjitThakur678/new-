# name = "Ranjit"
# print(name.center(10,"!"))
# name= input("enter your name :")
# print(name.center(len(name)+8,"*"))

def leap(year):
    "year -> 1 if leap year, else 0."
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f"{year} is a leapyear"
    return "Not a leap year"

def _days_before_year(year):
    "year -> number of days before January 1st of year."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400

print(leap(2015))
print(_days_before_year(2012))