from sklep.model import User_




def show_user():
    users = User_.all()
    for user in users:
        print(user)

def add_user():
    first_name = input("podaj imie\n")
    last_name = input("podaj nazwisko\n")
    username = input("podaj nazwe użytkownika")
    password = input("podaj hasło")
    u = User_(first_name=first_name, last_name=last_name, username=username, password=password)
    u.save()
    print("udało sie utworzyć użytkownika")

def update_user(user):
    try:
        user = user[0]
        first_name = input("podaj imie\n")
        last_name = input("podaj nazwisko\n")
        username = input("podaj nazwe użytkownika\n")
        password = input("podaj hasło\n")
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.password = password
        user.save()
    except IndexError:
        print("musisz sie zalogować ")

def login(user):
    username = input("podaj nazwe użytkownika\n")
    password = input("podaj hasło\n")
    u = User_.login(username, password)
    if u is not None:
        user.append(u)
    else:
        print("logowanie nie poprawne")

