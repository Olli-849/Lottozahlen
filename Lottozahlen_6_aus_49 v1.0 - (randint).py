
from random import randint

zahlenpool = list(range(1, 50))     # Gesamtpool der Zahlen von 1-49

print("Gesamtzahlen:\n", zahlenpool, "\n", sep="") # Ausgabe des Zahlen-Pools als Test

for i in range(0, 6):               # 6 Durchläufe, da 6 Zahlen gezogen werden sollen
    rand_zahl = randint(1, 49 - i)  # Die Range für die Zufallszahlen wird jedesmal kleiner
    print(i+1, ". Ziehung: ", zahlenpool.pop(rand_zahl-1), sep="")
    print(zahlenpool)               # Ausgabe des verbleibenden Zahlen-Pools als Test

"""
Hinweise:
- Die ermittelten Zufallszahlen werden als Index genutzt und nicht direkt ausgegeben
- Index x löscht auch Zahl x aus dem Pool
- Damit kann selbst bei gleichem Index nie dieselbe Zahl ausgegeben werden
- Der Pool für die Indizes schrumpft mit jedem Durchlauf

Beispiel:
Gesamtpool: 49 Zahlen/Indizes
1. Zahl: 8
- heisst, die Zufallszahl 7 wurde im Hintergrund eigentlich ermittelt
- auf Index 7 sitzt die Zahl 8
- diese wird als gezogene Zahl angegeben und gleichzeitig aus dem Pool entfernt (Gesamtpool: 48 Zahlen)
- damit rückt die Zahl 9 auf den Index 7 vor

Gesamtpool: 48 Zahlen/Indizes
2. Zahl: 9
- heisst, die Zufallszahl 7 wurde im Hintergrund erneut ermittelt
- auf Index 7 sitzt die 9, die als gezogene Zahl angegeben wird und aus dem Pool damit verschwindet

Gesamtpool: 47 Zahlen/Indizes
usw.
"""
