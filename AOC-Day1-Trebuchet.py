# Advent of Code 
# Day 1 - Trebuchet?!

import os
import os



def main():
    # Change the current working directory
    os.chdir("/Users/kai/Documents/code/AdventOfCode")

    # Open the input file
    with open("puzzle_input_1", "r") as df:
        # Read all lines from the file
        puzzle_input = df.readlines()

        # Initialize a variable to store the total
        total = 0

        # Iterate over each line in the input
        for l in puzzle_input:
            # Create an empty list to store the numbers
            num_list = []
            # Iterate over each character in the line
            for letter in range(len(l)):
                # Check if the character is a letter
                if l[letter].isalpha():
                    continue
                else:
                    # If it's not a letter, add it to the list
                    num_list.append(l[letter])

            # Remove the newline character from the list
            num_list.remove('\n')

            # Convert the first and last numbers in the list to integers
            new_num = int(num_list[0] + num_list[-1])

            # Add the new number to the total
            total += new_num

    # Print the total
    print(total)

if __name__ == "__main__":
    main()

