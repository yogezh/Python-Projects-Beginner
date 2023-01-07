userinput=(int(input("Enter your number to check if its prime number or not: ")))
for y in range(2,userinput):
    if userinput % y == 0:
        print("Your number %d is not a Prime Number."%userinput)
        break
    # break function will break out of the loop once condition is satisfied.
else :
    print("Your number %d is a Prime Number."%userinput)
# We don't want to repeat number of prime numbers so we'll print the result out of loop if number is prime.
