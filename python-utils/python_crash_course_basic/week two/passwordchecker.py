"""
Task: Simple Password Strength Checker

Write a program that:

Stores a list of user passwords in a collection (list/array/List).

Iterates through each password and:

Checks the length of the password.

Checks if it contains numbers and special characters.

Conditionals:

If password length < 6 → "Weak"

If length ≥ 6 but missing numbers/special characters → "Medium"

If length ≥ 8 and contains both numbers + special characters → "Strong"

Loops:

Use a for loop to process each password.

Use a while loop to simulate checking until all passwords are tested.

Extras (Optional):

Use a set to track unique password strengths ({Weak, Medium, Strong}).

Use a dict/object/map to count how many passwords fall into each category.
"""

def passwordChecker( userpasswords: list ) -> str:
    checks = [
        "1234567890", "~`!@#$%^&*()_-+={[]}\|;:',<.>/?"
    ]
    result = set()
    for pwd in userpasswords:
        if len(pwd) < 6:
            print("Weak")
            result.add("Weak")
        
        if len(pwd) >= 6 or len(pwd) >= 8:
            num = []
            spc = []

            for char in pwd:
                if char in checks[0]:
                    num.append(char)
                if char in checks[1]:
                    spc.append(char)
            if num and spc:
                print("Strong")
                result.add("Strong")
                return "Strong"
           
            print("Medium")
            result.add("Medium")
    return result

passwordChecker(["tes1&","Solomon*&*","89887887","90dkdkd2@@####"])