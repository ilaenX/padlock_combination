# Password Combination Generator for Padlock

## Description

The "Password Combination Generator for Padlock" is a Python tool designed to help users generate potential combinations for a padlock password. Users provide a subset of remembered digits, and the program systematically generates all possible password combinations for the remaining digits. This project aims to assist users in recovering forgotten padlock codes by offering a comprehensive list of potential passwords for quick identification.

## Time Complexity

The time complexity of the generate_padlock_passwords function in the optimized code depends on two cases. When the user doesn't remember any digits, the code generates all combinations of the desired password length from the range of numbers [1, 50]. This operation's time complexity is proportional to the number of combinations, which is approximately 19600. In the scenario where the user recalls some digits but not their positions, the code generates all permutations of the remembered digits combined with the remaining numbers. The maximum number of remembered digits is 3, and the remaining numbers can be at most 47. This results in a maximum of 114600 permutations. In both cases, generating each combination or permutation takes O(length) time. Considering these factors, the overall time complexity of the function can be approximated as O(N^3), where N is the range of numbers, specifically 50 in this context.

## System Requirements

- Python 3.10
- RAM: 12GB or more (Recommended)
