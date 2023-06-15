from abc import ABC, abstractmethod

class Karta(ABC):
    def __init__(self, nr_karty):
        self.__nr_karty = nr_karty

    @abstractmethod
    def getRodzaj(self):
        pass

    def getNr_karty(self):
        return self.__nr_karty

class KartaKredytowa(Karta):
    def __init__(self, nr_karty, limit):
        super().__init__(nr_karty)
        self.__limit = limit

    def getRodzaj(self):
        return "kredytowa"

    def getLimit(self):
        return self.__limit


class KartaDebetowa(Karta):
    def __init__(self, nr_karty):
        super().__init__(nr_karty)

    def getRodzaj(self):
        return "kredytowa"


class KartaBankomatowa(Karta):
    def __init__(self, nr_karty):
        super().__init__(nr_karty)

    def getRodzaj(self):
        return "kredytowa"
