#FASE 9 ------------------------
frase = "guanabara"      # fatiamento de 1 índice de um total de 8 índices
# FATIAMENTO -------
print(frase[5])          # do primeiro índice digitado até o segundo índice digitado menos 1
print(frase[1:6])
print(frase[1:9])
print(frase[1:4:2])      # esse dois no final serve pra pular de dois em dois índices
print(frase[:6])         # começo ate o 6
print(frase[1:])         # 1 até o final
print(frase[2::2])       # 2 até o final, de 2 em 2 índices
# ANALISE -----------
print(len(frase))        # quantos índices tem uma string
print(frase.count("a",0,6))  # comando pra contar quantos caracteres "a" tem na string com fatiamento de 0 até 5
print(frase.find("bara"))    # encontrar o índice em que começa os caracteres procurados
print(frase.find("apagador"))    # - 1  = nao existe
print("bara" in frase)
# TRANSFORMAÇÃO ---
print(frase.replace("ara","kkkkkkkkkk")) # substitui uma string por outra
print(frase.upper())  # deixa tudo em maiusculo
print(frase.lower())  # deixa tudo em minusculo
print(frase.capitalize()) # deixa tudo em minusculo porem a primeira letra em maiusculo
print(frase.title())  # deixa a primeira letra de cada palavra em maiusculo
print(frase.strip())  # remove todos os espaços inuteis no começo e final de uma string
print(frase.rstrip()) # remove os espaços do final
print(frase.lstrip()) # remove os espaços do começo
# DIVISÃO----
print(frase.split()) # separa todas as palavras em novos indices,e cada palavra nova gerada começa a partir de 0
# JUNÇÃO ---
print("algo".join(frase)) # substitui os espaços de uma string por uma string digitada antes do comando .join















