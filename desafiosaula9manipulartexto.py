# desafio 022
nome = str(input("digite seu nome completo : "))
mai = nome.upper()
min = nome.lower()
semespaço = nome.replace(" ","")
tamanho = len(semespaço)
nome1 = len(nome.split()[0])
print(f"o nome completo com todas as letras maiusculas é {mai}, minusculas é {min}")
print(f",numero de letras sem espaços é {tamanho} e o número de letras do primeiro nome é {nome1}")

# desafio 023
numero = str(input("digite um número de 0 a 9999 : "))
milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]
print(f"milhar : {milhar}, centena : {centena}, dezena : {dezena} e unidade : {unidade}")

# desafio 024
cidade = str(input("digite o nome de uma cidade : ")).upper()
santo = "SANTO" in cidade.split()[-1]
print(santo)

# desafio 025
nome2 = str(input("digite seu nome completo : ")).title()
silva = "Silva" in nome2
print(silva)

# desafio 026
frase = str(input("digite uma frase qualquer : ")).lower()
print(frase.count("a"))
print(frase.find("a"))
print(frase.rfind("a"))

# desafio 027
nome3 = str(input("digite o nome completo  : "))
primeiro = nome3.split()[0]
ultimo = nome3.split()[-1]
print("primeiro = {},ultimo = {}".format(primeiro,ultimo))


































