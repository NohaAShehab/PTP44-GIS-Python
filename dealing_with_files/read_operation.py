

""" read  --->
    open file for reading only if the file exists
 """

try:
    filobject = open("names.txt", "r")  # return textIOWrapper
except Exception as  e:
    print(f"----{e}")
else:
    print(filobject)
    file_data = filobject.read()  # read content
    print(file_data, type(file_data))
    """ move fileobject to specific byte """
    filobject.seek(0)

    "line by line"
    data = filobject.readlines()
    print(data, type(data))

    # lines = []
    # for l in filobject:
    #     lines.append(l)
    #
    # print(lines)
    filobject.close()