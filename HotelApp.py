## Schmidt Bálint András (A8HU0R) beadandó feladat

from abc import ABC
import datetime

class Szoba(ABC):
    def __init__(self, szobaSzam, ar):
        self.szobaSzam = szobaSzam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaSzam, furdoTipusa, ar = 2000):
        super().__init__(szobaSzam, ar = 2000)
        self.furdoTipusa = furdoTipusa

    def __str__(self):
        return f"Szobaszám: {self.szobaSzam}, Dátum: {self.szobaSzam} , Fűrdő tpíusa: {self.furdoTipusa}"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaSzam, tegerreNez, ar = 3000):
        super().__init__(szobaSzam, ar)
        self.tegerreNez = tegerreNez

    def __str__(self):
        return f"Szobaszám: {self.szobaSzam}, Dátum: {self.szobaSzam} , Terngere nézs : {self.tegerreNez}"

class Hotel:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def SzobaHozzaAd(self, room):
        self.szobak.append(room)

    def SzobaFoglalas(self, foglaltSzobaSzam):

        for x in self.foglalasok:
            if x.datum == foglaltSzobaSzam.datum:
                print(f"Ezen a napon {foglaltSzobaSzam} szoba már foglalt")
                return - 1
        self.foglalasok.append(foglaltSzobaSzam)

        for szoba in self.szobak:
            if szoba.szobaSzam == foglaltSzobaSzam.szobaSzam:
                return szoba.ar

        return -1

    def SzobaLemondas(self, lemondSzobaSzam, datum):

        for x in self.foglalasok:
            if x.szobaSzam == lemondSzobaSzam and x.datum == datum:
                self.foglalasok.remove(x)
                return True
        return False

    def Listazas(self):
        print("\n" + "-" * 35)
        for x in self.foglalasok:
            print(x)
        print("-" * 35)

    def ListazasSzobak(self):
        print("\n" + "-" * 55)
        for x in self.szobak:
            print(x)
        print("-" * 55)

class Foglalas:
    def __init__(self, szobaSzam, datum):
        self.szobaSzam = szobaSzam
        self.datum = datum

    def __str__(self):
        return f"Szobaszám: {self.szobaSzam}, Dátum: {self.datum} "


def felhasznaloiFelulet():
    kar = ""
    while kar != "Q" and kar != "q":
        print("\n" + "-" * 35)
        print("Fogalható szobák: 101, 202, 305")
        print("Válasszon opciót:")
        print("Q - kilépes,   F - foglalás,  T - törlés, L - foglalás listázása, S - Szobák listázása ")
        kar = input("Válasszál opciót: ")

        if(kar == "L" or kar == "l"):
            hotel.Listazas()

        elif(kar == "S" or kar == "s"):
            hotel.ListazasSzobak()
        
        elif(kar == "F" or kar == "f"):
            szoba = input("Foglalni kívánt szoba száma: ")

            while True:
                datum = input("Foglalni kívánt szoba dátuma: (ÉÉÉÉ-HH-NN): ")
                try:
                    datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
                    if datum >= datetime.date.today():
                        break
                    else:
                        print("A dátuma nem lehet a mai napnál korábbi!")
                except:
                    print("Hibás a formátum!")

            foglalasAdat = Foglalas(int(szoba), str(datum))
            result = hotel.SzobaFoglalas(foglalasAdat)

            if(result != -1):
                print("A foglalás sikeres!")
                print(f"A foglalt szoba ára: {result}")
            else:
                print("A foglalás sikertelen!")
        
        elif (kar == "T" or kar == "t"):
            szobaTorlesSzam = input("Törölni kívánt szoba száma: ")
            szobaTorlesDatum = input("Törölni kívánt szoba dátuma: (ÉÉÉÉ-HH-NN): ")
            resultTorles = hotel.SzobaLemondas(int(szobaTorlesSzam), szobaTorlesDatum)
            if(resultTorles):
                print("Foglalás sikeresen törölve!")
            else:
                print("Nem létező adat!")


hotel = Hotel("Teszt Szálloda")

szoba1 = EgyagyasSzoba(101, "zuhany")
szoba2 = KetagyasSzoba(202, True)
szoba3 = KetagyasSzoba(305, False)

hotel.SzobaHozzaAd(szoba1)
hotel.SzobaHozzaAd(szoba2)
hotel.SzobaHozzaAd(szoba3)

foglalas1 = Foglalas(101, "2024-05-05")
foglalas2 = Foglalas(202, "2024-06-01")
foglalas3 = Foglalas(305, "2024-05-02")
foglalas4 = Foglalas(101, "2024-05-11")
foglalas5 = Foglalas(101, "2024-05-23")

hotel.SzobaFoglalas(foglalas1)
hotel.SzobaFoglalas(foglalas2)
hotel.SzobaFoglalas(foglalas3)
hotel.SzobaFoglalas(foglalas4)
hotel.SzobaFoglalas(foglalas5)


felhasznaloiFelulet()

