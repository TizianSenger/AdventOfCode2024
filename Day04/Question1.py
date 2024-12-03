print("Day1 Question1")

def readDataFromFile():
    file = open("AdventOfCode2024\Day1\source.txt", "r")
    content = file.read()
    print(content)
    file.close()

readDataFromFile()


Um ein Regex zu erstellen, das auf ein beliebiges Präfix aus do() oder dont(), gefolgt von einer beliebigen Anzahl an Zeichen (außer dem genauen Muster mul(\d+,\d+)), und schließlich dem exakten mul(\d+,\d+) am Ende prüft, kannst du das folgende Regex verwenden:

^(do|dont).*?(?<!mul\d+,\d+)mul\d+,\d+$

Erklärung:

^ : Start des Strings.

(do|dont) : Entweder do() oder dont().

.*? : Beliebige Zeichen (nicht-gierig).

(?<!mul\d+,\d+) : Negative Lookbehind, um sicherzustellen, dass das Muster nicht direkt vor dem finalen mul(\d+,\d+) steht.

mul\d+,\d+$ : Sucht exakt nach mul(zahl,zahl) am Ende des Strings.

$ : Ende des Strings.


Beispiele:

✅ do()abcxyzmul(12,34) – Matcht.

❌ do()abcxyzmul(56,78)mul(12,34) – Kein Match, da das Muster zweimal vorkommt.

✅ dont()anything123mul(9,0) – Matcht.


Lass mich wissen, falls du weitere Anpassungen benötigst!

