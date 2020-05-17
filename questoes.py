algo = input("Qual é o seu nome?")
print("bem vindo,{:>80}!".format(algo))



n = float(input("digite um número : "))
n2 = float(input("digite outro número : "))
s = n + n2
print("a soma de {} e {} é {}".format(n,n2,s))
# lembrando que também da pra fazer usando ("f" e chaves)

c = input("digite qualquer coisa : ")
print(f"o tipo primitivo desse valor é {type(c)}")
print(f"possui letras? {c.isalpha()}")
print(f"tem número?{c.isnumeric()}")
print(f"tem letra maiúscula? {c.isupper()}")
print(f"tem letras ou números? {c.isalnum()}")

print("é capitalizado?",c.istitle())

















