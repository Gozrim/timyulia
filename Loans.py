from modules import Loans

def avaliable_books(loans_list, book_list,book_id):
    loan_num = []
    book_num = []
    same = []
    for item in loans_list:
        temp_list = item.split(",")
        loan_num.append(temp_list[1]) 
    print(loan_num)
    for element in book_list:
           new_list = element.split(",")
           book_num.append(new_list[0])
    print(book_num)
    for item in book_num:
        if item in loan_num:
            same.append(item)
    print(same)

def loan_book(loans_list,book_list):
    avaliable_books = book_list
    print("Here are all the avaliable books ")
    for item in avaliable_books:
        print(item)
    not_avaliable = []
    new_loan = Loans(custid=input("Enter your ID : "),bookid=input("Enter book ID : "),
                     loandate=input("Enter today's date : "),returndate=input("Enter return date : "))
    loans_list.append(new_loan.__str__())
    for item in avaliable_books:
        temp_list = item.split(",")
        id = temp_list[0]
        if new_loan.bookid == id:
            index = avaliable_books.index(item)
            avaliable_books.pop(index)
            not_avaliable.append(item.__str__())
            for books in avaliable_books:
                print(books)
    print(not_avaliable)
    print(loans_list)

    return not_avaliable, loans_list

