""" json ---> data representation style -->
in saving data to file
"""
import  json

# def save_book_to_file(book_data):
#     try:
#         fileobject = open("books.txt", 'a')
#     except Exception as e:
#         print("Error while saving book --> try again ")
#         return False
#     else:
#         book_values = list(book_data.values())
#         # bookdata= ':'.join(book_values)
#         bookdata = f"{book_values[0]}:{book_values[1]}:{book_values[2]}\n"
#         fileobject.write(bookdata)
#         fileobject.close()
#         return True

## get all books
def read_all_books():
    try:
        fileobject = open("books.json", 'r')
    except Exception as e:
        print("Error while saving book --> try again ")
        return False
    else:
        try:
            data = json.load(fileobject)
        except Exception as e:
            return  []
        else:
            return data



def save_book_to_file(book_data):
    old_data = read_all_books()
    try:
        fileobject = open("books.json", 'w')
    except Exception as e:
        print("Error while saving book --> try again ")
        return False
    else:
        old_data.append(book_data)
        json.dump(old_data, fileobject, indent=2)
        return True

