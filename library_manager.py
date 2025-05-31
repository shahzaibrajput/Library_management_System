import json
import os
import streamlit as st

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book_ui(library):
    st.subheader("Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.text_input("Publication Year")
        genre = st.text_input("Genre")
        read = st.checkbox("Have you read this book?")
        submitted = st.form_submit_button("Add Book")
        if submitted:
            if title and author and year and genre:
                new_book = {
                    'title': title,
                    'author': author,
                    'year': year,
                    'genre': genre,
                    'read': read
                }
                library.append(new_book)
                save_library(library)
                st.success(f"Book '{title}' added successfully!")
            else:
                st.error("Please fill all fields.")

def remove_book_ui(library):
    st.subheader("Remove a Book")
    titles = [book['title'] for book in library]
    if titles:
        title_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            new_library = [book for book in library if book['title'] != title_to_remove]
            save_library(new_library)
            st.success(f"Book '{title_to_remove}' removed successfully!")
            st.experimental_rerun()
    else:
        st.info("No books to remove.")

def search_library_ui(library):
    st.subheader("Search Library")
    search_by = st.selectbox("Search by", ["title", "author", "genre"])
    search_term = st.text_input(f"Enter {search_by}")
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book[search_by].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
        else:
            st.warning(f"No books found matching '{search_term}' in {search_by}.")

def display_library_books_ui(library):
    st.subheader("Library Books")
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        st.info("No books in the library.")

def display_statistics_ui(library):
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Books read:** {read_books}")
    st.write(f"**Percentage read:** {percentage_read:.2f}%")

def main():
    st.title("📚 Library Manager System")
    library = load_library()
    menu = ["Add Book", "Remove Book", "Search Library", "Display Library Books", "Display Statistics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        add_book_ui(library)
    elif choice == "Remove Book":
        remove_book_ui(library)
    elif choice == "Search Library":
        search_library_ui(library)
    elif choice == "Display Library Books":
        display_library_books_ui(library)
    elif choice == "Display Statistics":
        display_statistics_ui(library)

    st.markdown("---")
    st.markdown("<center><b>Developed by Shahzaib Rajput</b></center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()