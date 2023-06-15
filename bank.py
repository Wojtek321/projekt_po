from osoba import Osoba
from firma import FirmaTransportowa, ZakladUslugowy, Sklep
class Bank:
    def __init__(self, nazwa):
        self.__nazwa = nazwa
        self.__lista_osob = []
        self.__lista_firm = []

    def dodajOsobe(self, imie, nazwisko, nr_konta, saldo):
        self.__lista_osob.append(Osoba(imie, nazwisko, nr_konta, saldo))

    def usunOsobe(self, imie, nazwisko):
        for osoba in self.__lista_osob:
            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                self.__lista_osob.remove(osoba)

    def przegladOsob(self):
        return self.__lista_osob

    def dodajFirme(self, rodzaj, nazwa, NIP, nr_konta, saldo):
        if rodzaj == "sklep":
            self.__lista_firm.append(Sklep(nazwa, NIP, nr_konta, saldo))
        elif rodzaj == "zaklad uslugowy":
            self.__lista_firm.append(ZakladUslugowy(nazwa, NIP, nr_konta, saldo))
        elif rodzaj == "firma transportowa":
            self.__lista_firm.append(FirmaTransportowa(nazwa, NIP, nr_konta, saldo))

    def usunFirme(self, NIP):
        for firma in self.__lista_firm:
            if firma.getNIP() == NIP:
                self.__lista_firm.remove(firma)

    def przegladFirm(self):
        return self.__lista_firm

    def dodajKarte(self, imie, nazwisko, rodzaj, nr_karty):
        for osoba in self.__lista_osob:
            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                osoba.getKonto().dodajKarte(rodzaj, nr_karty)

    def usunKarte(self, imie, nazwisko, nr_karty):
        for osoba in self.__lista_osob:
            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                for karta in osoba.getKonto().getKarty():
                    if karta.getNr_karty() == nr_karty:
                        osoba.getKonto().getKarty().remove(karta)

    def autoryzuj(self, nr_karty, kwota):
        for osoba in self.__lista_osob:
            for karta in osoba.getKonto().getKarty():
                if karta.getNr_karty() == nr_karty:
                    if karta.getRodzaj() == "kredytowa":
                        if karta.getLimit() <= kwota and osoba.getKonto().getSaldo() >= kwota:
                            return True
                    else:
                        if osoba.getKonto().getSaldo() >= kwota:
                            return True
        return False

    def znajdzKonto(self, nr_karty):
        for osoba in self.__lista_osob:
            for karta in osoba.getKonto():
                if karta.getNr_karty() == nr_karty:
                    return osoba.getKonto()

    def rodzajKarty(self, konto, nr_karty):
        for osoba in self.__lista_osob:
            for karta in osoba.getKonto().getKarty():
                if osoba.getKonto() == konto and karta.getNr_karty() == nr_karty:
                    return karta.getRodzaj()

    def getFirmy(self):
        return self.__lista_firm

    def getNazwa(self):
        return self.__nazwa