# coding=utf-8
# Authored by Nishant Gupta
"""
Q.1 Write a program to print the :
1) Number of lowercase “a” and “o” in the following sentences.
2) Number of uppercase “L” and “N” in the following sentence.

               Discover , Learning ,with ,Python’



"""
def count_words(str):    #define a function for counting the 'a,o,L,N'
    words = 'aoLN'        #A string containing all the words
    count_a = 0
    count_o = 0
    count_L = 0
    count_N = 0
    for i in str:           #traverse the string
        if i in words:      #check if the the character is contained in the string
            if i == "a":
                count_a +=1
            elif i == "o":
                count_o +=1
            elif i == "L":
                count_L +=1
            elif i == "N":
                count_N+=1
    print ("The number of a in \"%s\" = %i"%(str,count_a))
    print ("The number of o in \"%s\" = %i" % (str,count_o))
    print ("The number of L in \"%s\" = %i" % (str, count_L))
    print ("The number of N in \"%s\" = %i" % (str, count_N))

str = "Discover , Learning ,with ,Python'"
count_words(str)  #Function call





