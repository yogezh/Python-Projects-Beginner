userinput = int(input("Enter your number to check if it's prime number or not: "))
for y in range(2, userinput):
    if userinput % y == 0:
        print("Your number %d is not a Prime Number. "%userinput,y)
        break
    else:
        print("Your number %d is a Prime Number. "%userinput,y)
        break
        # Use break statement to get out of loop
        

