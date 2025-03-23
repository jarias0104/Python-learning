# Jeshua Nauel Arias Santos 
# Currencies Exercise: I have Colombian Pesos, Peruvian Soles and Brazilian reais, I need to write a program that will ask the user how much he has of each and then sum the total in USD

pesos = int (input ("How much do you have in pesos? "))
soles = int (input ("How much do you have in soles? "))
reais = int (input ("How much do you have in reais? "))

colombianToUsd = 0.00024 * pesos
solesToUsd = 0.27 * soles
reaisToUsd = 0.17 * reais

total = colombianToUsd+solesToUsd+reaisToUsd

print(total)

