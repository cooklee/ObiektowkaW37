class A:
    opis = "Ala ma kota"

    def wypisz_ladnie_opis(self):
        print("_________________________________________")
        print(f"|           {self.opis}                |")
        print("_________________________________________")

    @classmethod
    def wypisz(cls):
        print(cls.opis)

    @staticmethod
    def cos_tam_cos_tam():
        print(B.opis)


class B(A):
    opis = "pies pogryzł ale"

    def wypisz_ladnie_opis(self):
        super().wypisz_ladnie_opis()
        print("koniec")

a =A()
a.wypisz()
b = B()
b.wypisz()
a.cos_tam_cos_tam()
b.cos_tam_cos_tam()

