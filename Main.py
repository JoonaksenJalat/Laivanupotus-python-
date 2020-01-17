import os
import Gamer

p1gps = []
p2gps = []

# funktio jolla laivat asettuva asemiinsa
def LaivojenAsettelu(Pelaaja):
    Kierros = 1

    while Kierros < 4:

        LaivanPituus = Kierros + 1

        print("on pelaajan " + Pelaaja.Nimi + " vuoro")

        for x in Pelaaja.PelaajanLaivat:
            print(x)

        Rivi = int(input("anna rivi 1-5: "))
        Sarake = input("anna sarake A-E")
        Suunta = input("vaaka vai pysty suunnassa? p/v")
        Index = Pelaaja.PelaajanLaivat[0].index(Sarake.upper())  # etsii oikean sarakkeen
        Sarake = Index

        if Suunta == "p":
            for i in range(LaivanPituus):
                Pelaaja.PelaajanLaivat[Rivi + i][Sarake] = "X"
                gps = Rivi + i, Sarake
                if Kierros == 1:
                    Pelaaja.PelaajanLaiva1.append(gps)
                if Kierros == 2:
                    Pelaaja.PelaajanLaiva2.append(gps)
                if Kierros == 3:
                    Pelaaja.PelaajanLaiva3.append(gps)

        if Suunta == "v":
            for i in range(LaivanPituus):
                Pelaaja.PelaajanLaivat[Rivi][Sarake + i] = "X"
                gps = Rivi, Sarake + i
                if Kierros == 1:
                    Pelaaja.PelaajanLaiva1.append(gps)
                if Kierros == 2:
                    Pelaaja.PelaajanLaiva2.append(gps)
                if Kierros == 3:
                    Pelaaja.PelaajanLaiva3.append(gps)

        Kierros = Kierros + 1

        os.system('cls')


def Pommitus(Pelaaja, Vastustaja):
    up = 0
    voitto = False
    for x in Pelaaja.PelaajanOsumat:
        print(x)

    print(Pelaaja.Nimi)

    Rivi = int(input("anna rivi : "))
    Sarake = input("anna sarake : ")
    Index = Pelaaja.PelaajanOsumat[0].index(
        Sarake.upper())  # Hakee valitun sarakkeen indexin helpottaa ajattelua eritellä
    Sarake = Index
    Osuuko = Vastustaja.PelaajanLaivat[Rivi][Sarake]
    gps = Rivi, Sarake
    Pelaaja.PelaajanAmmutut.append(gps)  # Lisätään osuma osuma historiaan

    if Osuuko != "0":
        Pelaaja.PelaajanOsumat[Rivi][Sarake] = "X"
        print("osuma")
    if Osuuko == "0":
        Pelaaja.PelaajanOsumat[Rivi][Sarake] = "M"
        print("ohi")

    # Kaikki lXoX muuttujat muuttuvat sen mukana onko laiva jo kokonaan upotettu
    if Pelaaja.l1o1 == False:
        om = set(Pelaaja.PelaajanAmmutut).intersection(Vastustaja.PelaajanLaiva1)
        ou = len(om)
        if ou == 2:
            print("laiva upotettu")
            up = up + 1
            Pelaaja.l1o1 = True
    if Pelaaja.l1o2 == False:
        om = set(Pelaaja.PelaajanAmmutut).intersection(Vastustaja.PelaajanLaiva2)
        ou = len(om)
        if ou == 3:
            print("laiva upotettu")
            up = up + 1
            Pelaaja.l1o2 = True
    if Pelaaja.l1o3 == False:
        om = set(Pelaaja.PelaajanAmmutut).intersection(Vastustaja.PelaajanLaiva3)
        ou = len(om)
        if ou == 4:
            print("laiva upotettu")
            up = up + 1
            Pelaaja.l1o3 = True

    if Pelaaja.l1o1 == True & Pelaaja.l1o2 == True & Pelaaja.l1o3 == True:
        print("voitit")
        voitto = True
    print("olet upottanut " + str(up) + " laivaa")
    input("paina jotain jatkaaksesi")
    os.system('cls')
    return voitto

# Pelin runko
def Peli():
    print("peli")

    Pelaaja1nimi = input("1. pelaajan nimi: ")
    Pelaaja2nimi = input("2. pelaajan nimi: ")

    PelaajaYksi = Gamer.Komentaja(Pelaaja1nimi)
    PelaajaKaksi = Gamer.Komentaja(Pelaaja2nimi)

    LaivojenAsettelu(PelaajaYksi)
    LaivojenAsettelu(PelaajaKaksi)

    Pelikaynnissa = True
    Vuoro = 1

    while Pelikaynnissa == True:  # HUOM HUOM selvitä voitto juttu

        if Vuoro % 2 != 0:
            Pelaaja = PelaajaYksi
            Vastustaja = PelaajaKaksi
        else:
            Pelaaja = PelaajaKaksi
            Vastustaja = PelaajaYksi

        if Pommitus(Pelaaja, Vastustaja):
            print("peli loppui")
            Kierros = Vuoro
            print("peli kesti: " + Kierros + " kierrosta")
            Pelikaynnissa = False

        Vuoro = Vuoro + 1


print("laivanupotus")
Aloitetaanko = input("Aloitetaanko peli? K/Y : ")
Aloitetaanko = Aloitetaanko.upper()
print(Aloitetaanko)

if Aloitetaanko == "K":
    print("aloitetaan")
    Peli()
elif Aloitetaanko != "K":
    print("lopetettaan sitten")