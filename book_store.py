from book_crud import  create_book, display_books, delete_book

# menu --> insert book , update , delete , list all
# json files ==>
## builtin modules in python






def mainmenu():
    while True:
        choice = input("please enter your choice: ")
        if choice == "c":
            create_book()
        elif choice=='u':
            pass
        elif choice=='l':
            display_books()
        elif choice =='d':
            delete_book()
        elif choice=='e':
            exit()
        else:
            print("-------------- please enter valid choice")



if __name__ == "__main__":
    mainmenu()
