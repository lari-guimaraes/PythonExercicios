import random
al1 = str(input('Digite o nome do aluno 1: '))
al2 = str(input('Digite o nome do aluno 2: '))
al3 = str(input('Digite o nome do aluno 3: '))
al4 = str(input('Digite o nome do aluno 4: '))
lista = [al1,al2,al3,al4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

