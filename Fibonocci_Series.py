print("You don't know what's fibonocci series ? :/ It's k, I'll tell you :) ")
print("Fibonocci series is an addition of last 2 digits like, 0,1,1(0+1),2(1+1),3(1+2),5(2+3),8(3+5)....  and it goes on and on and on")
print("So now you know Fibonocci Series then Let's begin the programming :) ")

print("WELCOME, LET'S FIND OUT THE FIBONOCCI NUMBER OF YOUR ENTERED POSITION'S VALUE ")
position = int(input("Enter your position number to get the value of fibonocci series : "))
first = 0
second = 1
if position == 0:
    print("Found it! The Fibonocci value for your entered position %d is : %d "%(position,first))
elif position == 1:
    print("Found it! The Fibonocci value for your entered position %d is : %d "%(position,second))
else :
    for y in range(2,position+1):
        nxt = first + second 
        first = second 
        second = nxt
        print(nxt,end=" ")
    print()
    print("Found it! The Fibonocci value for your entered position %d is : %d "%(position,nxt))