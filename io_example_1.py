# This code snippet won't work, check the last comment to fix it.
# Accept input from user via the keyboard and typecast the value recieved as a string data type.

# Code Goes Here
Age = input("Enter your age in numbers [18, 55, etc.]: ")
if Age < 18:
    print("Minors are not allowed here.")
else:
    print("You can vote, get married, and have fun! Enjoy!")
# Code Ends Here

# To fix the problem in the code, change the 1st line of code to:
# Age = int(input("Enter your age in numbers [18, 55, etc.]: "))
# OR
# Age = float(input("Enter your age in numbers [18, 55, etc.]: "))
