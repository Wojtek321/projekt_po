from abc import ABC, abstractmethod
from konto import Konto

class Firma(ABC):
    def __init__(self, nazwa, NIP, nr_konta, saldo):
        self.__nazwa = nazwa
        self.__NIP = NIP
        self.__konto = Konto(nr_konta, saldo)

    @abstractmethod
    def getRodzaj(self):
        pass
    def getNazwa(self):
        return self.__nazwa

    def getKonto(self):
        return self.__konto

    def getNIP(self):
        return self.__NIP


class ZakladUslugowy(Firma):
    def __init__(self, nazwa, NIP, nr_konta, saldo):
        super().__init__(nazwa, NIP, nr_konta, saldo)

    def getRodzaj(self):
        return "zaklad uslugowy"


class Sklep(Firma):
    def __init__(self, nazwa, NIP, nr_konta, saldo):
        super().__init__(nazwa, NIP, nr_konta, saldo)

    def getRodzaj(self):
        return "sklep"


class FirmaTransportowa(Firma):
    def __init__(self, nazwa, NIP, nr_konta, saldo):
        super().__init__(nazwa, NIP, nr_konta, saldo)

    def getRodzaj(self):
        return "firma transportowa"
