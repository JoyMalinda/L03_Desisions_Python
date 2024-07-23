def grading():
    marks = int(input("Enter the marks of the student "))

    if marks > 100 or marks < 0:
        print("Error: Invalid Entry.")
    elif marks >= 90:
        print("Excellent performance.")
    elif marks >= 80 and marks < 90:
        print("Very Good performance.")
    elif marks >= 70 and marks < 80:
        print("Good performance.")
    elif marks >= 60 and marks < 70:
        print("Average performance.")
    else:
        print("Poor performance.")
grading()