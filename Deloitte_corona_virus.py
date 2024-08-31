'''Every decimal number can be changed into its binary form. Suppose your computer has it’s own CoronaVirus, that eats binary digits from the right side of a number. Suppose a virus has 6 spikes, it will eat up 6 LSB binary digits in your numbers.
You will have a bunch of numbers, and your machine will have a virus with n spikes, you have to calculate what will be the final situation of the final numbers.'''

# Read the number of integers in the list `a`.
N = int(input("Enter the number of integers: "))

# Read the list of integers from input, separated by spaces.
a = list(map(int, input("Enter the numbers separated by spaces: ").split()))

# Read the number of spikes of the virus (i.e., the number of LSBs to remove).
n = int(input("Enter the number of virus spikes (LSBs to remove): "))

# Initialize an empty string `s` to store the resulting numbers.
s = ""

# Iterate over each number in the list `a`.
for i in a:
    # Perform a right bitwise shift by `n` positions to remove the LSBs.
    # Convert the resulting number back to a string and append it to `s`, followed by a space.
    s += str(i >> n) + " "

# Print the final numbers after the virus has eaten the LSBs.
print("Final numbers after the virus attack:", s)
