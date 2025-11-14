# TODO: Add __str__ method
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        # Return "Title by Author (X pages)"
        return f"{self.title} by {self.author} ({self.pages} pages)"
# Test:
book = Book("Python 101", "Jane Doe", 350)
print(book) # Should print: Python 101 by Jane Doe (350 pages)

# TODO: Add __len__ and __bool__
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def __str__(self):
        # Return "Playlist: name (X songs)"
        return f"Playlist: {self.name} ({len(self.songs)} songs)"
    def __len__(self):
        # Return number of songs
        return len(self.songs)
    def __bool__(self):
        # True if has songs
        return bool(self.songs)
# Test with empty and full playlist
playlist1 = Playlist("My Favorites")
added_song = "Song A"
playlist1.add_song(added_song)
print(playlist1)  # Should print: Playlist: My Favorites (1 songs)
print(bool(playlist1))  # Should print: True
# TODO: Matrix with both __str__ and __repr__
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0]*cols for _ in range(rows)]
    def __str__(self):
        # Return nice grid format
        # 0 0 0
        # 0 0 0
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.data)
    def __repr__(self):
        # Return "Matrix(rows, cols)"
        return f"Matrix({self.rows}, {self.cols})"
    def __len__(self):
        # Return total elements (rows * cols)
        return self.rows * self.cols
# Test:
matrix = Matrix(2, 3)
print(matrix)  # Should print a 2x3 grid of zeros
print(repr(matrix))  # Should print: Matrix(2, 3)
print(len(matrix))   # Should print: 6

# TODO: Compare game scores
class Score:
    def __init__(self, points):
        self.points = points
    def __str__(self):
        return f"Score: {self.points}"
    def __eq__(self, other):
        # Return True if points equal
        return self.points == other.points
    def __lt__(self, other):
        # Return True if less points
        return self.points < other.points
# Test:
# s1 = Score(100)
# s2 = Score(85)
# print(s1 > s2) # Should be True
s1 = Score(100)
s2 = Score(85)
print(s1 > s2) # Should be True
def __lt__(self, other):
    # Return True if less points
    return self.points < other.points


# TODO: Compare dates
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.month:02d}/{self.day:02d}/{self.year}"
    def __eq__(self, other):
        # Check if same date
        return (self.year == other.year and
                self.month == other.month and
                self.day == other.day)
    def __lt__(self, other):
        # Check if earlier date
        # Compare year, then month, then day
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day
# Test with different dates
d1 = Date(2020, 5, 15)
d2 = Date(2020, 6, 15)
print(d1 < d2) # Should be True