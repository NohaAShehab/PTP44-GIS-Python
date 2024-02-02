import  json


# read data

# fileobj = open("test.json", "r")
#
# # data = fileobj.read()  # string
# # print(data)
#
# data = json.load(fileobj)
# print(data)


## write data
# mydata = {"id":1, 'name': "noha"}
# fileobj = open("test.json", "a")
# fileobj.write(str(mydata))
#
# fileobj.close()
#
# mydata = {"id":1, 'name': "noha"}
# fileobj = open("test.json", "a")
# json.dump(mydata, fileobj)
# fileobj.close()

## read all data
## save data to the list
## write all data again


""" read all data """
fileobj = open('test.json', 'r')
data = json.load(fileobj)  # list
print(data)
fileobj.close()


mydata = {"id":1, 'name': "noha"}
data.append(mydata)


fileobj = open('test.json', 'w')
json.dump(data, fileobj, indent=2)
fileobj.close()