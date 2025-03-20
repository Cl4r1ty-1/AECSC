class Library:
    def __init__(self, name: str, location :str, books_data: dict):
        self.name = name
        self.location = location
        self.books_data = books_data

    def add_book(self, title: str, author: str, genre: str, quantity: str):
        self.books_data[title] = {"author": author, "genre": genre, "quantity": quantity}
    
    def remove_book(self, title: str):
        self.books_data.pop(title)

    def search_book(self, title: str):
        if title in self.books_data.keys():
            return f"{title}: {self.books_data[title]}"
        else:
            return "Book not found!"
    
    def borrow_book(self, title: str):
        if self.books_data[title]["quantity"] > 0:
            self.books_data[title]["quantity"] -= 1
        else:
            return "Book not avaliable"

    def return_book(self, title: str):
        self.books_data[title]["quantity"] += 1

    def display_books(self):
        pass