def check_substring():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check: ")
    
    if substring in main_string:
        print(f"'{substring}' is a substring of '{main_string}'.")
    else:
        print(f"'{substring}' is not a substring of '{main_string}'.")

def count_occurrences():
    main_string = input("Enter the main string: ")
    char = input("Enter the character to count: ")
    
    count = main_string.count(char)
    print(f"The character '{char}' occurs {count} times in '{main_string}'.")

def replace_substring():
    main_string = input("Enter the main string: ")
    old_substring = input("Enter the substring to replace: ")
    new_substring = input("Enter the new substring: ")
    
    new_string = main_string.replace(old_substring, new_substring)
    print("New string:", new_string)

def convert_to_capital():
    main_string = input("Enter the main string: ")
    capitalized_string = main_string.upper()
    print("Capitalized string:", capitalized_string)

while True:
    print("\nMenu:")
    print("A) Check String is Substring of Another String")
    print("B) Count Occurrences of Character")
    print("C) Replace a substring with another substring")
    print("D) Convert to Capital Letters")
    print("E) Exit")
    
    choice = input("Enter your choice (A/B/C/D/E): ")
    
    if choice == "A":
        check_substring()
    elif choice == "B":
        count_occurrences()
    elif choice == "C":
        replace_substring()
    elif choice == "D":
        convert_to_capital()
    elif choice == "E":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
