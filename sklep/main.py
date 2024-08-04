from menu import Menu, Option
from sklep.user_action import show_user, add_user, update_user


# def obsluga_authora():
#     m = Menu(
#         Option('Wyświetl wszystkich Autorów', show_author),
#         Option('Dodaj Autora', add_author),
#         Option('modyfikuj autora', update_author),
#         intend = "    "
#     )
#     m.start()


def obsluga_usera():
    m = Menu(
        Option('Wyświetl wszystkich uzytkownikow', show_user),
        Option('rejestracja', add_user),
        Option('modyfikuj dane', update_user),
        intend="    "
    )
    m.start()


m = Menu(
    Option('Użytkownicy', obsluga_usera),
    Option('Autorzy', lambda x:1))
m.start()
