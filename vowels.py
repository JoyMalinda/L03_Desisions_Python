def value_of_letter():
    lett = input("Enter a letter: ")
    letter = lett.lower()
    
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print(f"'{letter}' is a vowel.")
    else:
        print(f"'{letter}' is a consonant.")
value_of_letter()    