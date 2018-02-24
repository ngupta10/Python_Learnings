""" string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it

"""

str = "Nishant is studying Big Data"
str1 = 'Nishant is studying Programmming'
str2 = "Nishant is reading the book \"Learn Python the hard way\" by himself"
str3 = 'Nishant is reading the book \"Learn Python the hard way\" by himself'

print(str,str1,str2,str3)

""" accessing values by index and string slicing: 
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion" 
2.create a variable and assign it the "a" from the string assigned to the variable lannisters. 
3.create a variable and assign it the "J" from the string assigned to the variable lannisters. 
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters. 
5.create a variable and assign it "Cersei" from the string  assigned to the variable lannisters. 
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters. """

lannisters = "JaimeCerseiTyrion"
st1 = lannisters[1]
st2 = lannisters[0]
st3 = lannisters[0:5]
st4 = lannisters[5:11]
st5 = lannisters[11:]

print(st1,st2,st3,st4,st5)