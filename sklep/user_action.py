from sklep.model import User


def show_user():
    users = User.get_users()
    for user in users:
        print(user)

def add_user():
    first_name = input("podaj imie\n")
    last_name = input("podaj nazwisko\n")
    username = input("podaj nazwe użytkownika")
    password = input("podaj hasło")
    u = User(first_name, last_name, username, password)
    u.save()
    print("udało sie utworzyć użytkownika")

def update_user():
    pass