class A:
    opis = "Ala ma kota"

    def wypisz_ladnie_opis(self):
        print("_________________________________________")
        print(f"|           {self.opis}                |")
        print("_________________________________________")


class B(A):
    opis = "pies pogryzł ale"

    def wypisz_ladnie_opis(self):
        super().wypisz_ladnie_opis()
        print("koniec")


b = B()
b.wypisz_ladnie_opis()