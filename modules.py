class Book:
    def __init__(self, id, title, author, publisher, genre, frequency):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.frequency = frequency

    def __str__(self):
        return f"{self.id},{self.title},{self.author},{self.publisher},{self.genre}, {self.frequency}"

class Customers:
    def __init__(self, id, name, city, age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    def __str__(self):
        return f"{self.id}, {self.name}, {self.city}, {self.age}"

class Loans:
    def __init__(self, custid, bookid, loandate, returndate):
        self.custid = custid
        self.bookid = bookid
        self.loandate = loandate
        self.returndate = returndate

    def __str__(self):
        return f"{self.custid}, {self.bookid}, {self.loandate}, {self.returndate}"