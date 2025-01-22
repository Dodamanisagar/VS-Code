class Book:
    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies Available: {self.copies_available}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.copies_available > 0:
                    book.copies_available -= 1
                    print(f"Book '{book.title}' has been issued.")
                    return book
                else:
                    print(f"Book '{book.title}' is currently out of stock.")
                    return None
        print(f"No book found with ISBN {isbn}.")
        return None

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.copies_available += 1
                print(f"Book '{book.title}' has been returned.")
                return True
        print(f"No book found with ISBN {isbn}.")
        return False

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        book = library.issue_book(isbn)
        if book:
            self.borrowed_books.append(book)

    def return_book(self, library, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                library.return_book(isbn)
                self.borrowed_books.remove(book)
                return
        print(f"You have not borrowed a book with ISBN {isbn}.")

    def __str__(self):
        borrowed = ", ".join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"User: {self.name}, Borrowed Books: {borrowed}"


# Example Usage
if __name__ == "__main__":
    # Create Library
    library = Library()

    # Add Books
    book1 = Book("The Alchemist", "Paulo Coelho", "12345", 3)
    book2 = Book("1984", "George Orwell", "67890", 5)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "11111", 2)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display Books
    library.display_books()

    # Create User
    user = User("Sagar")

    # User Borrows a Book
    print("\n--- Borrowing Books ---")
    user.borrow_book(library, "12345")
    user.borrow_book(library, "11111")

    # Display Library Books
    print("\n--- Library Books After Borrowing ---")
    library.display_books()

    # Display User Details
    print("\n--- User Details ---")
    print(user)

    # User Returns a Book
    print("\n--- Returning Books ---")
    user.return_book(library, "12345")

    # Display Library Books After Returning
    print("\n--- Library Books After Returning ---")
    library.display_books()

    # Display User Details After Returning
    print("\n--- User Details After Returning ---")
    print(user)
