print("WELCOME , LETS FIND THE FACTORIAL OF YOUR GIVEN NUMBER: ")
userinput = int(input("Enter your number to find the factorial : "))
# Taking user input for which user wants factorial number
factorial = 1
for y in range(1,userinput+1):
    # Running a loop from 1 to the user's value + 1 as the ending number is exclusive 
    factorial = factorial * y
    # Here, factorial named variable will keep multiplying the incrementing number i.e y and store it in a loop
print("Factorial of your given number is : ",factorial)
# Printing the value outside of the loop


