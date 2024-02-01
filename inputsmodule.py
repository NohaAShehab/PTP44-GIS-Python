
""" ---> python module --> any .py file -->
import module or part of it in another module

"""

"""
in each .py file --> python module --> you have a main ---> entry point-- -> 
"entry 000 > is called when you run file "

"""
def askforInt(message="please enter a number"):  # define function
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("----- please enter a valid number ")



# age = askforInt("please enter your age:  ")
# print(f"age = {age}, {type(age)}")
#
name = 'noha'   # define variable
#
grade = 100

if __name__ == '__main__':

    course=  'python'
    print("------- inputsmodule  is called ")
    age = askforInt("please enter your age:  ")
    print(f"age = {age}, {type(age)}")


if __name__:
    course = 'python'
    print("------- inputsmodule  is called ")
    age = askforInt("please enter your age:  ")
    print(f"age = {age}, {type(age)}")


