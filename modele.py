class Author:
    next_id = 1

    def __init__(self, first_name, last_name):
        self.id = Author.next_id
        Author.next_id += 1
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"


class Book:
    next_id = 1

    def __init__(self, title, year, author=None):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f"{self.id} {self.title} {self.year} {self.author.first_name} {self.author.last_name}"
# print(Author.next_id)
# x = [Author("Sławek", "Bo"),
#      Author("Gosia", "Pe"),
#      Author("Kasia", "De")]
# print(Author.next_id)
# for author in x:
#     print(author)