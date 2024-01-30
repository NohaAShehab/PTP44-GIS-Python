info = ["Noha", 31, "GIS", "Smart"]  # unlabeled data

"""representation data --> more descriptive """
"""
    set : remove duplication 
"""
myd = {}
d = dict()

""" data represented inform of key value pair 
    dict ---> doesn't allow key duplication 
    --> used in representing labeled data 
"""
""" python 3.7 --> dict ordered in memory """
myinfo = {
    "name":"noha", 'age':31, 'gender':'female',
    'work':"iti" , "track":"GIS", "name":"Noha Shehab"
}
print(myinfo)

""" get len """
print(len(myinfo))

""" dict is mutable data ---> key value pair  --> key : string """

# myinfo = {
#     "name":"noha", 'age':31, 'gender':'female',
#     'work':"iti" , "track":"GIS", "name":"Noha Shehab",
#     10:"iti"
# }

""" access elements  --> key """
print(myinfo['name'])
# myinfo['age'] = 32  # update the value of existing key
myinfo['city'] = 'Cairo'  # add new key:value pair

""" check if element exists in dict """
print(myinfo)
print(31 in myinfo)  # in operator --> search if value exists in keys

""" get dict keys, values , value pairs  """
keys = myinfo.keys()  # dict_keys
print(keys)
keys_list = list(keys)


vals = myinfo.values()  # dict_values
print(vals)
vals_list = list(vals)

print(31 in myinfo.values())

"for loop "

for abbass in myinfo:
    # print(f"key = {abbass}")
    print(f"key = {abbass}, value= {myinfo[abbass]}")

""" dict items """

d_items = myinfo.items()  # dict_items
print(d_items)

itemss = list(d_items)
print(itemss)

for k , v in myinfo.items():
    print(f"{k}, {v}")

'remove element from dict '

popped_value=myinfo.pop("age")
print(popped_value)
#
# "del key value pair"
#
# del myinfo["age"]
#
# """ clear dictionary """
# # myinfo.clear() # remove all the key value pairs

nums = [3445,46,65,57]  # multiply each element*2
# newl= []
# for num in nums :
#     newl.append(num*10)
#
# print(nums)
# print(newl)

newl = map(lambda x:x*10, nums)
print(newl)  # map object
newl = list(newl)
print(newl)

#######################################
print(myinfo)
workinfo = {"work":"Information Technology", "Start_Date":2019, "courses":["python","mongo"]}

print(workinfo)

myinfo.update(workinfo)
print(myinfo)