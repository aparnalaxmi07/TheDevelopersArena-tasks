# ---------------------------------------------------------
# WEEK 5 PROJECT: LIBRARY MANAGEMENT SYSTEM (OOP)
# Developer's Arena Internship
# ---------------------------------------------------------

# Book class
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Issued"
        return f"{self.book_id} | {self.title} by {self.author} | {status}"


# Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.issued_books = []

    def __str__(self):
        return f"{self.member_id} | {self.name} | Books issued: {len(self.issued_books)}"


# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add a book
    def add_book(self, title, author, book_id):
        book = Book(title, author, book_id)
        self.books.append(book)
        print("✅ Book added successfully!")

    # Register a member
    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print("✅ Member registered successfully!")

    # Display all books
    def display_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    # Display all members
    def display_members(self):
        print("\n--- Library Members ---")
        if not self.members:
            print("No members found.")
            return
        for member in self.members:
            print(member)

    # Issue book to a member
    def issue_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book is None:
            print("❌ Book not found!")
            return
        if member is None:
            print("❌ Member not found!")
            return
        if not book.is_available:
            print("❌ Book is already issued!")
            return

        book.is_available = False
        member.issued_books.append(book)
        print(f"📘 '{book.title}' issued to {member.name}")

    # Return a book
    def return_book(self, book_id, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)

        if member is None:
            print("❌ Member not found!")
            return

        for book in member.issued_books:
            if book.book_id == book_id:
                book.is_available = True
                member.issued_books.remove(book)
                print(f"📗 '{book.title}' returned successfully!")
                return

        print("❌ Book not issued to this member.")


# ---------------- MAIN PROGRAM --------------------

def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            book_id = input("Book ID: ")
            library.add_book(title, author, book_id)

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            library.add_member(name, member_id)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            book_id = input("Book ID to issue: ")
            member_id = input("Member ID: ")
            library.issue_book(book_id, member_id)

        elif choice == "6":
            book_id = input("Book ID to return: ")
            member_id = input("Member ID: ")
            library.return_book(book_id, member_id)

        elif choice == "7":
            print("📚 Exiting Library System...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
