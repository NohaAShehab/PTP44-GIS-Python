import  random

def askforInt(message):
    try:
        num = int(input(message))
    except Exception as e:
        print("--- please enter an integer")
        return askforInt(message)
    else:
        return num




""" module in python ---> random """
##
def generateID():
    id  = random.randint(1,4728974)
    return id


def ask_for_string(message):
    while True:
        inputstring = input(message)
        if inputstring and not inputstring.isspace():
            inputstring=inputstring.strip()
            return inputstring
        else:
            print("--- please enter valid string ")












if __name__ == "__main__":
    print(generateID())
    print(ask_for_string("please enter title "))