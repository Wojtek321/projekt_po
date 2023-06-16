from karta import KartaKredytowa, KartaBankomatowa, KartaDebetowa
from Exceptions import NiepoprawnyRodzajException

class Konto:
    def __init__(self, nr_konta, saldo):
        self.nr_konta = nr_konta
        self.saldo = saldo
        self.lista_kart = []

    def dodajKarte(self, rodzaj, nr_karty):

        if rodzaj not in ["kredytowa", "bankomatowa", "debetowa"]:
            raise NiepoprawnyRodzajException()

        karta = None
        if rodzaj == "kredytowa":
            limit = input("Podaj limit karty kredytowej: ")
            karta = KartaKredytowa(nr_karty, limit)
        elif rodzaj == "bankomatowa":
            karta = KartaBankomatowa(nr_karty)
        elif rodzaj == "debetowa":
            karta = KartaDebetowa(nr_karty)

        self.lista_kart.append(karta)

    def usunKarte(self, nr_karty):
        for karta in self.lista_kart:
            if karta.getNr_karty() == nr_karty:
                self.lista_kart.remove(karta)

    def wplac(self, kwota):
        self.saldo += kwota

    def wyplac(self, kwota):
        self.saldo -= kwota

    def getKarty(self):
        return self.lista_kart

    def getSaldo(self):
        return self.saldo

    def getNrKonta(self):
        return self.nr_konta