# this is a comment

name = 'Ahmed'
Name = 'Noha'

print(name)

# print = 'iti'

# print('nohaaaaaaaaaaaaaaaaaaaaaaaaa')

# if = 'iti'

# track = 'GIS'

# if () {
# print("fff")
# }


# if name == 'Ahmed':
#     print("welcome to iti ")

## rules --> script file

track = 'GIS'

# if track == 'GIS':
#     print('Hello GIS')
#     print("Python is easy")


# if(track=='gis') {}

# if track=='GIS':
#     pass
#
# print("-------------------")


#### this is a comment

message = 'we love python'

info = "we are GIS students"

# both are strings


bio = ("My name is Noha "
       "I works at iti "
       "I lives in Cairo ")

print(bio)

## single. double qouted string don't preserver new lines

# bio = ("My name is Noha\n"   # explicity I need line her
#        "I works at iti "
#        "I lives in Cairo ")
#
# print(bio)


## to create string that preserve new line --> use triple
bio = '''My name is Noha 
I works at iti
I lives in Cairo'''

print(bio)

### use the string as a comment


""" this string can be used as a
 comment 
if name:
    print("Hello") 
else:
    print("bye")
"""

## define variables  ==> each variable datatype
#
# name = 'ahmed'  #str
# track ="GIS"
# age = 23
# pi = 3.14
# happy = True
# problems = None
#
# # check datatype
# print(type(name))
# print(type(age))
# print(type(happy))
# print(type(problems))
# name = 100 #int


"******************** type conversion ***********************"
# year= 2024   # int
# print(type(year))
# year = str(year)
# print(type(year))


age = "31"  # string  --> numeric string
age = int(age)  # type casting  --> cast string to int
print(type(age))

# message = "Hello world"   # str --> '' 49byte
# message = int(message)  # int --> 4 bytes   #ValueError
# print(message, type(message))

#####################################
"******************* arthimatic operators *******************"

num1 = 10
num2 = 3

print(num1 / num2)  # 3.3
print(num1 // num2)  # 3 --> division without fraction
print(num1 % num2)
print(num1 ** num2)  # POWER

num1 += 5  # num1 = num1 +5
# num1 = num1 +5
print(num1)

# comparison == -> compare value and data type


# bool True == 1


""" logical operators """
# print(1 and 10)  # 10 00> represent true
#
print("noha" and "python" and "ahmed")  # ahmed --> represent True  =--->

name = 'noha'  # this string represent True
if name:
    print("hii")
else:
    print("bye")

print(bool(name))

message = "            "  # this not empty string --> space is char
if message:
    print("found")
else:
    print("---Not found---")


print("" and "Ahmed" and "python")   # >?   "" --> represent false