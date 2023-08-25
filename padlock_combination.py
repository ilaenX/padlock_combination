'''
Name: Daniel Adeyelu

File: padlock_combination.py

Description: The "Password Combination Generator for Padlock" is a Python tool that utilises the theory of permutation and combination which assists users in creating potential padlock passwords. Users input remembered digits, and the program generates all possible combinations for the remaining digits, using a systematic approach of combinations and permutations. This project aids users in 
recovering forgotten padlock codes by providing an array of possible passwords for quick identification.
'''

import itertools

# Define the range and the password length
start_number = 1
end_number = 50
password_length = 3

def generate_padlock_passwords(start, end, length, remembered_part):
    passwords = []

    # Calculate the number of missing digits in the password
    missing_piece = length - len(remembered_part)

    # Check if the remembered part is longer than the desired password length
    if missing_piece < 0:
        return passwords

    remaining_numbers = set(range(start, end + 1)) - set(remembered_part)

    if not remembered_part:  # User doesn't remember anything
        for combination in itertools.combinations(remaining_numbers, length):
            passwords.append(list(combination))
    else:
        for combination in itertools.combinations(remaining_numbers, missing_piece):
            for permutation in itertools.permutations(remembered_part + list(combination)):
                passwords.append(list(permutation))

    return passwords

print("\n-----------------------------------------")
print("Enter the remembered part of the password")
print("-----------------------------------------\n")
print("Note: use spaces to separate numbers (max three numbers)\n")

remembered_part = list(map(int, input("Numbers: ").split()))

passwords = generate_padlock_passwords(start_number, end_number, password_length, remembered_part)

# Generate the total number of possible passwords
total_passwords = len(passwords)

print("Total number of possible passwords:", total_passwords)
print("Possible Passwords:")
for password in passwords[:200]:
    print(' '.join(map(str, password)))
