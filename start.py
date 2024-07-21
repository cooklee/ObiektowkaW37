from menu import Option, Menu
from modele import Author, Book

authors = [Author("Adam", "Mickiewicz"), Author("Andrzej", "Sapkowski")]
books = []


def add_author():
    first_name = input("podaj imie\n")
    last_name = input("podaj nazwisko\n")
    authors.append(Author(first_name, last_name))
    print(f"dodaleś autora {first_name} {last_name}")


def add_book():
    title = input("podaj tytuł \n")
    year = input("podaj tytuł \n")
    year = int(year)
    show_author()
    id_autora = int(input("wybierz autora"))
    for author in authors:
        if author.id == id_autora:
            break
    books.append(Book(title, year, author))


def show_author():
    for author in authors:
        print(author)


def show_book():
    for book in books:
        print(book)


def update_author():
    id = input("podaj id autora\n")
    author = None
    for a in authors:
        if a.id == int(id):
            author = a
            break
    if author is None:
        print("Nie ma authora o podanym id")
    else:
        first_name = input("podaj imie\n")
        last_name = input("podaj nazwisko\n")
        author.first_name = first_name
        author.last_name = last_name


def obsluga_authora():
    m = Menu(
        Option('Wyświetl wszystkich Autorów', show_author),
        Option('Dodaj Autora', add_author),
        Option('modyfikuj autora', update_author),
        intend = "    "
    )
    m.start()


def obsluga_ksiazki():
    m = Menu(
        Option('Wyświetl wszystkich ksiazek', show_book),
        Option('Dodaj ksiazke', add_book),
        Option('modyfikuj ksiazke', update_author),
        intend="    "
    )
    m.start()


m = Menu(
    Option('Ksiazki', obsluga_ksiazki),
    Option('Autorzy', obsluga_authora))
m.start()
