

message=  ""

message2 = "hello Ghaza"  # index  starts from zero
"1- get len of string"
print(len(message2))
"2- slicing the string "
print(message2[1:7])  # 1---> 6
print(message2[::])
print(message2[::2])
print(message2[::-1])  # reverse the string


"3- count char accourence"
print(message2.count("a"))

"""4- get index of char"""
print(message2.index("a"))   # index return with the index of the first occurrence of the char


""" operations on the string """
"concat string "
fname= 'noha'
midname = 'abdelhady'
lname= 'shehab'

fullname = fname+ " "+midname+ " "+lname +str(10) # CONCAT  available between objects from the same types
print(fullname)


""" string is immutable data """
# lname[0]='A'

""" formatting the string """

temp = "we have {0} students in {1} course "
print(temp)
no_of_students = 20
coursename = 'python'

# res=temp.format(no_of_students,coursename)  # retrun new string
# print(temp)
# res=temp.format(coursename, no_of_students)  # retrun new string
# print(res)

temp = "we have {stds} students in {crs} course "  # format using keyword
print(temp.format(crs=coursename, stds=no_of_students))
print(temp.format(crs='mongo', stds=no_of_students))


## f-format string
""" formatting string according to existing variables """
track = 'GIS'
no_of_courses = 30
temp = f"In {track} courses we have {no_of_courses} course"
# when you format this string--> use existing variables
print(temp)


""" ask user enter a name  --> welcome """
# name = input("please enter your name ") ### input function always returns with string
# print(name, type(name))
# welcomemessage = f"Nice to meet you {name}"
# print(welcomemessage)

"""===> examine string content """
# num1 = input("enter first number")
# num2 = input("enter second number")
# ## check if content inside the string is number
#
# print(num1.isdigit())  # return True if string consists only from digits  --> (0->9)
# # res = num1 + num2
# # print(res)
# if num1.isdigit() and num2.isdigit():
#     res = int(num1) + int(num2)
#     print(res)
# else:
#     print("""num1 and num2 must be integer""")


""" isdigit() === isnumeric() ===> return True if the string consists only from digits"""
""" examine string case """
name = 'ahmed'
print(name.isupper())  # True --> string consists only from upper cases char
print(name.islower())
print(name.istitle())    # retrun True --> each char from each word


""" validate strings consists only from alphas [a-z]"""
# message = input("please enter message: ")
# # print(message.isdigit())
# print(message.isalpha()) # return True if consists only from alphas [a-z]


""" string consists only from spaces """
# message = input("please enter message: ")  # input always returns with string
# # print(message.isdigit())
# print(message.isspace())

"""  change string // lower/ upper /// title// capitalize  ---> return new string """
fullname = 'noha abdelhady shehab'
print(fullname.upper())
print(fullname.lower())
print(fullname.title())
print(fullname.capitalize())

""" string interpolation"""
fname= 'noha '
midname= 'abdelhady '
lname ='shehab'
# fullname = fname  + midname + midname +lname
fullname = fname  + midname *2 +lname
print(fullname)
print("iti_"*10)

""" strip string """

message = "nn      we love python      nn"
print(len(message))
print(message)
# strip string
# print(message.strip())  # strip spaces from the beginning and the end of the string
# print(message.lstrip())
# print(message.rstrip())

""" strip --> strip certain chars """
print(message.strip("nw "))  # strip n from the beginning and the end of the string
# print(message.lstrip())
# print(message.rstrip())


""" iterate over the string """
"""for """
mymessage = "python is easy sdkjf kdjhsfjk kjsfh"
for char in mymessage:
    print(f"char = {char}")


# replace char by char
"replace space with underscore ? "

# newmsg=mymessage.replace(" ", "_")
# print(newmsg)

newmsg=mymessage.replace(" ", "_", 2)
print(newmsg)



# """ in operator"""
# print("o" in "noha")  # return True if element in the string



"in operator"
print("no" in "noha")


"noha => nh "
































#




























