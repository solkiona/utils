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
    result_dict = { }
    for count, pwd in enumerate(userpasswords):
        if len(pwd) < 6:
            #print("Weak")
            result.add("Weak")
            result_dict[f"pwd {count + 1}"] = "Weak"
        
        if len(pwd) >= 6 or len(pwd) >= 8:
            num = []
            spc = []

            for char in pwd:
                if char in checks[0]:
                    num.append(char)
                if char in checks[1]:
                    spc.append(char)
            if num and spc:
                #print("Strong")
                result.add("Strong")
                result_dict[f"pwd {count + 1}"] = "Strong" 
            else: 
                result.add("Medium")
                result_dict[f"pwd {count + 1}"] = "Medium"
    print(result)
    print(result_dict)
    return result_dict

res = passwordChecker(["tes1&","Solomon*&*","89887887","90dkdkd2@@####","weak_password"])


for key, value in res.items():
    print(f"{key}: {value}")