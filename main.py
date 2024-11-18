from classes import Library

National_library = Library()

National_library.add_book(354, 1920, "Pushkin", 12.5)
National_library.add_book(500, 1870, "Tolstoy", -5.0) 
National_library.add_book(500, 1870, "Tolstoy", 15.0)
National_library.add_book(-100, 1869, "Dostoevsky", 14.0)
National_library.add_book(320, 1869, "Dostoevsky", 14.0)  
National_library.add_book(320, -1869, "Gogol", 14.0)  

for book in National_library.list_of_books:
    print(book)

books_by_pushkin = National_library.find_books_by_author("Pushkin")
print("Books by Pushkin:", books_by_pushkin)

books_by_authors = National_library.find_books_by_author("Pushkin", "Tolstoy")
print("Books by Pushkin and Tolstoy:", books_by_authors)

if len(National_library.list_of_books) >= 2:
    book1 = National_library.list_of_books[0]
    book2 = National_library.list_of_books[1]

    print(book1.compare_price(book2))
    print(book2.compare_price(book1))
    print(book1.compare_price(book1))
