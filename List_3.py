#Questão 1

d1 = float(input("Quilômetros Percoridos:   "))
t1 = float(input("\nHora:  "))
v = d1/t1
print("\nA velocidade média é: ", v)

if v < 100:
    r="Carro devagar"

elif v>100 and v<140:
    r="Carro com velocidade mediana"

elif v>140:
    r="Carro com alta velocidade"

print("Status:", r)

#Questão 2

l1 = float(input("L1:"))
l2 = float(input("\nL2:"))
n1 = (l1+l2)/2
print("\nNota 1:", n1)
p1 = float(input("\nP1:"))
l3 = float(input("\nL3:"))
l4 = float(input("\nL4:"))
n2 = (p1+l3+l4)/3
print("\nNota 2:", n2)
p2 = float(input("\nP2:"))
l5 = float(input("\nL5:"))
n3 = (p2+l5)/2
print("\nNota 3:", n3)
p3 = float(input("\nP3:"))
l6 = float(input("\nL6:"))
l7 = float(input("\nL7:"))
n4 = (p3+l6+l7)/3
print("\nNota 4:", n4)
print()
media = (n1+n2+n3+n4)/4
print("A média é:", media)

if media < 4:
    m="Reprovado"

elif media>4 and media<7:
    m="Recuperação"

elif media>7:
    m="Aprovado"

print("Resultado Final:", m)

#Questão 3

salario = float(input("\nSalário do Colaborador: R$"))
imposto = salario*0.15
print("Desconto do imposto: R$", imposto, "\n")
inss = salario*0.10
print("Desconto do inss: R$", inss, "\n")
final = imposto+inss
vlf = salario-final
print("Salário Final: R$", vlf, "\n")

if vlf < 1000:
    receita='Colaborador receberá cesta básica e gratificação.'

elif vlf > 1000 and vlf < 2000:
    receita='Colaborador receberá apenas gratificação.'

elif vlf > 2000:
    receita='Colaborador receberá apenas a metade da gratificação.'

print(receita)

#Questão 4
metro = float(input("\nDigite o Valor dos Metros: "))
escolha = int(input("Escolha para Transformar: \n1: em Quilômetros \n2: em Centímetros \n3: em Milímetros \nR:"))
print()
if escolha==1:
    transformacao=metro/1000
    print("Quilômetros:", transformacao)

elif escolha==2:
    transformacao=metro*100
    print("Centímetros:", transformacao)

elif escolha==3:
    transformacao=metro*1000
    print("Milímetros:", transformacao)

else: 
    print("Erro no sistema!")

#Questão 5
#Um garoto está jogando um jogo onde ele quer saber se um número é verdadeiro ou falso.
#Se este número ele for maior que 10, ele é falso.
#Porém se este número for menor que 10, ele é verdadeiro.
#Se este número for menor que 0, ele é um número especial.

escolha_numero = float(input("\nEscolha o número entre 0 e 10:"))

if escolha_numero > 10:
    print("Este número é falso.")

elif 0 < escolha_numero:
    print("Este número é verdadeiro.")

else:
    print('Este número é especial.')