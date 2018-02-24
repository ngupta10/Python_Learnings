# coding=utf-8
# Authored by Nishant Gupta
"""
Write a program to remove the following form:
www.college.ca
Remove all w’s before and after .college.
Remove all lowercase letter before and after .college.
Remove all printable characters.

"""

#Function to remove all w's before and after .college.

def string_without_w(str_form):
    for letter in str_form:

        index_beg_dot = str_form.index(".")

        index_end_dot = str_form.rindex(".")

        index_w = str_form.find("w")

        if index_w != -1:
            if index_w < index_beg_dot or index_w > index_end_dot:
                str_form = str_form[:index_w]+str_form[index_w+1:]

    return str_form


# Function to remove all lowercase letter before and after .college.

def str_without_lower(str_form):
    beg_pos = 0  ##starting index position
    for letter in str_form:

        index_beg_dot = str_form.index(".")

        index_end_dot = str_form.rindex(".")

        pos = str_form.find(letter,beg_pos)



        if pos != -1 & letter.islower():
            if pos < index_beg_dot or pos > index_end_dot:
                str_form = str_form[:pos]+str_form[pos+1:]

        #else:
            #beg_pos +=1

    return str_form




# Function to Remove all printable characters.
def str_printable(str_form):
    beg_pos = 0  ##starting index position
    for letter in str_form:
        pos = str_form.find(letter)
        if letter !=".":
            str_form = str_form[:pos]+str_form[pos+1:]

    return str_form



str_form = "www.college.ca"

str = string_without_w(str_form)
print ("After removing all w's before and after \".college.\" from \"%s\" : %s"%(str_form,str))

str = str_without_lower(str_form)
print ("After removing all lowercase letter before and after \".college.\" from \"%s\" : %s"%(str_form,str))

str = str_printable(str_form)


print("After removing all printable characters from \"%s\" : %s"%(str_form,str))