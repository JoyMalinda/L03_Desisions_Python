def even_odd():
    num1 = int(input("Enter a number: "))
    num2 = num1%2==0
    if num2 == True:
        print(f"{num1} is even.")
    else:
        print(f"{num1} is odd.")

even_odd()