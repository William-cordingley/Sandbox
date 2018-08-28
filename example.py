books = "title,autor,1,r"
book = books.split(",")
print(book)
print(book[0])
print(len(book))

string = "new book"
books.insert(0, string)
print(books)