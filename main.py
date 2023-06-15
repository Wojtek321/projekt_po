from centrumObslugiKart import CentrumObslugiKart
import os

centrum = CentrumObslugiKart()

while(True):
    os.system('cls')
    print("----Centrum Obslugi Kart----")
    print("1. Zarzadzaj firmami")
    print("2. Zarzadzaj bankami")
    print("3. Zarzadzaj osobami")
    print("4. Zarzadzaj kartami oraz pieniedzmi")
    print("5. Dokonaj platnosci")
    print("6. Zarzadzaj archiwum")
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
                    firmy = centrum.przegladFirm()
                    for firma in firmy:
                        print(f"{firma.getNazwa()} {firma.getNIP()}")

        case 2:
            os.system('cls')
            print("----Zarzadzanie bankami----")
            print("1. Dodaj Bank")
            print("2. Usun Bank")
            print("3. Przegladaj banki")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    nazwaBankuDoDodania = str(input("Podaj nazwe banku"))
                    centrum.dodajBank(nazwaBankuDoDodania)
                case 2:
                    nazwaBankuDoUsuniecia = str(input("Podaj nazwe banku"))
                    for bank in centrum.przegladBankow():
                        if nazwaBankuDoUsuniecia == bank.getNazwa():
                            centrum.usunBank(nazwaBankuDoUsuniecia)
                case 3:
                    banki = centrum.przegladBankow()
                    for bank in banki:
                        print(bank.getNazwa)

        case 3:
            os.system('cls')
            print("----Zarzadzanie osobami----")
            print("1. Dodaj osobe")
            print("2. Usun osobe")
            print("3. Przegladaj osoby")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass

        case 4:
            os.system('cls')
            print("----Zarzadzanie kartami----")
            print("1. Dodaj karte")
            print("2. Usun Karte")
            print("3. Wplac pieniadze")
            print("4. Wyplac pieniadze")
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
                                osoba.konto.dodajKarte(rodzaj, nr_karty)
                case 2:
                    imie = str(input("Podaj imie wlasciciela: "))
                    nazwisko = str(input("Podaj nazwisko wlasciciela: "))
                    nr_karty = str(input("Podaj numer karty, ktora chcesz usunac: "))
                    for bank in centrum.przegladBankow():
                        for osoba in bank.przegladOsob():
                            if osoba.getImie() == imie and osoba.getNazwisko() == nazwisko:
                                osoba.konto.usunKarte(nr_karty)

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
            pass
        case 6:
            os.system('cls')
            print("----Zarzadzanie archiwum----")
            print("1. Zapisz dane do pliku")
            print("2. Odczytaj dane z pliku")
            print("3. Przeszukaj archiwum")
            wybor = int(input("Wprowadz odpowiedni numer: "))

            match wybor:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
