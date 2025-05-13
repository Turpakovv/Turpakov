class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.name} by {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Pages must be an integer")
        if pages <= 0:
            raise ValueError("Pages must be a positive number")
        self._pages = pages

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, (int, float)):
            raise TypeError("Duration must be a number")
        if duration <= 0:
            raise ValueError("Duration must be a positive number")
        self._duration = duration

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, {self.duration:.2f} hours"

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"