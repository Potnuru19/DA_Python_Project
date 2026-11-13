# Library Management System

## Project Overview

The **Library Management System** is a beginner-friendly, menu-driven Python project that helps manage books, library members, and book borrowing records. It supports book registration, member registration, searching, issuing and returning books, availability tracking, due-date calculation, fine calculation, and borrowing summaries.

The project stores its data in a text file (`library_data.txt`) so that book, member, and issue records can be loaded again when the program is run.

## Technologies Used

- **Programming Language:** Python
- **Modules:** `datetime` (`date` and `timedelta`)
- **Data Storage:** Text file (`library_data.txt`)
- **Concepts:** Classes and objects, dictionaries, lists, loops, conditional statements, functions, file handling, and exception handling

## Features

1. **Book Registration** – Add a book using its ISBN, title, author, category, and number of copies. Duplicate ISBNs are rejected, and the copy quantity must be greater than zero.
2. **Book Categories** – Display the distinct categories available in the registered books.
3. **Member Registration** – Register a member with a member ID, name, and phone number. Duplicate member IDs are rejected.
4. **Book Search** – Search for books by title or author.
5. **Display All Books** – Display the details and copy counts of all registered books.
6. **Book Issue** – Issue an available book to a registered member. The issue date is the current date and the due date is 14 days later.
7. **Book Return** – Return a book using its issue ID. The system updates the available copy count and calculates a late fine.
8. **Availability Tracking** – Display available and total copies for each book.
9. **Due Date Calculation** – Display active issue records and their due dates.
10. **Fine Calculation** – Calculate fines for active overdue issues and display recorded fines for returned books.
11. **Borrowing Summary** – Display totals for books, members, borrowing records, currently issued books, and returned books.
12. **Exit** – Close the menu-driven program.

## Fine Calculation

The project uses the following rule:

- The borrowing period is **14 days** from the issue date.
- The fine is **₹5 per late day**.
- No fine is charged when a book is returned on or before its due date.

## Data Storage

The program uses `library_data.txt` in the current working directory.

Records are saved as pipe-separated lines with a record-type prefix:

- `B` – Book record
- `M` – Member record
- `I` – Issue record

When the program starts, it attempts to load the saved records. If the file does not exist, it displays a message that a new file will be created. The program saves data after book registration, member registration, book issue, and book return.

## How to Run

1. Make sure Python 3 is installed.
2. Save the project code as `library_management.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

   ```bash
   python library_management.py
   ```

5. Choose an option from the displayed menu by entering its number.
6. Select **12** to exit.

## Main Menu

| Option | Operation |
|---|---|
| 1 | Book Registration |
| 2 | Book Categories |
| 3 | Member Registration |
| 4 | Book Search |
| 5 | Display All Books |
| 6 | Book Issue |
| 7 | Book Return |
| 8 | Availability Tracking |
| 9 | Due Date Calculation |
| 10 | Fine Calculation |
| 11 | Borrowing Summary |
| 12 | Exit |

## Project Structure

```text
Library-Management-System/
├── library_management.py
└── library_data.txt   # Created/used by the program to store records
```

## Exception Handling

The program handles some common input and file-related errors:

- Displays a message if `library_data.txt` is not found when loading data.
- Skips records with invalid integer values while loading.
- Checks that the number of book copies is a valid positive integer.
- Handles an invalid issue ID entered during book return.

## Conclusion

This project demonstrates how Python can be used to build a simple library management application. It brings together basic programming concepts, file handling, date calculations, and exception handling to manage library books, members, and borrowing records.

## Note

This README describes the features implemented in the supplied Python program. The program uses a local text file for storage; it does not use a database or a graphical user interface.
