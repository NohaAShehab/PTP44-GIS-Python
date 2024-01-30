#
# """ sequence  is the most basic datatype in python"""
# """ loosely dynamic typed lang."""
"""1- to define a tuple"""
#
ll= ()
myl = tuple()
#
""" tuple can hold different data from different datatypes """
myt = ("Ahmed", 324, 24.23, True, None, "iti",["python", "mongo"], "iti", ("iti", "abc",34))
print(myt)
#
"""get len of tuple ?"""
print(len(myt))
#
""" count element occurence in tuple"""
print(myt.count("iti"))
#
""" get element index in tuple  """
print(myt.index("iti"))
#
""" access element using index"""
print(myt[5])
print(myt[6][1])
""" tuple is immutable datatype  ==> once created cannot be changed"""
# myt[3] = 'updated' #tuple' object does not support item assignmen
#




""" concat the tuple """
t1 = ("python", "gis", "agile")
t3 = ("ArchGIS", "c#", 'databases')
courses = t1 + t3   # return new tuple
print(courses)
#

#


#
""" loop over the tuple ? """
for item in myt:
    print(f"item= {item}")
#

#
""" enumatrate fun"""
tuple_index = enumerate(myt)  # generate index for tuple
print(tuple_index) # enumerate object  # iterable

# for abbass , test in tuple_index:
#     print(f"{abbass}: {test}")

""" cast enumerate to list """
mydata = list(tuple_index)
print(mydata)
#
""" cast string to tuple """
print(tuple("noha"))  # each char --> as element in the tuple

""" cast list to tuple and vicevera """
# tt = ("python", "gis", "agile")
# tt = list(tt)
# print(tt)

#
print("iti" in myt)
#
# print('$'.join("noha"))
#
#
print(min(courses))
#
""" tuple of one item """
mytt = ("python",)
print(mytt,type(mytt))
#
