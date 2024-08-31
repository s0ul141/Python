'''After JEE Mains, some students got admission into an engineering college. Now there is a class consisting of such n students, and the HOD came to say it is time to select the class monitor. But He never gets all of them at one time. So he brought a register, every time he gets someone with less rank than the previous time he cut the name and wrote the name of the student and the rank.
For a given number of ranks he gets each time, you have to predict how many names are cut in the list.'''


n = int(input("Enter the number of students: "))
ranks = list(map(int, input("Enter the ranks of students: ").split()))

# Initial conditions
m = ranks[0]  # Start with the first student's rank
cuts = 0      # Initialize the counter for cuts

# Iterate through the ranks starting from the second student
for i in range(1, n):
    if ranks[i] < m:  # If the current rank is better (lower) than the previous
        m = ranks[i]  # Update the recorded rank
        cuts += 1     # Increment the cuts counter

print("Number of names cut:", cuts)

