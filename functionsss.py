""" functions with known number of arguments ===> required"""

# def myfun():  # define function
#     pass
#
# res=myfun()
# print(res)


# def myfun():  # define function
#     return
#
# res=myfun()
# print(res)

# def hello_ghaza():
#     print("--- Hello from Ghazaa")
#
# hello_ghaza()


""" function returns with result"""

# def get_fullname():
#     firstname = input("Enter your first name: ")
#     lastname = input("Enter your last name: ")
#     fullname = f'{firstname} {lastname}'
#     return fullname
#
# myname = get_fullname()
# print(myname)


"""function accepts data and return with result"""

# def sumnum(num1, num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     return res
#
#
# ss = sumnum(202, 22)
# print(ss)
#
# res2 = sumnum('124', '23')
# print(res2)

# def sumnum(num1, num2):
#     if num1.isnumeric() and num2.isnumeric():
#         print(f"num1={num1}, num2={num2}")
#         res = int(num1) + int(num2)
#         return res
#
#
# ss = sumnum(202, 22)
# print(ss)
#
# res2 = sumnum('124', '23')
# print(res2)


" validate functions must be integers"
""" int x """

# def sumnum(num1: int, num2: int):  # for documentation purpose
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     return res
#
#
# ss = sumnum(202, 22)
# print(ss)
#
# res2 = sumnum('124', '23')  # for your info
# print(res2)
#
# res3 = sumnum("ahmed", 10)  # TypeError: can only concatenate str (not "int") to str


""" validate datatype """

# print(type(10)==int)
print(isinstance(10, str))

# def sumnum(num1: int, num2: int):  # for documentation purpose
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1={num1}, num2={num2}")
#         res = num1 + num2
#         return res
#
#
# ss = sumnum(202, 22)
# print(ss)
#
# res2 = sumnum('124', '23')  # for your info
# print(res2)
#
# res3 = sumnum("ahmed", 10)  #

""" --------------------- -------------------------- """
""" function with optional arguments ---> default argument """

# def sumnum(num1=4, num2:int=10):  # for documentation purpose
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     return res
#
#
# ss = sumnum(202, 22)
# print(ss)
#
# ss = sumnum(202)
# print(ss)
#
# print(sumnum())
""" functions with unknown number of arguments  --"""


# print(434)
# print()
# print("ahmed", "noha", "iti", 2323, sep='||')

# def candidate(*stds):  # function allow zero or more argument ---> *
#     print(stds)  # tuple
#
#
# candidate()
# candidate("Ahmed")  #
# candidate("Ali", "ahmed", 3, 23)


""" """

def introduce_your_self(**info):  # keyword ---> argument
    print(info)

introduce_your_self(name='noha', work='iti')
introduce_your_self(fname='ahmed')
introduce_your_self()

""" 3-> [[1], [2,4],[3,6,9]]"""

" 5 , 3  --> [3,4,5,6,7]"

"""
'abdulrahman'
    abdu
    lr
    ahm
    an
"""

"""
["apple", "banana", "cherry"]
apple 
::: noha
-----
==? 7 tries 
-pp--

-pp-e


"""