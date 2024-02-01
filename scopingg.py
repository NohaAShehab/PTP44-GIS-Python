""" variable defined inside the function --> variable with local scope
 this variable is accessed only inside the function
 """
# def sumnum(num1 , num2):
#     name = 'ahmed'    # local scope
#     res = num1 +  num2
#     return  res
#
#
# sumnum(23,556)
# print(name)


""" check this scenario"""

# course = 'python'  #
""" variable defined in the python script is a variable with global scope 
can be access anywhere in the script

"""


# def printCourse():
#     print(f"Course = {course}")


# printCourse()


""" ---->> modify global variable ------"""

# coursename= 'python'
# def modifyCourse():
#     coursename = input("please enter course name: ")  # local scope
#     print(f"===> after modify --> course=  {coursename}")
#
#
# modifyCourse()
# print(coursename)


# coursename = 'python'

#
# def modifyCourse():
#     global coursename  # please don't create new local variable 00> use the global one
#     coursename = input("please enter course name: ")
#     print(f"===> after modify --> course=  {coursename}")
#
#
# modifyCourse()
# print(coursename)


""" -----> function inside a function --> """

# def courseInfo():
#     coursename = input("please enter course name ")   # local variable
#     """ you can access local variable anywhere inside the function --> inner function """
#
#     def printCourseUpper():
#         print(f"from inside print --> {coursename}")
#
#     printCourseUpper()
#
#
#     print(f"===> from CourseInfo {coursename}")
#
# courseInfo()


# def courseInfo():
#     coursename = input("please enter course name ")   # local variable
#     """ you can access local variable anywhere inside the function --> inner function """
#     def printCoursename():
#         print(f"from inside print --> {coursename}")
#
#     printCoursename()
#
#
#     print(f"===> from CourseInfo {coursename}")
#
# courseInfo()
# printCoursename()


""" modify local variable from inside inner function """


# def courseInfo():
#     coursename = input("please enter course name ")   # local variable
#     """ you can access local variable anywhere inside the function --> inner function """
#     def printCoursename():
#         print(f"from inside print --> {coursename}")
#
#     printCoursename()
#
#     def modifycourse():
#         coursename = input("please modify course name :")  # new local variable from the modifycourse function
#         print(f"===> from modifycourse {coursename}")  # python with oop
#
#     modifycourse()
#
#
#     print(f"===> from CourseInfo {coursename}")  # python
#
# courseInfo()


""" """


# def courseInfo():
#     coursename = input("please enter course name ")   # local variable
#     """ you can access local variable anywhere inside the function --> inner function """
#     def printCoursename():
#         print(f"from inside print --> {coursename}")
#
#     printCoursename()
#
#     def modifycourse():
#         global  coursename  ######  global ---> out to the global scope
#         coursename = input("please modify course name :")  # new local variable from the modifycourse function
#         print(f"===> from modifycourse {coursename}")  # python with oop
#
#     modifycourse()
#
#
#     print(f"===> from CourseInfo {coursename}")  # python
#
# courseInfo()



def courseInfo():
    coursename = input("please enter course name ")   # local variable
    """ you can access local variable anywhere inside the function --> inner function """
    def printCoursename():
        print(f"from inside print --> {coursename}")

    printCoursename()

    def modifycourse():
        nonlocal coursename  ######  please use the parent variable and don't create new local one
        coursename = input("please modify course name :")
        print(f"===> from modifycourse {coursename}")  # python with oop

    modifycourse()


    print(f"===> from CourseInfo {coursename}")  # python

courseInfo()















