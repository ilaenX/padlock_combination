# Password Combination Generator for Padlock

## Description

The "Password Combination Generator for Padlock" is a Python tool designed to help users generate potential combinations for a padlock password. Users provide a subset of remembered digits, and the program systematically generates all possible password combinations for the remaining digits. This project aims to assist users in recovering forgotten padlock codes by offering a comprehensive list of potential passwords for quick identification.

## Time Complexity

The time complexity of this program depends on the number of possible passwords generated and the length of the remembered portion. The generation process involves combinations and permutations, resulting in a time complexity of approximately O(C(n, r) * (n - r)!), where n is the range of numbers (1 to 50) and r is the length of the remembered portion. While execution time may vary based on input parameters, the program is optimized for relatively small password lengths and remembered portions.

## System Requirements

- Python 3.x
- RAM: 16GB or more (Recommended)

Please ensure that your system meets the minimum RAM requirement of 16GB to ensure smooth execution of the program, especially for larger password lengths.
