# Strings sind text-based data (Buchstaben)

beispiel = "Hello World"
print(beispiel[0])
# Printet den ersten String des Variabels "beispiel" (Output: "H")

print(beispiel[-1])
# Printet den letzten String des Variabels "beispiel" (Output: "d")

print(beispiel[0:])
# Printet den String von Index 0 bis zum letzten Index (Output: Hello World)


alter = int(input("Wie alt bist du?"))
print(alter)
# Wenn man im Input eine Zahl eingibt, wird die Zahl kein Integer sein sonder ein String deswegen "int(input())


# String Methods
s = "Hello, World!"
print(s.lower())  # Output: hello, world!
print(s.upper())  # Output: HELLO, WORLD!
print(s.title())  # Output: Hello, World!
print(len(s))  # Output: 13  // Die länge von "s"

r_method = "Hello World!"
print(r_method.replace("World", "Friend"))
# Output: Hello Friend // .replace um einen String zu ersetzten
