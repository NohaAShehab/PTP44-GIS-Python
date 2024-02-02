from custom_inputs import  askforInt, generateID, ask_for_string
from filehandler import  (save_book_to_file, read_all_books,
                          search_book_by_id, delete_from_file)

from tabulate import tabulate
def create_book():
    title = ask_for_string("please enter book title ")
    no_of_pages = askforInt("please enter number of pages ")
    id = generateID()

    book_data = {
        "id": id,
        "title": title,
        "no_of_pages": no_of_pages
    }  # dict
    ## save data to the file
    saved = save_book_to_file(book_data)
    if saved:
        print("print book saved successfully")



def display_books():
    books = read_all_books()  # list of dicts
    headers = {"id":"book_id", "title":"book_title", "no_of_pages":"Number of pages"}
    print(tabulate(books, headers,tablefmt="rounded_grid"))
    # for book in books:
    #     print(book)



## edit , delete  --> delete first
def delete_book():
    id = askforInt("please enter the id of the you want to delete: ")
    ## search using this id if book exists  -->
    found = search_book_by_id(id)
    if found:
        print(found)
        delete_from_file(found)
    # if exists --> remove it file
    else:
        print("--- book not found ")


