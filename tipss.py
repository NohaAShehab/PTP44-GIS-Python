""" FYI """

""" allow only some properties to be added to the object """
class Employee(object):
    __slots__ = ['name', 'salary', 'email', "__dict__"]
    # define allowed properties
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        self.__dict__ ={
            "name":self.name,
            "email":self.email,
            "salary":self.salary
        }

    def __str__(self):
        ## must return string
        return str(self.name)


emp = Employee("John", "<EMAIL>", 893)
# emp.city ='San Francisco'
#
print(emp.__dict__)
print(emp)