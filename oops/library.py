class library:
    def __init__(self):
        self.nobooks=0
        self.books =[]

    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"the lirary has {self.nobooks} books, and the books are")
        for book in self.books:
            print(book)



l1 = library()

l1.addbook("Harry potter 1")
l1.addbook("Harry potter 2")
l1.addbook("Harry potter 3")
l1.addbook("Harry potter 4")

l1.showinfo()