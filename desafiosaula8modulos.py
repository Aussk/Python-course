# FASE 8 -------
from math import sqrt
num = int(input("digite um número inteiro : "))
raiz = sqrt(num)
print(f"a raiz de {num} é igual a {raiz}")

# desafio 016
from math import floor
x = float(input("digite qualquer número real : "))
i = floor(x)
print(f"o número {x} tem a parte inteira {i}")

# desafio 017
from math import hypot
co = float(input("comprimento do cateto oposto : "))
ca = float(input("comprimento do cateto adjacente : "))
hi = hypot(co,ca)
print("a hipotenusa mede {:.2f}".format(hi))

# desafio 018
from math import sin,cos,tan
angulo = float(input("digite um angulo qualquer : "))
sen = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print("o ângulo {} possui sen = {:.2f} , cos = {:.2f} e tan = {:.2f}".format(angulo,sen,cosseno,tangente))

# desafio 019
import random
n1 = str(input("primeiro aluno : "))
n2 = str(input("segundo aluno : "))
n3 = str(input("terceiro aluno : "))
n4 = str(input("quarto aluno : "))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f"o escolhido foi {escolhido}")

# desafio 020
from random import shuffle
a1 = str(input("primeiro aluno : "))
a2 = str(input("segundo aluno : "))
a3 = str(input("terceiro aluno : "))
a4 = str(input("quarto aluno : "))
lista2 = [a1,a2,a3,a4]
shuffle(lista2)
print("a ordem de apresentação será : {}".format(lista2))















