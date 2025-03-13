def detect_letter_type():
    while True:
        letter = input("Enter a single letter (or type 'exit' to return to menu): ")
        if letter.lower() == "exit":
            break
        if len(letter) == 1 and letter.isalpha():
            vowels = "AEIOUaeiou"
            print(f"{letter} is a Vowel." if letter in vowels else f"{letter} is a Consonant.")
        else:
            print("----------------------------------------------------")
            print("Invalid input! Please enter a single letter.")
            print("----------------------------------------------------")
            return


def check_odd_even():
    while True:
        number = input("Enter a number (or type 'exit' to return to menu): ")
        if number.lower() == "exit":
            break
        try:
            num = float(number)
            if num % 2 == 0:
                print(f"{number} is Even.")
            else:
                print(f"{number} is Odd.")
        except ValueError:
            print("----------------------------------------------------")
            print("Invalid input! Please enter a valid number.")
            print("----------------------------------------------------")


def detect_special_character():
    while True:
        char = input("Enter a single character (or type 'exit' to return to menu): ")
        if char.lower() == "exit":
            break
        if len(char) == 1:
            print(f"{char} is a Special Character." if not char.isalnum() else f"{char} is NOT a Special Character.")
        else:
            print("----------------------------------------------------")
            print("Invalid input! Please enter a single character.")
            print("----------------------------------------------------")


def analyze_string():
    while True:
        user_input = input("Enter a string to analyze (or type 'exit' to return to menu): ")
        if user_input.lower() == "exit":
            break
        if user_input.strip():  
            results = []
            for char in user_input:
                if char.isalpha():
                    results.append(f"{char} is a Vowel." if char in "AEIOUaeiou" else f"{char} is a Consonant.")
                elif char.isdigit():
                    results.append(f"{char} is Even." if int(char) % 2 == 0 else f"{char} is Odd.")
                else:
                    results.append(f"{char} is a Special Character.")
            print("\n".join(results))
        else:
            print("----------------------------------------------------")
            print("Invalid input! Please enter at least one character.")
            print("----------------------------------------------------")


if __name__ == "__main__":  
    while True:
        print("\nChoose an option:")
        print("1. Detect Letter Type (Vowel/Consonant)")
        print("2. Check if a Number is Odd or Even")
        print("3. Detect if a Character is a Special Character")
        print("4. Analyze a String (Combination of All)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            detect_letter_type()  

        elif choice == "2":
            check_odd_even()  

        elif choice == "3":
            detect_special_character()  

        elif choice == "4":
            analyze_string()  

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
