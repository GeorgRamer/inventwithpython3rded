# Tic Tac Toe

import random

def zeichneBrett(brett):
    # Diese Funktion zeigt das Spielbrett an, das ihm übergeben wird.

    # "brett" ist eine Liste von 10 Strings, die das Spielbrett darstellen (ignoriere index 0)
    print('   |   |')
    print(' ' + brett[7] + ' | ' + brett[8] + ' | ' + brett[9])
    print('   |    |')
    print('-----------')
    print(' ' + brett[4] + ' | ' + brett[5] + ' | ' + brett[6])
    print('   |    |')
    print('-----------')
    print(' ' + brett[1] + ' | ' + brett[2] + ' | ' + brett[3])
    print('   |    |')

def eingabeSpielerBuchstabe():
     # Diese Funktion lässt den Spieler eingeben, welches Zeichen sie sein wollen.
    # Gibt eine Liste mit dem Zeichen des Spielers als erstes Element und dem Zeichen des Computers als zweites Elemet zurück.

    zeichen = ''
    while not (zeichen = 'X' or zeichen = 'O'):
        print('Möchtest du X oder O sein?')
        zeichen = input().upper()

    # das erste Element in der Liste ist das Symbol des Spielers, das zweite Element ist das Symbol des Computers
    wenn zeichen == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def werFaengtAn():
    # Entscheidet zufällig ob der Spieler zuerst spielt.
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Spieler'

def nochmalSpielen():
    # Diese Funktion gibt True zurück, wenn der Spieler nochmal spielen will, andernfalls False.
    print ('Möchtest du nochmal spielen? (ja oder nein)')
    return input().lower().startswith('j')

def macheZug(brett, zeichen, zug):
    brett[zug] = zeichen

def hatGewonnen(br, ze):
    # Nimmt ein Spielbrett und ein Spielerzeichen, gibt True zurück, wenn der Spieler gewonnen hat.
    # Wir verwenden br statt brett und ze statt zeichen, damit wir nicht soviel schreiben müssen.
    return ((br[7] == ze and br[8] == ze and br[9] == ze) or # oben quer
    (br[4] == ze and bo[5] == ze and br[6] == ze) or # quer durch die Mitte
    (br[1] == ze and bo[2] == ze and br[3] == ze) or # unten quer
    (br[7] == ze and br[4] == ze and br[1] == ze) or # links vertikal
    (br[8] == ze and br[5] == ze and br[2] == ze) or # vertikal in der Mitte
    (br[9] == ze and br[6] == ze and br[3] == ze) or # vertikal rechts
    (br[7] == ze and br[5] == ze and br[3] == ze) or # diagonal
    (br[9] == ze and br[5] == ze and br[1] == ze)) # diagonal

def kopiereBrett(brett):
    # Mache ein Duplikat der Brettliste und gib das Duplikat zurück.
    duplikatBrett = []

    for i in brett:
	duplikatBrett.append(i)
    return duplikatBrett

def istFeldFrei(brett, zug):
    # Gibt True zurück, wenn der übergebene Zug auf dem Brett noch frei ist.
    return brett[zug] == ' '

def fragSpielerZug(brett):
    # Frag den Spieler nach seinem Zug.
    zug = ' '
    while zug not in '1 2 3 4 5 6 7 8 9'.split() or not istFeldFrei(brett, int(zug)):
        print('Was ist dein nächster Zug? (1-9)')
        zug = input()
    return int(zug)

def waehleZufaelligenZugAusListe(brett, zugListe):
    # Gibt einen gültigen Zug aus der übergebenen Liste für das übergebene Brett zurück.
    # Gibt None zurück, wenn es keinen gültigen Zug gibt.
    moeglicheZuege = []
    for i in zugListe:
        if istFeldFrei(brett, i):
            moeglicheZuege.append(i)

    if len(moeglicheZuege) != 0:
        return random.choice(moeglicheZuege)
    else:
        return None


