from firma import FirmaTransportowa, Sklep, ZakladUslugowy
from bank import Bank
import pandas as pd
class CentrumObslugiKart:
    def __init__(self):
        self.__archiwum = []
        self.__lista_bankow = []
        self.__lista_firm = []

    def poczatek_pliku(self):
        self.ZapiszDoPliku()

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


    def dodajBank(self, nazwa):
        bank = Bank(nazwa)
        self.__lista_bankow.append(bank)

    def usunBank(self,nazwa):
        for bank in self.__lista_bankow:
            if bank.getNazwa() == nazwa:
                self.__lista_bankow.remove(bank)

    def przegladBankow(self):
        return self.__lista_bankow

    def platnosc(self, NIP, nr_karty, kwota, bank_klienta, bank_firmy):
        szukane_konto = bank_klienta.znajdzKonto(nr_karty)
        szukane_konto.wyplac(kwota)

        for firma in bank_firmy.przegladFirm():
            if firma.getNIP() == NIP:
                firma.getKonto().wplac(kwota)

        self.zarchiwizuj(bank_klienta,bank_firmy,NIP,nr_karty,kwota)


    def ZapiszDoPliku(self):
        excel = pd.DataFrame(self.__archiwum)
        excel.to_excel("Archiwum.xlsx",index=False)

    def zarchiwizuj(self, bank_klienta, bank_firmy, NIP, nr_karty, kwota):
        platnosc = {
            "Nazwa banku klienta": f"{bank_klienta.getNazwa()}",
            "Nazwa banku firmy": f"{bank_firmy.getNazwa()}",
            "NIP firmy": NIP,
            "numer karty": nr_karty,
            "kwota": kwota,
        }
        self.__archiwum.append(platnosc)


    def przeszukiwanieArchiwum(self):
        while(True):
            print("----Archiwum----")
            print("1. historia platnosci firmy")
            print("2. historia platnosci przechodzacych przez dany bank")
            print("3. historia platnosci dana karta")
            print("4. historia platnosci danej osoby")
            print("5. historia platnosci wzgledem danej kwoty")
            print("6. Wyjdz z archiwum")
            wybor = input("Wybierz numer(1-5): ")
            match wybor:
                case 1:
                    NIP_firmy = input(print("Podaj NIP firmy: "))
                    for i in range(0,len(self.__archiwum)):
                        if self.__archiwum[i][1] == NIP_firmy:
                            print(self.__archiwum[i])

                case 2:
                    nazwa_banku = input(print("Podaj nazwe banku: "))
                    for i in range(0,len(self.__archiwum)):
                        if self.__archiwum[i][0] == nazwa_banku:
                            print(self.__archiwum[i])

                case 3:
                    nr_karty = input(print("Podaj numer karty: "))
                    for i in range(0, len(self.__archiwum)):
                        if self.__archiwum[i][2] == nr_karty:
                            print(self.__archiwum[i])

                case 4:
                    imie = input(print("Podaj imie osoby: "))
                    nazwisko = input(print("Podaj nazwisko osoby: "))
                    for i in range(0, len(self.__archiwum)):
                        if self.__archiwum[i][3] == imie and self.__archiwum[i][4] == nazwisko:
                            print(self.__archiwum[i])

                case 5:
                    kwota = input(print("Podaj kwote: "))
                    print("Wybierz co chcesz zrobic: ")
                    print("1. Znajdz historie platnosci rowna danej kwocie")
                    print("2. Znajdz historie platnosci od danej kwoty w gore")
                    print("3. Znajdz historie platnosci ponizej danej kwoty")
                    match wybor:
                        case 1:
                            for i in range(0,len(self.__archiwum)):
                                if self.__archiwum[i][5] == kwota:
                                    print(self.__archiwum[i])

                        case 2:
                            for i in range(0, len(self.__archiwum)):
                                if self.__archiwum[i][5] > kwota:
                                    print(self.__archiwum[i])

                        case 3:
                            for i in range(0, len(self.__archiwum)):
                                if self.__archiwum[i][5] < kwota:
                                    print(self.__archiwum[i])

                case 6:
                    break

    def getArchiwum(self):
        return self.__archiwum