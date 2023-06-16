class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NiepoprawnyRodzajException(MyException):
    def __init__(self):
        super().__init__("Wprowadzono niepoprawny rodzaj karty.")


class NiepoprawnyNumerKartyException(MyException):
    def __init__(self):
        super().__init__("Podano niepoprawny numer karty.")