import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    genre = input("Enter the genre of the book:")
    read = input("Have you read this book? (yes/no): ").lower() == 'yes'
    
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added to the library Successfully.")

def remove_book(library):
    title = input ("Enter the title of the book to remove from the Library:")
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed from the library successfully.")
    else:
        print(f"Book '{title}' not found in the library.")
        
def search_library(library):
    search_by = input("Search by (title/author): ").lower()
    search_term = input("Enter a search term (title, author): ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]
    
    if results:
        print("Search Results:")
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print(f"No books found matching '{search_term}' under the {search_by} term.")

def display_all_books(library):
    if library:
        print("All Books in the Library:")
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print("No books in the library.")

def display_statustics(library):
    total_books = len(library)
    read_books = len([book for book in library if book ['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
            print("\nWelcome to the Library Management System")
            print("====================================")
            print("Library Menu:")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Library")
            print("4. Display All Books")
            print("5. Display Statistics")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                add_book(library)
            elif choice == '2':
                remove_book(library)
            elif choice == '3':
                search_library(library)
            elif choice == '4':
                display_all_books(library)
            elif choice == '5':
                display_statustics(library)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()