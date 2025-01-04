class Library:
    def __init__(self):
        self.books = ["Gaurab", "Saamar", "Amul"]
        self.no_of_books = len(self.books)

    def add_book(self):
        new_book = input("Enter the name of the book you want to add: ").strip()
        if new_book:
            self.books.append(new_book)
            self.no_of_books = len(self.books)
            print(f"Book added successfully! Total books: {self.no_of_books}")
        else:
            print("Invalid book name. Please try again.")

    def verify_book_count(self):
        if self.no_of_books == len(self.books):
            print("Book count is accurate.")
        else:
            print("Book count mismatch. Please check.")

    def display_books(self):
        print("\nCurrent list of books:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")


# Main Loop
library = Library()
while True:
    print("\nLibrary Menu:")
    print("1. Add a Book")
    print("2. Verify Book Count")
    print("3. Display Books")
    print("4. Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.verify_book_count()
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        print("Exiting the Library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
