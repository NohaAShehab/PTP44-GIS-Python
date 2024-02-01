

""" write  --->
    open file for writing if the file doen't exist python will try to create

    ===> if file exists > python will open the file for writing starting from
    the beginning of the file (erase old content )
 """

try:
    # because of permission
    filobject = open("mycv.txt", "w")  # return textIOWrapper
except Exception as  e:
    print(f"----{e}")
else:
    print(filobject)
    filobject.write("My name is Noha\n")
    filobject.write("I lives in Mansoura\n")
    filobject.write("I works at ITI")

    filobject.writelines(["Ahmed\n", "Abbass\n","fawzy\n", "Radwa\n"])
    filobject.close()