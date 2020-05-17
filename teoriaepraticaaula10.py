# FASE 10 --------
nome = str(input("qual é o seu nome? : ")).title()
if nome == "Guanabara":
    print("que beleza esse nome ai")
else:
    print("nao gostei do seu nome... tente na proxima")
print("bom dia ai {}".format(nome))

n1 = float(input("digite a primeira nota : "))
n2 = float(input("digite a segunda nota : "))
m = (n1 + n2) / 2
print("a sua média foi {:.1f}".format(m))
if m >= 6.0:
    print("parabens amigao passo de ano")
else:
    print("vai repeti de ano ein kk")

# desafio 028
from random import randint
escolhapc = int(randint(0,5))
escolha = int(input("digite um número inteiro de 0 a 5 : "))
if escolha == escolhapc:
    print("parabens vc e um genio")
else:
    print("sinto muito mas vc errou")
    print("o número aleatório foi {}".format(escolhapc))

# desafio 029
v = int(input("qual a velocidade do carro, em km/h? : "))
if v > 80:
    multa = (v - 80) * 7
    print(f"vc foi multado, a multa total é de {multa} reais")
else:
    print("vc esta de acordo com as leis de transito")

# desafio 030
inteiro = int(input("digite um numero inteiro : "))
if inteiro % 2 == 0:                                    # MOD OPERADOR
    print("o número {} é par".format(inteiro))
else:
    print("o número {} é ímpar".format(inteiro))

# desafio 031
distancia = int(input("qual a distancia da viagem ? "))
if distancia <= 200:
    valor = distancia * 0.50
    print(f"o valor da passagem é {valor}")
else:
    valor2 = distancia * 0.45
    print(f"o valor da passagem é {valor2}")

# desafio 032
ano = int(input("digite um ano qualquer : "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"o ano {ano} é bissexto")
else:
    print(f"o ano {ano} não é bissexto")

# desafio 033
n1 = float(input("digite um numero : "))
n2 = float(input("digite outro : "))
n3 = float(input("digite outro : "))
if n1 > n2 and n1 > n3:
    print(f"o número {n1} é o maior")
if n2 > n1 and n2 > n3:
    print(f"o número {n2} é o maior")
if n3 > n1 and n3 > n2:
    print(f"o número {n3} é o maior")
if n1 < n2 and n1 < n3:
    print(f"o número {n1} é o menor")
if n2 < n1 and n2 < n3:
    print(f"o número {n2} é o menor")
if n3 < n1 and n3 < n2:
    print(f"o número {n3} é o menor")

# desafio 034                                                   salario - 100        10salario = 100x
salario = float(input("qual é o salário do funcionário? : "))    # x    - 10            x = 10salario / 100
if salario > 1250:
    aumento = (salario * 110) / 100
    print("o salário, com aumento de 10%,é igual a {:.2f}".format(aumento))
else:
    aumento2 = (salario * 115) / 100
    print("o salário, com aumento de 15%,é igual a {:.2f}".format(aumento2))

# desafio 035
r1 = float(input("digite o comprimento da primeira reta : "))
r2 = float(input("digite o comprimento da segunda reta : "))
r3 = float(input("digite o comprimento da terceira reta : "))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print("é possível formar um triângulo")
else:
    print("não é possível formar um triângulo")

    






















































