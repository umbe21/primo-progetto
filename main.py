print("Benvenuto nella Calcolatrice Base!")

num1 = float(input("Inserisci il primo numero: "))
operatore = input("Inserisci l'operatore (+, -, *, /): ")
num2 = float(input("Inserisci il secondo numero: "))

if operatore == "+":
    risultato = num1 + num2
elif operatore == "-":
    risultato = num1 - num2
elif operatore == "*":
    risultato = num1 * num2
elif operatore == "/":
    if num2 != 0:
        risultato = num1 / num2
    else:
        risultato = "Errore: divisione per zero"
else:
    risultato = "Operatore non valido"

print("Risultato:", risultato)