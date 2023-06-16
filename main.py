from centrumObslugiKart import CentrumObslugiKart
from Exceptions import NiepoprawnyRodzajException, NiepoprawnyNumerKartyException
import os
import dill
import sys
import time

#centrum = CentrumObslugiKart()

with open('data.pkl', 'rb') as file:
    centrum = dill.load(file)


while(True):
    print("----Centrum Obslugi Kart----")
    print("1. Zarzadzaj firmami")
    print("2. Zarzadzaj bankami")
    print("3. Zarzadzaj osobami")
    print("4. Zarzadzaj kartami oraz pieniedzmi")
    print("5. Dokonaj platnosci")
    print("6. Zarzadzaj archiwum")
    print("7. Zakoncz prace")
    wybor = int(input("Wprowadz odpowiedni numer: "))

    match wybor:
        case 1:
            os.system('cls')
            print("----Zarzadzanie firmami----")
            print("1. Dodaj firme")
            print("2. Usun firme")
            print("3. Przegladaj firmy")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    nazwa_banku = str(input("Podaj nazwe banku, w ktorym bedzie firma: "))
                    rodzaj = str(input("Podaj rodzaj firmy(sklep, zaklad uslugowy, firma transportowa): "))
                    nazwa = str(input("Podaj nazwe firmy: "))
                    NIP = str(input("Podaj NIP firmy: "))
                    nr_konta = str(input("Podaj numer konta firmy: "))
                    saldo = float(input("Podaj poczatkowe saldo firmy: "))

                    centrum.dodajFirme(rodzaj, nazwa, NIP, nr_konta, saldo)

                    for bank in centrum.przegladBankow():
                        if nazwa_banku == bank.getNazwa():
                            bank.dodajFirme(rodzaj, nazwa, NIP, nr_konta, saldo)

                case 2:
                    NIP = str(input("Podaj NIP firmy, ktorej chcesz usunac: "))

                    centrum.usunFirme(NIP)

                    for bank in centrum.przegladBankow():
                        for firma in bank.przegladFirm():
                            if NIP == firma.getNIP():
                                bank.usunFirme(NIP)

                case 3:
                    os.system('cls')
                    for bank in centrum.przegladBankow():
                        for firma in bank.przegladFirm():
                            print(f"{firma.getNazwa()} {firma.getNIP()} {firma.getKonto().saldo}")
                    time.sleep(3)

        case 2:
            os.system('cls')
            print("----Zarzadzanie bankami----")
            print("1. Dodaj Bank")
            print("2. Usun Bank")
            print("3. Przegladaj banki")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    nazwaBankuDoDodania = str(input("Podaj nazwe banku: "))
                    centrum.dodajBank(nazwaBankuDoDodania)
                case 2:
                    nazwaBankuDoUsuniecia = str(input("Podaj nazwe banku: "))
                    for bank in centrum.przegladBankow():
                        if nazwaBankuDoUsuniecia == bank.getNazwa():
                            centrum.usunBank(nazwaBankuDoUsuniecia)
                case 3:
                    os.system('cls')
                    banki = centrum.przegladBankow()
                    for bank in banki:
                        print(bank.getNazwa())
                    time.sleep(3)


        case 3:
            os.system('cls')
            print("----Zarzadzanie osobami----")
            print("1. Dodaj osobe")
            print("2. Usun osobe")
            print("3. Przegladaj osoby")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    imie = str(input("Podaj imie osoby ktora chcesz dodac: "))
                    nazwisko = str(input("Podaj nazwisko osoby ktora chcesz dodac: "))
                    poczatkowe_saldo = int(input("Podaj poczatkowe saldo: "))
                    nazwaBanku = str(input("Podaj nazwe banku: "))
                    nr_konta = str(input("Podaj numer konta: "))

                    for bank in centrum.przegladBankow():
                        if bank.getNazwa() == nazwaBanku:
                            bank.dodajOsobe(imie,nazwisko,nr_konta,poczatkowe_saldo)

                case 2:
                    imie_osoby = str(input("Podaj imie osoby do usuniecia: "))
                    nazwisko_osoby = str(input("Podaj nazwisko osoby do usuniecia: "))
                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie_osoby and osoba.getNazwisko() == nazwisko_osoby:
                                bank.usunOsobe(imie_osoby,nazwisko_osoby)
                case 3:
                    os.system('cls')
                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            print(f"{osoba.getImie()} {osoba.getNazwisko()} {osoba.getKonto().getNrKonta()} {osoba.getKonto().getSaldo()}")
                    time.sleep(3)
        case 4:
            os.system('cls')
            print("----Zarzadzanie kartami----")
            print("1. Dodaj karte")
            print("2. Usun Karte")
            print("3. Wplac pieniadze")
            print("4. Wyplac pieniadze")
            print("5. Przegladaj karty")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))
                    rodzaj = str(input("Podaj rodzaj karty(kredytowa, debetowa, bankomatowa): "))
                    nr_karty = str(input("Podaj numer karty: "))


                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                try:
                                    osoba.konto.dodajKarte(rodzaj, nr_karty)
                                except NiepoprawnyRodzajException as e:
                                    print(e.args[0])

                case 2:
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))
                    nr_karty = str(input("Podaj numer karty, ktora chcesz usunac: "))
                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                try:
                                    osoba.konto.usunKarte(nr_karty)
                                except NiepoprawnyRodzajException as e:
                                    print(e.args[0])

                case 3:
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))
                    kwota = float(input("Wplacana kwota: "))

                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                osoba.konto.wplac(kwota)
                case 4:
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))
                    kwota = float(input("Wyplacana kwota: "))

                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                osoba.konto.wyplac(kwota)
                case 5:
                    os.system('cls')
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))

                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                for karta in osoba.getKonto().getKarty():
                                    print(f"{karta.getRodzaj()} {karta.getNr_karty()}")
                    time.sleep(3)


        case 5:
            os.system('cls')
            NIP = str(input("Podaj NIP firmy, do ktorej maja byc przelane pieniadze: "))
            nr_karty = str(input("Podaj numer karty, ktora dokonana bedze transakcja: "))
            kwota = float(input("Podaj kwote: "))
            bank_firmy = None
            bank_klienta = None

            for bank in centrum.przegladBankow():
                for firma in bank.przegladFirm():
                    if firma.getNIP() == NIP:
                        bank_firmy = bank

            for bank in centrum.przegladBankow():
                for osoba in bank.przegladOsob():
                    for karta in osoba.konto.getKarty():
                        if karta.getNr_karty() == nr_karty:
                            bank_klienta = bank

            centrum.platnosc(NIP, nr_karty, kwota, bank_klienta, bank_firmy)

        case 6:
            os.system('cls')
            print("----Zarzadzanie archiwum----")
            print("1. Zapisz dane do pliku")
            print("2. Przeszukaj archiwum")
            print("3. Wyswietl archiwum")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    centrum.ZapiszDoPliku()

                case 2:
                    centrum.przeszukiwanieArchiwum()

                case 3:
                    for platnosc in centrum.getArchiwum():
                        print(platnosc)

        case 7:
            with open('data.pkl', 'wb') as file:
                dill.dump(centrum, file)
            sys.exit(0)