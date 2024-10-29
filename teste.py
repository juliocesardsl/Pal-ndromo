texto = input('Digite uma palavra pra saber se é um palíndromo ou não: ')

texto = texto.replace(" ","").lower()

inverso = texto[::-1]

print("isso é um palíndromo" if texto == inverso else "não é um palíndromo")