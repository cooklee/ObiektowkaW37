class User:

    def __init__(self, imie, nazwisko, rok_urodzenia, amount=0):
        self.first_name = imie
        self.last_name = nazwisko
        self.year = rok_urodzenia
        self.amount = amount

    def __str__(self):
        return (f"{self.first_name} {self.last_name} {self.amount}")



def dodaj_usera(user_name):
    imie = input("podaj imie")
    nazwisko = input("podaj nazwisko")
    stan = 0
    rok_urodzenia = int(input("podaj rok urodzenia"))
    u = User(imie=imie, nazwisko=nazwisko, rok_urodzenia=rok_urodzenia)
    users[user_name] = u




users = {}

while True:
    x = input("""
    1 - dodaj uzytkownika
    2 - wpłać pln na konto
    """)
    if x == "1":
        un = input('podaj nazwe uzytkownika')
        dodaj_usera(un)
        print(users)
    elif x == "2":
        un = input("podaj nazwe uzytkownika")
        kw = float(input("podaj kwote"))
        users[un]+=kw
    elif x == "3":
        for u in users.values():
            print(u)
    elif x == '4':
        break
