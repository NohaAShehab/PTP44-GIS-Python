
""" list is the most basic datatype in python"""
""" loosely dynamic typed lang."""
"""1- to define a list"""

ll= []
myl = list()

""" list can hold different data from different datatypes """
myl = ["Ahmed", 324, 24.23, True, None, "iti",["python", "mongo"], "iti"]
print(myl)

"""get len of list ?"""
print(len(myl))

""" count element occurence in list"""
print(myl.count("iti"))

""" get element index in list  """
print(myl.index("iti"))

""" access element using index"""
print(myl[5])
print(myl[6][1])
""" list is mutable datatype """
myl[3] = 'updated'
# myl[100] = 'new element ' #IndexError: list assignment index out of range

""" add element to the list --->  """
myl.append("new element ") # append --> add element to the end of the list
myl.insert(3, "inserted element")

""" remove element from the list """
# popped_elememnt=myl.pop()  # pop the last element
# print(myl)
# print(popped_elememnt)


popped_elememnt=myl.pop(3)  # pop the last element
print(myl)
print(popped_elememnt)


""" remove element --> without index """
myl.remove("iti")  # first occurrence in the list
print(myl)


""" concat the list """
l1 = ["python", "gis", "agile"]
l3 = ["ArchGIS", "c#", 'databases']
courses = l1 + l3   # return new list
# print(courses)

""" extend a list ?  """
l1.extend(l3)
print(l1)

""" sort the list  ---> comparison ---> you can only compare items from the same type """
# sortedlist=courses.sort()  # sort data ascending  in the same variable
# print(sortedlist)
# print(courses)
# courses =sorted(courses)
courses.sort(reverse=True)
print(courses)
# myl.sort()  #TypeError: '<' not supported between instances of 'int' and 'str'

"reverse a list "
print(myl)
myl.reverse()
print(myl)

""" loop over the list ? """
for item in myl:
    print(f"item= {item}")

""" item , index """
index = 0
for item in myl:
    print(f"item= {item}, {index}")
    index +=1
# print(myl)

""" enumatrate fun"""
list_index = enumerate(myl)  # generate index for list
print(list_index) # enumerate object  # iterable

# for abbass , test in list_index:
#     print(f"{abbass}: {test}")

""" cast enumerate to list """
mydata = list(list_index)
print(mydata)

""" cast string to list """
print(list("noha"))  # each char --> as element in the list
""" split string to a list """
msg= "we love python"
words = msg.split(" ")  #
print(words)
"""join list elements into one string --> list consists of strings  """
newmsg = '_'.join(words)  # join accept iterable
print(newmsg)


print("iti" in myl)

print('$'.join("noha"))


print(min(courses))











