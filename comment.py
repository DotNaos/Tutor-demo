# Aufgabe 1: Berechnung der Summe von zwei Zahlen

# Diese Funktion berechnet die Summe von zwei Zahlen.
def berechne_summe(a, b):
    return a + b  # Rückgabe der Summe

print(berechne_summe(3, 5))  # Ausgabe: 8


# Aufgabe 2: Temperaturumrechnung (Celsius zu Fahrenheit)
def celsius_to_fahrenheit(celsius):
    # Berechnung
    return (celsius * 9/5) + 32  # Formel für die Umrechnung

print(celsius_to_fahrenheit(0))  # Ausgabe: 32


# Aufgabe 3: Überprüfung, ob eine Zahl gerade oder ungerade ist

# Diese Funktion überprüft, ob eine Zahl gerade oder ungerade ist.
def ist_gerade(zahl):
    # Modulo-Operation, um den Rest bei der Division durch 2 zu erhalten
    if zahl % 2 == 0:  # Wenn der Rest 0 ist
        # Rückgabe von True, weil die Zahl gerade ist
        return True
    else:
        # Rückgabe von False, weil die Zahl ungerade ist
        return False

print(ist_gerade(4))  # Ausgabe: True


# Aufgabe 4: Berechnung des Faktorials einer Zahl

# Diese Funktion berechnet das Faktorial einer Zahl rekursiv.
def faktorial(n):
    # Basisfall: Wenn n 1 oder kleiner ist, gib 1 zurück.
    if n <= 1:
        return 1
    # Rekursiver Fall: Multipliziere n mit dem Faktorial von n-1.
    else:
        return n * faktorial(n - 1)

print(faktorial(5))  # Ausgabe: 120


# Aufgabe 5: Überprüfung, ob eine Zahl positiv, negativ oder null ist

def zahl_status(zahl):
    if zahl > 0:
        return "positiv"
    elif zahl < 0:
        return "negativ"
    else:
        return "null"

print(zahl_status(-3))  # Ausgabe: negativ
