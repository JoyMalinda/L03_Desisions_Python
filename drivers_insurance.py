def drivers_insurance():

    marriedQ = input("Are you married [y/n]: ")
    marriedA = marriedQ.lower()

    genderQ = input("What is your gender [m/f]? ")
    genderA = genderQ.lower()

    age = int(input("How old are you? "))

     
    if marriedA == "y" or marriedA == "yes":
        print("You are insured.")
    elif marriedA == "n" and genderA == "m" or genderA == "male" and age>30:
        print("You are insured.")
    elif marriedA == "n" and genderA == "f" or genderA == "female" and age>25:
        print("You are insured.")
    else:
        print("Sorry, you are not insured.")
drivers_insurance()

