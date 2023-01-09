print("LETS TAKE INPUT FROM THE USER FOR TWO SETS CONTAINING 5-10 VALUES IN EACH")
print("In this Program you'll get the out of your two set's Union and Intersection")

s1_range= int(input("How many values you want in your FIRST SET (between 5-10) : "))
s2_range= int(input("How many values you want in your SECOND SET (between 5-10) : "))
set_1 = set()
set_2 = set()
for s1 in range(1,s1_range+1):
    s1_values=int(input("Enter Values for your FIRST SET : "))
    set_1.add(s1_values)
print("Values for FIRST SET are added SUCCESSFULLY")
for s2 in range(1,s2_range+1):
    s2_values=int(input("Enter Values for your SECOND SET : "))
    set_2.add(s2_values)
print("Values for SECOND SET are added SUCCESSFULLY")

print('''
*********************************************
INTERSECTION VALUES OF YOUR SETS ARE :     ||
*********************************************
''')
print(set_1 & set_2)
print('''
*********************************************
UNION VALUES OF YOUR SETS ARE :            ||
*********************************************
''')
print(set_1 | set_2)

