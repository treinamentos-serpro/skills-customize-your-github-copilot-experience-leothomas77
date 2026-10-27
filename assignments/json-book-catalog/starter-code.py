import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("books.json")

INITIAL_BOOKS = [
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "publication_year": 1937,
    },
    {
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "publication_year": 1962,
    },
]


def save_books(books):
    """Save the list of books to DATA_FILE."""
    # TODO: Open DATA_FILE and write books as formatted JSON.
    pass


def load_books():
    """Return the list of books stored in DATA_FILE."""
    # TODO: Open DATA_FILE and return the decoded JSON data.
    pass


def display_books(books):
    for book in books:
        print(
            f"{book['title']} by {book['author']} "
            f"({book['publication_year']})"
        )


def main():
    # TODO: Load saved books, or copy INITIAL_BOOKS if DATA_FILE is missing.
    books = []

    display_books(books)

    # TODO: Ask for a book's title, author, and publication year.
    # Add the new book to books and save the updated catalog.


if __name__ == "__main__":
    main()