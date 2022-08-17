from Books import add_book, remove_book, find_book
from Customers import add_customer, find_customer, remove_customer
from Loans import loan_book
from main import last_id, book_list, customer_list,loans_list
command = None
print("Welcome to the library, how may i assist?(chose the relevant number")

while command != "4":
    command = input("1.Books 2.Customers 3.Loans 4.Exit menu")

    if command == "1":
        action = input(f"Chose an action\n"
              f"1.Add a new book\n"
              f"2.Remove a book\n"
              f"3.Display all books\n"
              f"4.Find a book")
        if action == "1":
           add_book(int(last_id), book_list)
        if action == "2":
            remove_book(book_list)
        if action == "3":
            print(book_list)
        if action == "4":
            find_book(book_list)

    if command == "2":
        action = input(f"Chose an action\n"
              f"1.Add a new customer\n"
              f"2.Display customers\n"
              f"3.Find customer\n"
              f"4.Remove customer")
        if action == "1":
            customer_list = add_customer(customer_list)
        if action == "2":
            print(customer_list)
        if action == "3":
            find_customer(customer_list)
        if action == "4":
            remove_customer(customer_list)

    if command == "3":
        action = input(f"Chose an action\n"
              f"1.Loan a book\n"
              f"2.Display all loans\n"
              f"3.Return a book\n"
              f"4.Display late loans")
        if action == "1":
            loan_book(loans_list,book_list,customer_list, loand_books)
        if action == "2":
            print(loans_list)
