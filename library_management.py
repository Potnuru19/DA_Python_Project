

from datetime import date, timedelta


# LIBRARY MANAGEMENT SYSTEM

class Library:

    # Constructor
    def __init__(self):
        self.books = {}
        self.members = {}
        self.issues = []

        self.filename = "library_data.txt"

        self.load_data()

    # 1. SAVE DATA
    def save_data(self):

        with open(self.filename, "w") as file:

            # Save Books
            for isbn, book in self.books.items():

                file.write(
                    "B|" + isbn + "|" +
                    book["title"] + "|" +
                    book["author"] + "|" +
                    book["category"] + "|" +
                    str(book["total"]) + "|" +
                    str(book["available"]) + "\n"
                )

            # Save Members
            for member_id, member in self.members.items():

                file.write(
                    "M|" + member_id + "|" +
                    member["name"] + "|" +
                    member["phone"] + "\n"
                )

            # Save Issue Records
            for issue in self.issues:

                return_date = issue["return_date"]

                if return_date is None:
                    return_date = "-"

                file.write(
                    "I|" +
                    str(issue["issue_id"]) + "|" +
                    issue["isbn"] + "|" +
                    issue["member_id"] + "|" +
                    issue["issue_date"] + "|" +
                    issue["due_date"] + "|" +
                    return_date + "|" +
                    str(issue["fine"]) + "\n"
                )

    # 2. LOAD DATA
    def load_data(self):

        try:

            with open(self.filename, "r") as file:

                for line in file:

                    data = line.strip().split("|")

                    try:

                        if data[0] == "B" and len(data) == 7:

                            self.books[data[1]] = {
                                "title": data[2],
                                "author": data[3],
                                "category": data[4],
                                "total": int(data[5]),
                                "available": int(data[6])
                            }

                        elif data[0] == "M" and len(data) == 4:

                            self.members[data[1]] = {
                                "name": data[2],
                                "phone": data[3]
                            }

                        elif data[0] == "I" and len(data) == 8:

                            self.issues.append({
                                "issue_id": int(data[1]),
                                "isbn": data[2],
                                "member_id": data[3],
                                "issue_date": data[4],
                                "due_date": data[5],
                                "return_date": None if data[6] == "-" else data[6],
                                "fine": int(data[7])
                            })

                    except ValueError:
                        print("Invalid record skipped.")

        except FileNotFoundError:

            print("Library data file not found.")
            print("A new file will be created.")

    # 3. BOOK REGISTRATION
    def add_book(self):

        print("\n--- Book Registration ---")

        isbn = input("Enter Book ISBN: ")

        if isbn in self.books:
            print("Book already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        category = input("Enter Book Category: ")

        try:

            quantity = int(input("Enter Number of Copies: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:

            print("Enter a valid number!")
            return

        self.books[isbn] = {
            "title": title,
            "author": author,
            "category": category,
            "total": quantity,
            "available": quantity
        }

        self.save_data()

        print("Book registered successfully!")

    # 4. DISPLAY BOOK CATEGORIES
    def show_categories(self):

        print("\n--- Book Categories ---")

        categories = []

        for book in self.books.values():

            category = book["category"]

            if category not in categories:
                categories.append(category)

        if categories:

            for category in categories:
                print(category)

        else:
            print("No categories available.")

    # 5. MEMBER REGISTRATION
    def register_member(self):

        print("\n--- Member Registration ---")

        member_id = input("Enter Member ID: ")

        if member_id in self.members:
            print("Member already registered!")
            return

        name = input("Enter Member Name: ")
        phone = input("Enter Phone Number: ")

        self.members[member_id] = {
            "name": name,
            "phone": phone
        }

        self.save_data()

        print("Member registered successfully!")

    # 6. BOOK SEARCH
    def search_book(self):

        print("\n--- Book Search ---")

        keyword = input("Enter Book Title or Author: ").lower()

        found = False

        for isbn, book in self.books.items():

            if (keyword in book["title"].lower()
                    or keyword in book["author"].lower()):

                print("\nISBN:", isbn)
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Category:", book["category"])
                print("Available:", book["available"])

                found = True

        if not found:
            print("Book not found!")

    # 7. DISPLAY ALL BOOKS
    def display_books(self):

        print("\n--- All Library Books ---")

        if not self.books:
            print("No books available.")
            return

        for isbn, book in self.books.items():

            print("\nISBN:", isbn)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            print("Total Copies:", book["total"])
            print("Available Copies:", book["available"])

    # 8. BOOK ISSUE
    def issue_book(self):

        print("\n--- Book Issue ---")

        isbn = input("Enter Book ISBN: ")
        member_id = input("Enter Member ID: ")

        if isbn not in self.books:
            print("Book not found!")
            return

        if member_id not in self.members:
            print("Member not registered!")
            return

        if self.books[isbn]["available"] <= 0:
            print("Book not available!")
            return

        issue_date = date.today()

        due_date = issue_date + timedelta(days=14)

        issue_id = len(self.issues) + 1

        issue = {
            "issue_id": issue_id,
            "isbn": isbn,
            "member_id": member_id,
            "issue_date": str(issue_date),
            "due_date": str(due_date),
            "return_date": None,
            "fine": 0
        }

        self.issues.append(issue)

        self.books[isbn]["available"] -= 1

        self.save_data()

        print("Book issued successfully!")
        print("Issue ID:", issue_id)
        print("Issue Date:", issue_date)
        print("Due Date:", due_date)

    # 9. BOOK RETURN
    def return_book(self):

        print("\n--- Book Return ---")

        try:

            issue_id = int(input("Enter Issue ID: "))

        except ValueError:

            print("Invalid Issue ID!")
            return

        for issue in self.issues:

            if (issue["issue_id"] == issue_id
                    and issue["return_date"] is None):

                return_date = date.today()

                due_date = date.fromisoformat(issue["due_date"])

                late_days = max(
                    0, (return_date - due_date).days
                )

                fine = late_days * 5

                issue["return_date"] = str(return_date)
                issue["fine"] = fine

                isbn = issue["isbn"]

                self.books[isbn]["available"] += 1

                self.save_data()

                print("Book returned successfully!")
                print("Return Date:", return_date)
                print("Late Days:", late_days)
                print("Fine Amount: Rs.", fine)

                return

        print("Active issue record not found!")

    # 10. AVAILABILITY TRACKING
    def check_availability(self):

        print("\n--- Book Availability ---")

        if not self.books:
            print("No books available.")
            return

        for isbn, book in self.books.items():

            print(
                book["title"],
                "| Available:", book["available"],
                "| Total:", book["total"]
            )

    # 11. DUE DATE CALCULATION
    def show_due_dates(self):

        print("\n--- Pending Book Returns ---")

        found = False

        for issue in self.issues:

            if issue["return_date"] is None:

                member = self.members[issue["member_id"]]

                book = self.books[issue["isbn"]]

                print("\nIssue ID:", issue["issue_id"])
                print("Member:", member["name"])
                print("Book:", book["title"])
                print("Due Date:", issue["due_date"])

                found = True

        if not found:
            print("No pending returns.")

    # 12. FINE CALCULATION
    def calculate_fines(self):

        print("\n--- Fine Calculation ---")

        total_fine = 0

        for issue in self.issues:

            if issue["return_date"] is None:

                due_date = date.fromisoformat(issue["due_date"])

                late_days = max(
                    0, (date.today() - due_date).days
                )

                fine = late_days * 5

            else:

                fine = issue["fine"]

            print(
                "Issue ID:", issue["issue_id"],
                "| Fine: Rs.", fine
            )

            total_fine += fine

        print("Total Fine: Rs.", total_fine)

    # 13. BORROWING SUMMARY
    def borrowing_summary(self):

        print("\n--- Borrowing Summary ---")

        active = 0
        returned = 0

        for issue in self.issues:

            if issue["return_date"] is None:
                active += 1

            else:
                returned += 1

        print("Total Books:", len(self.books))
        print("Total Members:", len(self.members))
        print("Total Borrowing Records:", len(self.issues))
        print("Currently Issued:", active)
        print("Books Returned:", returned)


# MAIN PROGRAM

library = Library()

while True:

    print("\n==============================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Book Registration")
    print("2. Book Categories")
    print("3. Member Registration")
    print("4. Book Search")
    print("5. Display All Books")
    print("6. Book Issue")
    print("7. Book Return")
    print("8. Availability Tracking")
    print("9. Due Date Calculation")
    print("10. Fine Calculation")
    print("11. Borrowing Summary")
    print("12. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.show_categories()

    elif choice == "3":
        library.register_member()

    elif choice == "4":
        library.search_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.issue_book()

    elif choice == "7":
        library.return_book()

    elif choice == "8":
        library.check_availability()

    elif choice == "9":
        library.show_due_dates()

    elif choice == "10":
        library.calculate_fines()

    elif choice == "11":
        library.borrowing_summary()

    elif choice == "12":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please select between 1 and 12.")
