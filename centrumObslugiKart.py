import csv
from firma import FirmaTransportowa, Sklep, ZakladUslugowy
from bank import Bank

class CentrumObslugiKart:
    def __init__(self):
        self.__archiwum = []
        self.__lista_bankow = []
        self.__lista_firm = []

    def poczatek_pliku(self):
        with open('archiwum.csv', 'w', newline='') as plik:
            writer = csv.writer(plik)
            writer.writerow(['bank','NIP firmy','imie','nazwisko','kwota'])
        plik.close()

    def dodajFirme(self, rodzaj, nazwa, NIP, nr_konta, saldo):
        if rodzaj == "sklep":
            self.__lista_firm.append(Sklep(nazwa, NIP, nr_konta, saldo))
        elif rodzaj == "zaklad uslugowy":
            self.__lista_firm.append(ZakladUslugowy(nazwa, NIP, nr_konta, saldo))
        elif rodzaj == "firma transportowa":
            self.__lista_firm.append(FirmaTransportowa(nazwa, NIP, nr_konta, saldo))

    def usunFirme(self, NIP):
        for firma in self.__lista_firm:
            firma_NIP = getattr(firma,'NIP',None)
            if firma_NIP == NIP:
                self.__lista_firm.remove(firma)
                break

    def przegladFirm(self, rodzaj):
        for firma in self.__lista_firm:
            if getattr(firma, 'getRodzaj') and callable(getattr(firma, 'getRodzaj')):
                if firma.getRodzaj() == rodzaj:
                    print(firma.getNazwa() + "\n")

    def dodajBank(self, nazwa):
        bank = Bank(nazwa)
        self.__lista_bankow.append(bank)

    def usunBank(self,nazwa):
        for bank in self.__lista_bankow:
            bank_nazwa = getattr(bank,'nazwa')
            if bank_nazwa == nazwa:
                self.__lista_bankow.remove(bank)

    def przegladBankow(self):
        for bank in self.__lista_bankow:
            print(getattr(bank, 'nazwa'))

    def platnosc(self, NIP, nr_karty, kwota, bank_klienta, bank_firmy):
        for i in range (0,len(self.__lista_bankow)):
            if self.__lista_bankow[i] == bank_klienta:
                znaleziony_bank = self.__lista_bankow[i]
                szukane_konto = znaleziony_bank.znajdzKonto(nr_karty)
                szukane_konto.saldo -= kwota
                break

        for i in range(0,len(self.__lista_bankow)):
            if self.__lista_bankow[i] == bank_firmy:
                znaleziony_bank_firmy = self.__lista_bankow[i]
                for firma in znaleziony_bank_firmy.getFirmy:
                    firma_NIP = getattr(firma,'NIP',None)
                    if firma_NIP == NIP:
                        szukana_firma = firma
                        szukane_konto_firmy = getattr(szukana_firma,'konto',None)
                        szukane_konto_firmy.saldo -= kwota
                        break

    def ZapiszDoPliku(self, bank, NIP, imie, nazwisko, kwota):
        # do zmiany
        nowy_wpis = [bank,NIP,imie,nazwisko,kwota]
        # lista = [item for item in archiwum[0].values()]
        with open('archiwum.csv','a',newline='') as plik:
            writer = csv.writer(plik)
            writer.writerow(nowy_wpis)
        plik.close()

    def OdczytZpliku(self):
        with open('archiwum.csv','r') as plik:
            reader = csv.reader(plik)
            for row in reader:
                print(row)
        plik.close()

    def zarchiwizuj(self, bank, NIP, nr_karty, imie, nazwisko, kwota):
        platnosc = {
            "nazwa_banku": f"{getattr(bank, 'nazwa')}",
            "NIP_firmy": NIP,
            "nr_karty": nr_karty,
            "imie": imie,
            "nazwisko": nazwisko,
            "kwota": kwota,
        }
        self.__archiwum.append(platnosc)

    def przeszukiwanieArchiwum(self):
        pass