'''
Name: Daniel Adeyelu

File: padlock_combination.py

Description: The "Password Combination Generator for Padlock" 
is a Python tool that assists users in creating potential padlock 
passwords. Users input remembered digits, and the program generates 
all possible combinations for the remaining digits, using a systematic 
approach of combinations and permutations. This project aids users in 
recovering forgotten padlock codes by providing an array of possible 
passwords for quick identification.
'''
import itertools

start_number = 1
end_number = 50
password_length = 3

def generate_padlock_passwords(start, end, length, remembered_part):
    numbers = list(range(start, end + 1))
    passwords = []
    
    missing_piece = length - len(remembered_part)
    
    if missing_piece < 0:
        print("Remembered part is longer than the password length.")
        return passwords
    
    for combo in itertools.combinations(numbers, missing_piece):
        remaining_numbers = [num for num in numbers if num not in remembered_part + list(combo)]
        for perm in itertools.permutations(remaining_numbers, len(remaining_numbers)):
            full_combo = list(remembered_part) + list(combo) + list(perm)
            passwords.append(full_combo)
    return passwords


print("\n-----------------------------------------")
print("Enter the remembered part of the password")
print("-----------------------------------------\n")
print("Note: use spaces to separate numbers (max three numbers)\n")

remembered_part = input("Numbers: ").split()
remembered_part = list(map(int, remembered_part))

passwords = generate_padlock_passwords(start_number, end_number, password_length, remembered_part)

total_passwords = len(passwords)

print("Total number of possible passwords: {}".format(total_passwords))
print("Sample passwords:")
for password in passwords[:10]:
    print(' '.join(map(str, password)))