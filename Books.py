from modules import Book

def add_book(counter, book_list):
    counter += 1
    with open("book_rank.txt", "a") as file:
        new_book = str(Book(counter,str(input("Enter the title of the book: ")),
                        str(input("Enter author: ")), str(input("Enter publisher")),
                       str(input("Enter genre: ")),  int(input("Enter frequency"))))
        book_list.append(new_book)
        return print("The Book has been added")

def remove_book(book_list):
    id_input = str(input("Type the id of the book you wish to remove: "))
    for i in book_list:
        temp_list = i.split(",")
        if id_input in temp_list[0]: # if you have an object and not string you dont need this
                                     # you just do:
                                     # for book in book_list
                                     #      if id_input in book.id:
            index = book_list.index(i)
            book_list.pop(index)
            return print("The book has been removed")

# you need 2 spaces here
def find_book(book_list):
    # why not find book by name? please add its easier
    id_input = str(input("Enter the id of the book you wish to find: "))
    for i in book_list:
        # see my comment above for the remove book. please fix in all functions
        temp_list = i.split(",")
        if id_input in temp_list[0]:
            print(f"Book's name: {temp_list[1]}\n"
                  f"Author: {temp_list[2]}\n"
                  f"Publisher: {temp_list[3]}\n"
                  f"Genre: {temp_list[4]}\n")
            break












