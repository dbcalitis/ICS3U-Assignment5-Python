#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program adds fractions


def main():
    # This function adds a series of fractions
    # input
    max_denominator = input("Enter an integer for a max denominator: ")

    # process & output
    try:
        total = 0
        max_denominator = int(max_denominator)
        for counter in range(1, max_denominator + 1):
            total += 1 / counter

        print("The sum is {0}".format(total))
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
