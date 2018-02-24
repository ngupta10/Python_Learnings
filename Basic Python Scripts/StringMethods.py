"""

len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from
the string assigned  to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last
problem (use the  str() string method for this)

"""

str1 = "Python"
length1 = len(str1)
length2 = len(str1[1:4])
float1 = 1.32
str2 = str(float1)[3]

print(length1,length2,str2)

""" 

.upper() and .lower() practice: 1.create a variable and assign it the string "upper" changed to 
"UPPER" using .upper() 2.create a variable and assign it the string "owe" from "LOWER" using 
string slicing and .lower() 

"""

str3 = "upper"
print(str3.upper())
str4 = "LOWER".lower()[1:4]
print(str4)

""" 

%s and input(): 
1.create a variable to hold a user's favorite restaurant (use input() for this.) 
2.create a variable to hold the name of a place a user wants to visit. 
3.create a variable to hold the user's nickname or first name if they don't have a nickname. 
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], 
you want to visit  [name of place the user wants to visit], and your nickname or first name is 
[nickname or first name]" to a variable 5.print that variable 

"""

restaurant = input("Please Enter your Favourite Restaurant")
place = input("Please Enter the place you want to visit")
name = input("Please Enter your name or nickname")
print("Your favorite restaurant is %s, you want to visit %s, and your nickname or first name is %s."%(restaurant,place,name))
