# Programmer: Alex Bean
# Course: CS151, Dr. Rajeev
# Date: Oct 6 2021
# Programming Assignment: 2
# Program Inputs: The month and the year
# Program Outputs: How many days are in a given month and if it is a leap year

MonthNumber=input("What is the number of the month (1-12)? ")

while not (MonthNumber.isdigit()):
    print("Invalid number")
    MonthNumber = input("What is the number of the month (1-12)? ")

MonthNumber=int(MonthNumber)

year=input("What year is it? ")

while not (year.isdigit()):
    print("Invalid number")
    year = input("Enter the year:")

year=int(year)

#If month was 1, 3, 5, 7, 8, 10, or 12 there are 31 days
if MonthNumber==1 or MonthNumber==3 or MonthNumber==5 or MonthNumber==7 or MonthNumber==8 or MonthNumber==10 or MonthNumber==12:
    NumberOfDays=31

elif MonthNumber==2:
    if year%100==0:
        if year%400==0:
            NumberOfDays=29
        else:
            NumberOfDays=28
    else:
        if year%4==0:
            NumberOfDays=29
        else:
            NumberOfDays=28

#If month was 4, 6, 9, or 11 there are 30 days
elif MonthNumber==4 or MonthNumber==6 or MonthNumber==9 or MonthNumber==11:
    NumberOfDays=30

print("There are", NumberOfDays, "days in the", MonthNumber, "month of the year", year)