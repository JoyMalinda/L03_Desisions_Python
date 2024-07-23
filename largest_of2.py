def largest_number():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1<num2:
        print(f"{num2} is larger than {num1}")
    elif num2<num1:
        print(f"{num1} is larger than {num2}")
    else:
        print("The numbers are equal.")
largest_number()