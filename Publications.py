class Publications:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"This publications is called {self.name}")


class Book(Publications):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_info(self):
        print(f"This book is called {self.name} by {self.author} with {self.page_count} pages")

class Magazine(Publications):
    def __init__(self, name, Editor):
        super().__init__(name)
        self.name = name
        self.editor = Editor
    def print_info(self):
        print(f"This magazine is called {self.name} and the editor is {self.editor}")

book1 = Book("The art of Disguise", "Clark Kent", 320)
book2 = Book("Running on Time", "Barry Allen", 100)
mag1 = Magazine("Daily Buggle", "J. Jonah Jameson")
mag2 = Magazine("Daily Planet", "Perry White")

book1.print_info()
book2.print_info()
mag1.print_info()
mag2.print_info()