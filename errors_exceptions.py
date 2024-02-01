
#
# name = "noha"
# name = int(name)   # runtime error


""" syntax errors  must be handled """
# if:
#
# print("-------")




# def sumnum(num1 , num2):
#     res = num1 * num2
#     return res
#
# print(sumnum(2,2))
#
# print(sumnum(45,6))  # logical error ---> Developer
#
# #### developer (unit testing === FYI
#


# num = input("please enter a number ")
# num = int(num)
# print(f"-- num= {num}")

# print("------------------------------------")

#
# try:
#     num = input("please enter a number ")
#     num = int(num)
#     print(f"-- num= {num}")
# except:
#     print("----- problem happened ")


# print("------------------------------------")


"""
    try(){}
    catch Exception as e {
        // exception handling
    }

"""
#
# try:
#     num = input("please enter a number ")
#     num = int(num)
#
# except:
#     print("----- incorrect input number is set to be zero  ")
#     num = 0
#
# print(f"-- num= {num}")
#
# res = num * 1.5




# while True:
#     try:
#         num = int(input("please enter a number: "))
#         break
#     except:
#         print("------ please enter number again ")
#
# print(num)

# def askforInt(message="please enter a number"):  # define function
#     while True:
#         try:
#             num = int(input(message))
#             return num
#         except :
#             print("----- please enter a valid number ")



# def askforInt(message="please enter a number"):  # define function
#     try:
#         num = int(input(message))
#         return num
#     except :
#         print("----- please enter a valid number ")
#         return askforInt(message)



# try:
#     num = int(input("please enter a number: "))
#     res = 10/num
# except Exception as abbasss :  # get exception info
#     print(f"---- error happened {abbasss}  ")


# try:
#     num = int(input("please enter a number: "))
#     res = 10/num
# except ZeroDivisionError as ze  :  # get exception info
#     print(f"---- error happened {ze}  ")
#     res = 0
#
# except ValueError as ve :
#     print(f"---- problem : {ve}")
#     num = 1
#     res = 10 / num
#
#
# print(f"---- result == {res}")



########################
# try:
#     num = int(input("please enter a number: "))
#     res = 10/num
# except Exception as e:
#     exit()


#######################################################


# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print("---- problem happend ")
#
# print(num)  # only need if the process executed successfully


# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print("---- problem happend ")
# else:
#     print(num)  # only need if the process executed successfully

""" finally """


# try:
#     num = int(input("Enter a number: "))
# except Exception as e:
#     print("---- problem happend ")
# else:
#     print(num)  # only need if the process executed successfully
# finally:
#     print("------ this block will be executed  always -----")

# print("#################################")




# def askforNumber(message):
#     try:
#         num = float(input(message))
#     except Exception as e:
#         print(f"---- {e} ")
#         return  0
#     else:
#         return  num
#
#     print("--- asking for number processd finished ")
#
#
#
# print(askforNumber("please enter your salary"))
#
#




def askforNumber(message):
    try:
        num = float(input(message))
    except  :
        print(f"---- ")
        return  0
    else:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return  num
    finally:
        # finally execution ---> precedes return execution
        print("--- asking for number processd finished ")



print(askforNumber("please enter your salary"))
















