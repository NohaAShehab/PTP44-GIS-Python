""" overloading

2 function in the same class with
same name -> but different in
no _of properties , datatypes of properties

public int myfunc(int num1 , int num2){
}

public int myfunc(int num1 ){

}
public str myfunc(str num1){

}
"""

# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#
#     def printEmployee(self):
#         print(self.name)
#
#     """ overloading cannot be done explicitly in python """
#     def printEmployee(self, message):
#         print(self.name, message)
#
#
# emp = Employee("noha")
# emp.printEmployee()


""" """


class Employee:
    def __init__(self, name):
        self.name = name

    """ overloading cannot be done explicitly in python """
    def printEmployee(self, message=''):
        print(self.name, message)


emp = Employee("noha")
emp.printEmployee()
emp.printEmployee("hi")


### FYI ==> implement in overloading in python
### external lib --> install --> overlaod
# https://pypi.org/project/overloading/





