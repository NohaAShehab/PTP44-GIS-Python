""" while loop """
## while ?  ==> no of iterations

"""
    while condition:
        do something 
"""

# num = 0
# while num < 5:
#     print(f"---num = {num}")
#     num +=1

""" name ---> all alphas  """
# while True:
#     name = input("Enter your name: ")
#     if name.isalpha():
#         break #--> control loop /// limit loop behaviour
#
# print(f"name= {name}")

##
# for i in range(10):
#     print(i)

# for i in range(10):
#     if i==5:
#         break
#     print(f"-- i = {i}")
#
# for i in range(10):  # 0->9
#     if i==5:
#         continue   # skip to the next iteration
#     print(f"-- i = {i}")
#     print("---------------------")


####### break , continue

""" atm password ? """

# for i in range(3):
#     password = input("Enter your password: ")
#     if password =='abc':
#         print("--- login in successfully")
#         break
#     print("---- invalid password please try again")
#
# # we must block account if loop reached its end
# # print(i)
# if i==2:
#     print("----- Account blocked ---------")




# for i in range(3):
#     password = input("Enter your password: ")
#     if password =='abc':
#         print("--- login in successfully")
#         break
#     print("---- invalid password please try again")
#
# # we must block account if loop reached its end
# # print(i)
# if i==2 and password !='abc':
#     print("----- Account blocked ---------")

for i in range(3):
    password = input("Enter your password: ")
    if password =='abc':
        print("--- login in successfully")
        break
    print("---- invalid password please try again")
else:
    """ this block will be executed if the loop wasn't broken"""
    print("--- account has been blocked ---")


# continue with loops
name = input("Enter your name: ")
if name:
    pass


# for i in range(10):
#     if i==5:
#         continue
#     print(f"i = {i}")

for i in range(10):
    if i==5:
        pass
    print(f"i = {i}")



















