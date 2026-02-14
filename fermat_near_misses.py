"""
Title: Fermat Near Miss Finder
File: fermat_near_misses.py
Programmers: Biju Jacob, Carlos F
Course: Software Engineering
Date completed/submitted: 02/15/2026
Purpose:
    Interactive program to search for "near misses" to Fermat's Last Theorem.
    For user-provided n and k, the program checks all pairs (x, y) where
    10 <= x <= k and 10 <= y <= k, and finds z such that z^n is closest to (x^n + y^n).
    It prints a line whenever a new smallest relative miss is found.
"""

def near_miss():

    while True:
        try:
            n = int(input("Enter n, the power to use in the equation: ").strip())
            if 2 < n < 12:
                break
            else:
                print("n must be between 3 and 11.")
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            k = int(input("Enter k, the range of x and y: ").strip())
            if k > 10:
                break
            else:
                print("k must be 11 and above.")
        except ValueError:
            print("Please enter a valid integer.")

    """ Loop purpose: Iterate through all x and y values in the required range"""
    smallest_miss = 1  # Initialize before the loops

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            s = (x ** n) + (y ** n)
            z = round(s ** (1 / n))
            miss = abs(s - (z ** n))
            rel_miss = miss / s
            if rel_miss < smallest_miss:
                smallest_miss = rel_miss
                print(f"x={x}, y={y}, z={z}, n={n}, miss={miss}, relative miss={rel_miss}")


