print("\t\t  Informática - 1° Ano")
print()
print("Questão 1. Faça uma calculadora onde o usuário escolhe que deseja realizar, caso o usuário escolha. (Utilize o if-elif-else).")
print()
e1 = float(input("Escolha um operador para calcular:    "))
e2 = float(input("Escolha outro operador para calcular:    "))
e3 = float(input("Escolha:\n1. Para somar\n2. Para subtrair\n3. Para multiplicar\n4. Para dividir\n5. Para exponenciação\n6. Para divir somente a parte inteira\nR: "))

if e3==1:
    re1=e1+e2
    print("Resultado da Soma:", re1)

elif e3==2:
    re1=e1-e2
    print("Resultado da Subtração:", re1)

elif e3==3:
    re1=e1*e2
    print("Resultado da Multiplicação:", re1)

elif e3==4:
    re1=e1/e2
    print("Resultado da Divisão:", re1)

elif e3==5:
    re1=e1**e2
    print("Resultado da Exponenciação:", re1)

elif e3==6:
    re1=e1//e2
    print("Resultado da Divisão c/ Inteiro:", re1)

else:
    print("Erro no Sistema!")

print("\nQuestão 2. Faça um programa que verifique (Usando If e Else) se uma letra digitada é vogal ou consoante.")
print()

le1 = str(input("Digite a letra:"))

if le1=='a':
    re="Vogal"

elif le1=='A':
    re="Vogal"

elif le1=='b':
    re="Consoante"

elif le1=='B':
    re="Consoante"

elif le1=='c':
    re="Consoante"

elif le1=='C':
    re="Consoante"

elif le1=='d':
    re="Consoante"

elif le1=='D':
    re="Consoante"

elif le1=='e':
    re="Vogal"

elif le1=='E':
    re="Vogal"

elif le1=='F':
    re="Consoante"

elif le1=='f':
    re="Consoante"

elif le1=='g':
    re="Consoante"

elif le1=='G':
    re="Consoante"

elif le1=='H':
    re="Consoante"

elif le1=='h':
    re="Consoante"

elif le1=='i':
    re="Vogal"

elif le1=='I':
    re="Vogal"

elif le1=='j':
    re="Consoante"

elif le1=='J':
    re="Consoante"

elif le1=='K':
    re="Consoante" 

elif le1=='k':
    re="Consoante"

elif le1=='l':
    re="Consoante"

elif le1=='L':
    re="Consoante"

elif le1=='m':
    re="Consoante"

elif le1=='M':
    re="Consoante"

elif le1=='n':
    re="Consoante"

elif le1=='N':
    re="Consoante"

elif le1=='o':
    re="Vogal"

elif le1=='O':
    re="Vogal"

elif le1=='p':
    re="Consoante"

elif le1=="P":
    re="Consoante"
    
elif le1=='q':
    re="Consoante"

elif le1=='Q':
    re="Consoante"

elif le1=='r':
    re="Consoante"

elif le1=='R':
    re="Consoante"

elif le1=='s':
    re="Consoante"

elif le1=='S':
    re="Consoante"

elif le1=='t':
    re="Consoante"

elif le1=='T':
    re="Consoante"

elif le1=='u':
    re="Vogal"

elif le1=='U':
    re="Vogal"

elif le1=='v':
    re="Consoante"

elif le1=='V':
    re="Consoante"

elif le1=='w':
    re="Consoante"

elif le1=='W':
    re="Consoante"

elif le1=='x':
    re="Consoante"

elif le1=='X':
    re="Consoante"  

elif le1=='y':
    re="Consoante"

elif le1=='Y':
    re="Consoante"

elif le1=='z':
    re="Consoante"

elif le1=='Z':
    re="Consoante"

else: 
    re="Isso não é uma letra"

print(re)

print("\nQuestão 3. Faça um programa que leia três números, verifique (usando if e else), e mostre o maior deles.")
print()
num1 = float(input("Digite o primeiro número:  "))
num2 = float(input("Digite o segundo número:   "))
num3 = float(input("Digite o terceiro número:  "))

if num1>=num2 and num1>=num3:
    res="O maior número é:", num1

elif num2>=num1 and num2>=num3:
    res="O maior número é:", num2

elif num3>=num1 and num3>=num1:
    res="O maior número é:", num3

else:
    res="Erro no Sistema!"

print(res)

print("\nQuestão 4. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.")
print()

e_num = float(input("Digite um Número:"))

if e_num<0:
    fale="Número Negativo"

elif e_num>0:
    fale="Número Positivo"

elif e_num==0:
    fale="Neutro"

else:
    fale="Isso não é um número"

print("Estado:", fale)

print("\nQuestão 5. Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem 'Bom dia!' ou 'Boa noite!' ou 'Valor inválido', conforme o caso. ")

turn = str(input("Em que turno você estuda?\nM: Matutino\nV: Vespertino\nN: Noturno\nR: "))

if turn=="M":
    diga = "Bom dia!"

elif turn=="m":
    diga = "Bom dia!"

elif turn=="V":
    diga = "Boa tarde!"

elif turn=="v":
    diga = "Boa tarde!"

elif turn=="N":
    diga = "Boa noite!"

elif turn=="n":
    diga = "Boa noite!"

else:
    diga = "Valor inválido =)"

print(diga)

print("\nQuestão 6. Faça um programa que o usuário informe o salário recebido e o total gasto. Deverá ser exibido na tela 'Gastos dentro do orçamento' caso o valor gasto não ultrapasse o valor do salário e 'Orçamento estourado' se o valor ultrapassar o valor do salário.")

salario = float(input("Salário recebido: R$"))
gasto = float(input("Total de gastos: R$"))
conta_secreta = salario-gasto

print("O Salário Final é:", conta_secreta)
if conta_secreta>0:
    final = "Gastos dentro do orçamento"

elif conta_secreta<0:
    final = "Orçamento estourado"
    
elif conta_secreta==0:
    final = "Orçameto estourado"

else:
    "Erro no Sistema!"

print("Situação:", final)