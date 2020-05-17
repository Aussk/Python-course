# FASE 7 --------------
# desafio 005

x = int(input("digite um número que seja inteiro : "))
antecessor = x - 1
sucessor = x + 1

print("o antecessor de {} é {} e o seu sucessor é {}".format(x,antecessor,sucessor))

# desafio 006

y = int(input("digite um número inteiro : "))

d = 2 * y
t = 3 * y
raiz = y ** 0.5

print(f"o dobro de {y} é igual a {d},o triplo é igual a {t} \ne a raiz é {raiz} ")

# desafio 007

nota1 = float(input("digite a primeira nota do aluno : "))
nota2 = float(input("digite a segunda nota : "))
media = (nota1 + nota2) / 2
print(f"a média do aluno é : {media}")

# desafio 008

metro = float(input("digite um valor em metros : "))
centimetro = metro * 100
milimetro = metro * 1000
print(f"{metro} metros é igual a {centimetro} centímetros e {milimetro} milímetros")

# desafio 009

nqualquer = int(input("digite um número inteiro para mostrar sua tabuada : "))
um = nqualquer * 1  # eu nao faço ideia de como juntar tudo em uma variável então coloquei tudo separado
dois = nqualquer * 2
tres = nqualquer * 3
quatro = nqualquer * 4
cinco = nqualquer * 5
seis = nqualquer * 6
sete = nqualquer * 7
oito = nqualquer * 8
nove = nqualquer * 9
dez = nqualquer * 10

print(f"a tabuada de {nqualquer} é, respectivamente, {um},{dois},{tres},{quatro},{cinco}",end= "")
print(f", {seis},{sete},{oito},{nove},{dez}")

# desafio 010
# 1 dólar = 5,90 reais         5,98x = carteira
# x dólar = carteira
carteira = float(input("digite o valor em real dentro de sua carteira para saber quantos dólares pode comprar : "))
dolar = carteira / 5.90
print(f"você pode comprar o total de {dolar} dólares com {carteira} reais ")

#desafio 011
# 1 litro - 2m²                      area = 2m² * x
# x litros - area                     x = area / 2
largura =  float(input("digite a largura de uma parede, em metros : "))
altura = float(input("digite a altura da parede, em metros : "))
area = largura * altura
tinta = area / 2
print(f"a área de uma parede de {largura} metros de largura e {altura} metros de altura é igual a",end="")
print(f" {area} metros quadrados,e precisa de {tinta} litros de tinta para pintá-la")

# desafio 012
# preço - 100%                    preço . 95 = descontado . 100
# descontado - 95%                descontado = (preço . 95) / 100
preço = float(input("digite o preço do produto : "))
descontado = (preço * 95) / 100
print(f"o preço do produto com cinco por cento de desconto é igual a {descontado}")

# desafio 013
# salario - 100%                  salario * 115 = aumento * 100
# aumento - 115%                  aumento = (salario * 115) / 100
salario = float(input("digite o salário do funcionário : "))
aumento = (salario * 115) / 100
print(f"o novo salário, com 15 por cento de aumento, é igual a {aumento}")






































