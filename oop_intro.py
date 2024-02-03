# info related to employee ? ==
# info= ["ahmed", 1000]
# emp1 ={"name":"ahmed", "salary":1000 }
# emp2= {"empname":"mohamed", "salary":3209}   # dict --> object from class dict
# emp1.values()
# def printEmployee(emp):
#     print(f"name = {emp['name']}, salary = {emp['salary']}")


# printEmployee(emp1)
# printEmployee(emp2)

"""create uniform structure for our customized datatype  --> class
---> template definition of an object structure
"""

""" your first class """
print(list)

# class Employee:
#     pass
#
#
# print(Employee)
# """ My first object """
# emp = Employee()
# print(emp)  # print object address
#
# """ loosely dynamically typed lang."""
# emp.name = 'Ahmed'
# print(emp.name)
#
#
# emp2 = Employee()
# emp2.empname = "Ali"
#
# print(type(emp2))


""" control object creation in the class --> constructor  """

# class Employee:
#     """ constructor --> function called while initializing new object/ instance """
#     def __init__(self):
#         print(f"self = {self}")
#         print("--- object is being created ---")
#
#
# emp = Employee()
# print(f"emp = {emp}")


# class Employee:
#     """ constructor --> function called while initializing new object/ instance """
#     def __init__(self):
#         """ define object property ? """
#         self.name = 'ahmed'
#         self.salary = 823748935
#
#
# emp = Employee()
# emp.name = 'noha'
# print(emp.name)
# emp.email = 'noha@gamil.com'
#
# emp2 = Employee()


""" """

# class Employee:
#     """ constructor --> function called while initializing new object/ instance """
#     """ customize object creation """
#
#     def __init__(self, name, salary):
#         """ define object property ? """
#         """ name, salary ---> instance variables """
#         self.name = name
#         self.salary = salary
#
#
# emp = Employee("noha", 37824)
#
# emp2 = Employee("ali", 38723)


'check this scenario '

# class Employee:
#     """ constructor --> function called while initializing new object/ instance """
#     """ customize object creation """
#
#     def __init__(name, salary):  # first parameter in the __init__ function self
#         print(name, salary)
#         print("--- object is being created =---")
#
#
# # emp = Employee("Ahmed", 76575)
# emp = Employee("Ahmed")
"""  """
# class Employee:
#     """ constructor --> function called while initializing new object/ instance """
#     """ customize object creation """
#
#     def __init__(self, name, salary):  # first parameter in the __init__ function self
#         # self represent object address in memory
#         self.name = name
#         self.salary = salary
#
#
# # emp = Employee("Ahmed", 76575)
# emp = Employee("Ahmed", 8573)
# print(emp.name)
# emp.name = '72ywrsdjb'

""" instance methods """

# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def printEmpInfo(self, message = 'Hi'):   # self ==> refer to the caller object/instance
#         print(f"{message}:Employee name: {self.name}, Employee salary: {self.salary}")
#
#
# emp = Employee("Ahmed", 8573)
# emp.printEmpInfo()
#
# emp.printEmpInfo("Bye")


""" ===> count number of instances  taken from the class """

# class Employee:
#
#     def __init__(self, name='noha', salary=1000):
#         self.name=  name
#         self.salary= salary
#         self.count = 1  # related to instance / object
#
#
# emp  = Employee()
#
# emp2 = Employee()
#
# print(emp2.count)

""" class variables  ---> variable represent class property not instance property"""

# class Employee:
#     count = 0  # class variable 00> represent class property
#     salary_transfer_date = '1st of month'
#
#     def __init__(self, name='noha', salary=1000):
#         self.name = name
#         self.salary = salary
#         # Employee.count +=1
#         print(self.__class__)
#         self.__class__.count +=1
#
#
# print(Employee.count)
# emp = Employee()
# print(Employee.count)
# emp2 = Employee()
# print(Employee.count)
#
# """ class variablle --> shared property between all instances/ objects """
# Employee.salary_transfer_date = '10st of month'
""" class method """

# class Employee:
#     count = 0  # class variable 00> represent class property
#     salary_transfer_date = '1st of month'
#
#     def __init__(self, name='noha', salary=1000):
#         self.name = name
#         self.salary = salary
#         Employee.count += 1
#
#     # function --> class method  --> not depends on any instance
#     @classmethod
#     def get_emp_count(cls):  # first parameter -> cls --> represent current class
#         # print(cls)
#         print(f"total Employee count: {cls.count}")
#         return cls.count
#
#
# print(Employee.get_emp_count())
#
# emp = Employee()
# emp2 = Employee()
# print(Employee.get_emp_count())
# print(Employee.count)
""" class method """

# class Employee:
#     count = 0  # class variable 00> represent class property
#     salary_transfer_date = '1st of month'
#
#     def __init__(self, name='noha', salary=1000):
#         self.name = name
#         self.salary = salary
#         Employee.count += 1
#
#     # function --> class method  --> not depends on any instance
#     @classmethod
#     def get_emp_count(cls):  # first parameter -> cls --> represent current class
#         # print(cls)
#         print(f"total Employee count: {cls.count}")
#         return cls.count
#
#     """ function ---> return new object from the class"""
#     """ class method - -> object factory """
#
#     @classmethod
#     def add_object(cls, object1, object2):
#         if isinstance(object1, cls) and isinstance(object2, cls):
#             name = f"{object1.name} {object2.name}"
#             salary = object1.salary + object2.salary
#             # create new object
#             # return Employee(name, salary)
#             return cls(name, salary)
#
#
# print(Employee.get_emp_count())
#
# emp = Employee()
# emp2 = Employee()
# print(Employee.get_emp_count())
# print(Employee.count)
# emp3 = Employee.add_object(emp, emp2)
#
#
# """ save created objects in a file - >> instance
#  get all instances created from the class==> from a file ===> class method
#  """

"""  check this scenario """


class Employee:
    count = 0  # class variable 00> represent class property
    salary_transfer_date = '1st of month'

    def __init__(self, name='noha', salary=1000):
        self.name = name
        self.salary = salary
        Employee.count += 1

    # function --> class method  --> not depends on any instance
    @classmethod
    def get_emp_count(cls):  # first parameter -> cls --> represent current class
        # print(cls)
        print(f"total Employee count: {cls.count}")
        return cls.count

    "used with helper functions"

    @staticmethod
    def cal_net_sal(salary):
        return salary * .8


emp = Employee("noha", 874238)
emp2 = Employee("ali", 876386)

""" helper function """
# def cal_net_sal(salary):
#     return salary*.8
#
#
# print(cal_net_sal(emp.salary))
#
# print(cal_net_sal(623754))


print(Employee.cal_net_sal(85765675))
