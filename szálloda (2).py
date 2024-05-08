from datetime import datetime
from abc import ABC, abstractmethod

# Definiáljuk az osztályokat

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas_hozzaadas(self, szobaszam, datum):
        if datum <= datetime.now().date():
            return "A megadott dátum nem érvényes."
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return "Ez a szoba már foglalt erre a dátumra."
                self.foglalasok.append(Foglalas(szoba, datum))
                return f"Foglalás rögzítve: a(z) {szoba.szobaszam} szobára, dátum: {datum}. Ár: {szoba.ar} Ft" "\n \n          Köszönjük hogy a szállodánkat választotta." 
        return "Nem található ilyen szobaszám."

    def foglalas_torles(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás törölve."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        return "\n".join(f"Szobaszám: {f.szoba.szobaszam}, Dátum: {f.datum}, Ár: {f.szoba.ar} Ft" for f in self.foglalasok)

# Definiáljuk a felhasználói interfészt és az indító kódot

def start_app():
    szalloda = Szalloda("Budapest Hotel")
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 101))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 102))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 103))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 104))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 105))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 106))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 201))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 202))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 203))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(80000, 204))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 205))
    szalloda.szoba_hozzaadas(KetagyasSzoba(120000, 206))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(90000, 301))
    szalloda.szoba_hozzaadas(KetagyasSzoba(130000, 302))
    szalloda.szoba_hozzaadas(KetagyasSzoba(130000, 303))
    szalloda.szoba_hozzaadas(EgyagyasSzoba(90000, 304))

    foglalas_kezelo = FoglalasKezelo(szalloda)

    # Kezdeti foglalások
    foglalas_kezelo.foglalas_hozzaadas(101, datetime(2024, 5, 10).date())
    foglalas_kezelo.foglalas_hozzaadas(102, datetime(2024, 5, 21).date())
    foglalas_kezelo.foglalas_hozzaadas(106, datetime(2024, 6, 12).date())
    foglalas_kezelo.foglalas_hozzaadas(304, datetime(2024, 7, 23).date())
    foglalas_kezelo.foglalas_hozzaadas(202, datetime(2024, 8, 4).date())

    while True:
        print("\n********** Budapest Szálloda Foglalási Rendszere **********")
        print("1. Foglalás")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")
        if valasztas == "1":
            szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
            ev = int(input("Év: "))
            honap = int(input("Hónap: "))
            nap = int(input("Nap: "))
            datum = datetime(ev, honap, nap).date()
            print(foglalas_kezelo.foglalas_hozzaadas(szobaszam, datum))
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a lemondani kívánt szoba számát: "))
            ev = int(input("Év: "))
            honap = int(input("Hónap: "))
            nap = int(input("Nap: "))
            datum = datetime(ev, honap, nap).date()
            print(foglalas_kezelo.foglalas_torles(szobaszam, datum))
        elif valasztas == "3":
            print(foglalas_kezelo.foglalasok_listazasa())
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    start_app()
