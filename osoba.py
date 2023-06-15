from konto import Konto

class Osoba:
    def __init__(self, imie, nazwisko, nr_konta, saldo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.konto = Konto(nr_konta, saldo)

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko

    def getKonto(self):
        return self.konto