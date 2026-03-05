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
                print("k must be 10 and above.")
        except ValueError:
            print("Please enter a valid integer.")

    print("\nSearching for near misses for x^n + y^n ≈ z^n ...")
    print(f"Using n = {n}, x and y from 10 to {k}\n")

    # Track the best (smallest) relative miss found so far
    best_rel = float("inf")
    best_info = None

    """ Loop purpose: Iterate through all x and y values in the required range"""

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            s = (x ** n) + (y ** n)

            z = int(round(s ** (1 / n)))

            # Check BOTH sides: z and z+1, pick the smaller miss
            miss1 = abs(s - (z ** n))
            miss2 = abs(((z + 1) ** n) - s)

            if miss2 < miss1:
                miss = miss2
                z_used = z + 1
            else:
                miss = miss1
                z_used = z

            rel_miss = miss / s

            # If we found a new best, store and print it
            if rel_miss < best_rel:
                best_rel = rel_miss
                best_info = (x, y, z_used, miss, rel_miss)

                # Print well-labeled output every time we improve
                print("NEW BEST NEAR MISS FOUND:")
                print(f"  x = {x}")
                print(f"  y = {y}")
                print(f"  n = {n}")
                print(f"  z = {z}  (closest power is z^n or (z+1)^n)")
                print(f"  miss (integer) = {miss}")
                print(f"  relative miss  = {rel_miss:.12f}   ({rel_miss * 100:.10f}%)")
                print("-" * 50)

                # Final result (last thing printed should show the smallest miss)
            if best_info is not None:
                x, y, z, miss, rel_miss = best_info
                print("\nFINAL BEST RESULT (smallest relative miss found):")
                print(f"  x = {x}, y = {y}, n = {n}")
                print(f"  z = {z}")
                print(f"  miss (integer) = {miss}")
                print(f"  relative miss  = {rel_miss:.12f}   ({rel_miss * 100:.10f}%)")
            else:
                print("No results found (this should not happen).")

                # Pause so the output stays visible in the IDE
            exit(input("\nPress Enter to exit..."))

if __name__ == "__main__":
    near_miss()



