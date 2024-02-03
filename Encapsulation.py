""" encapsulation  ====>"""

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name =name
#         self.email = email
#         self.salary = salary
#
#
#
# emp = Employee("ahmed", 'ahmed@gmaill.com', 8923749)
# print(emp.email)
"""
access modifiers 
    public : --> property/ function: accessed anywhere using instance/ object
    protected: --> property/ function: accessed only in the class or the child classes 
    private : --> property/ function: accessed only in the class 

" ---------------- no access modifiers in python --------------------" 
    --> workaround --> use variable_name --> represent access level
    start with a-z ----> public
    start with _  ---> protected 
    start with __ ---> private 

setters getters --> limit accessibility ---> apply logic 

"""

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name =name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private


# emp = Employee("ahmed", 'ahmed@gmaill.com', 8923749)
# print(emp.name)
# """ python developer is mature decent developer """
# print(emp._email)   # ethically don't do that
# emp._email = 'updated'  # ethically don't do that
#
# """ what about private ?"""
# # print(emp.__salary)
# # print(emp._Employee__salary)  # ethically don't do this
#
#


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name =name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float) :
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
#
# emp = Employee("John", "<EMAIL>", 78264)
# # emp.setSalary("iti")
# emp.setSalary(726482364)


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name =name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float) :
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
#     def getSalary(self):
#         return  self.__salary * 0.8
#
# emp = Employee("John", "<EMAIL>", 78264)
# emp.setSalary("iti")
# # emp.setSalary(726482364)
#
# # print("iti"> 10)
""" check this """


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         self.__salary = salary  # private
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
#     def getSalary(self):
#         return self.__salary * 0.8
#
#     @property  # allow writing logic applied to property ---> infor of function
#     def salary(self):
#         return self.__salary*.8
#
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
# emp = Employee("John", "<EMAIL>", 78264)
# print(emp.getSalary())
# print(emp.salary)
#
# # emp.salary ="iti"
# emp.salary = 89237


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name  # public
#         self._email = email  # protected
#         # self.__salary = salary  # private
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
#     @property  # allow writing logic applied to property ---> infor of function
#     def salary(self):
#         return self.__salary*.8
#
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             """raising errors"""
#             raise ValueError('salary must be numeric value')
#
# emp = Employee("John", "<EMAIL>", "iti")

# print(emp.salary)


class Employee:
    makeerros = False

    def __init__(self, name, email, salary):
        self.name = name  # public
        self._email = email  # protected
        # self.__salary = salary  # private
        self.salary = salary

    @property  # allow writing logic applied to property ---> infor of function
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            """raising errors"""
            raise ValueError('salary must be numeric value')

#
emp = Employee("John", "<EMAIL>", 784)
#
# emp.salary = 100  # call property setter
# print("---------------------------------------")
#
# """ display object properties in form of dict """
#
print(emp.__dict__)
