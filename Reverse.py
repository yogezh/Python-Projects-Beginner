print("::: LETS REVERSE THE VALUE ENTERED BY THE USER AND PRINT IT :::")
UserInput = int(input("Enter your value : "))
reverse = 0
while (UserInput>0):
    # Running a loop until the value entered by user becomes 0
    remainder = UserInput % 10
    # Storing remainder to push it at first position one by one to make a reverse number
    reverse = reverse * 10 + remainder
    # Logic to store reverse number of user's entered value
    quotient = UserInput // 10
    # To understand it better let's find quotients exact value to calculate further for next remainder
    UserInput = quotient
    # storing quotient in userinput value so the next remainder can perform in that new value
print("The reverse value of your entered number is : ",reverse)