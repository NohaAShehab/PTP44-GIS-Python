

""" append  --->
    open file for appending if the file doen't exist python will try to create

    ===> if file exists > python will open the file for writing starting from
    the end of the file (keep old content )
 """

try:
    # because of permission
    filobject = open("dataaaaaa.txt", "a")  # return textIOWrapper
except Exception as  e:
    print(f"----{e}")
else:
    print(filobject)
    # filobject.write("My name is Noha\n")
    # filobject.write("I lives in Mansoura\n")
    # filobject.write("I works at ITI")
    #
    # filobject.writelines(["Ahmed\n", "Abbass\n","fawzy\n", "Radwa\n"])
    filobject.write("###################\n\n")
    filobject.close()