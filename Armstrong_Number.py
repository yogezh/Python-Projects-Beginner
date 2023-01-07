print("*************************************************************************************************|")
print('''LETS CHECK IF THE NUMBER ENTERED BY USER IS ARMSTRONG NUMBER OR NOT!                           |
********************************************************************************************************|
Jeez! you don't know what's an armstrong number? :/ it's k I'll tell you                                |
Here, we take number of digits as a power to the each digit and make addition of them to check          |
if it's equal to the user's entered number or not!                                                      |
For eg. 153 have total 3 digits so if (1)3 + (5)3 + (3)3 = 153 then it's an armstrong number and it is! |
********************************************************************************************************|
''')
userinput = int(input("Enter your number to check if it's Armstrong number or not: "))
power = int(len(str(userinput)))
sumofall = 0
armstrong = userinput
while(userinput > 0):
    remainder = userinput % 10
    sumofall = sumofall + (remainder ** power)
    quotient = userinput // 10
    userinput = quotient
if armstrong == sumofall:
    print("Your number %d is an Armstrong Number! "%armstrong)
else:
    print("Your number %d is not an Armstrong Number."%armstrong)
