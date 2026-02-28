import random

Dado_u = input("qual é o tipo de dado? ")

if "d" in Dado_u:
    partes_do_dado = Dado_u.split("d") 
else:
    print("Valor incorreto nos dados")

quantidade_dados = int(partes_do_dado[0])
faces_dados = int(partes_do_dado[1])

#Verificar se o numero é menor que 0 e não ser numero decimal, para os dois inputs dos usuários
if quantidade_dados > 0 and quantidade_dados % 1 == 0:
    Dados = quantidade_dados
else:
    print("Valor incorreto nos dados")

if faces_dados > 0 and faces_dados % 1 == 0:
    Faces = faces_dados
else:
    print("Valor incorreto nos dados")

for dado in range(Dados):
    Rolar = random.randint(1, Faces)
    print(Rolar)





