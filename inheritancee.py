"""

inheritance ---> Parent and child
"""

# class Person:
#     pass
#
#
# class Employee(Person):
#     pass
#
# """ inheritance  --> is a relationship """
# emp = Employee()
# print(isinstance(emp , Person))

""" """


# class Person:
#     def __init__(self, name):
#         print("--- I am Person ")
#         self.name = name
#
#
# class Employee(Person):
#     pass
#
#
# emp = Employee("noha")


""" 2nd case """
# class Person:
#     def __init__(self, name):
#         print("--- I am Person ")
#         self.name = name
#
#
#
#
#
# class Employee(Person):
#     def __init__(self, salary):
#         self.salary = salary
#
#
# emp = Employee("noha")  # call Employee constructor
#
#


""" call parent constructor """
# class Person:
#     def __init__(self, name):
#         print("Parent constructor called: I am Person ")
#         self.name = name
#
#
#
#
#
# class Employee(Person):
#     def __init__(self, name, salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#
#
#
# emp = Employee("noha",48937)  # call Employee constructor
#







""" methods """


# class Person:
#     def __init__(self, name):
#         print("Parent constructor called: I am Person ")
#         self.name = name
#
#     def displayPerson(self):
#         print(f"name= {self.name.upper()}")
#
#
#
# class Employee(Person):
#     def __init__(self, name, salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#
#
# emp = Employee("noha", 48937)  # call Employee constructor
# emp.displayPerson() # call parent methods

""" check this scenario """

""" 
    2 functions with the same name
    in 2 classes have inheritance relation
    ---> function in the child class 
    override the function in the parent class
"""
# class Person:
#     def __init__(self, name):
#         print("Parent constructor called: I am Person ")
#         self.name = name
#
#     def displayPerson(self):
#         print(f"name= {self.name.upper()}")
#
#
#
# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary


    # overriding
#     def displayPerson(self):
#         # call parent function
#         super().displayPerson()
#         print(f"salary = {self.salary}")
#
#
# emp = Employee("noha", 48937)  # call Employee constructor
# emp.displayPerson() # call parent methods


"""======================================================================"""

# class GIS:  # inherits from class object
#     pass
#
# g = GIS()
#
# print(isinstance(g, object))


# class GIS(object):  # inherits from class object
#     def __init__(self, name):
#         self.name= name
#
# g = GIS("ndsfhjk")
#
# print(isinstance(g, object))
#

""" python supports multiple inheritance  or not ?"""
""" yes """

# class Employee:
#     pass
#
# class Engineer:
#     pass
#
# class Developer(Employee, Engineer):
#     pass
#
# dev = Developer()
# print(isinstance(dev, Employee))
# print(isinstance(dev, Engineer))

""" """

# class Employee:
#     def __init__(self):
#         print("Employee")
#
# class Engineer:
#     def __init__(self):
#         self.eng = True
#         print("Engineer")
#
# class Developer(Employee, Engineer):
#     pass
#
# dev = Developer()
# print(isinstance(dev, Employee))
# print(isinstance(dev, Engineer))










class MyException(Exception):
    pass


raise  MyException("kshjkdfh")



""" multi-level single inheritance"""

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass



"""
    'define variable  --> decided datatype of reference 
    "--> statistically  tightly lang."
    Employee emp  = Engineer()
    reference child ===> child object 
    reference parent  ---> child object 
    reference child --> parent object

"""














