def leap_year():
    year = int(input("Enter a year: "))
    year2 = year % 4==0

    if year2==True:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
leap_year()