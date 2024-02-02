from custom_inputs import  askforInt, generateID, ask_for_string
from filehandler import  save_book_to_file, read_all_books
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
    books = read_all_books()
    for book in books:
        print(book)


## edit , delete  --> delete first
