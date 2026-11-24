class Library:
    books_available = 100    # Total books in library

    books_available =0 
    def __init__(self,books):
        self.books = books
        Library.books_available += books
    
    @classmethod
    def lend_books(cls,books):
        cls.books_available -= books
    @classmethod
    def return_books(cls,books):
        cls.books_available += books

    


    # TODO: Implement class methods to manage book lending
    # TODO: Implement return_books method to increase the number of books available

library = Library(100)


# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
