print("::: LETS CHECK IF THE ENTERED NUMBER IS PALINDROME OR NOT :::")
print(" :: YOU DON'T KNOW PALINDROME? K, LET ME EXPLAIN, IF USER'S VALUE AND REVERSE OF THAT VALUE ARE SAME THEN IT'S CALLED PALINROME. K? GOOD :) ")
UserInput = int(input("Enter your value : "))
reverse = 0
Palindrome = UserInput
while (UserInput>0) :
    remainder = UserInput % 10
    reverse = reverse * 10 + remainder
    quotient = UserInput // 10
    UserInput = quotient
if (Palindrome == reverse):
    print("IT'S A PALINDROME AS"," Your value : ",Palindrome, " is equal to : ", reverse)
else:
    print("IT'S NOT A PALINDROME AS "," Your value : ",Palindrome, " is not equal to : ", reverse)
    