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



def save_all_books(books:list):
    try:
        fileobject = open("books.json", 'w')
    except Exception as e:
        print("Error while saving book --> try again ")
        return False
    else:
        json.dump(books, fileobject, indent=2)
        return True



def save_book_to_file(book_data):
    old_data = read_all_books()
    old_data.append(book_data)
    saved=save_all_books(old_data)
    return saved
    # try:
    #     fileobject = open("books.json", 'w')
    # except Exception as e:
    #     print("Error while saving book --> try again ")
    #     return False
    # else:
    #     old_data.append(book_data)
    #     json.dump(old_data, fileobject, indent=2)
    #     return True



def search_book_by_id(book_id):
    all_books = read_all_books()
    for book in all_books:
        if book['id'] == book_id:
            return book
    else:
        return False




def delete_from_file(book):
    all_books = read_all_books()  # list
    print(all_books)
    if all_books:
        all_books.remove(book)
        print(all_books)
        deleted=save_all_books(all_books)
        return deleted
        # write all books after