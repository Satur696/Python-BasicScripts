#Questão 1 
d1 = float(input("Quilômetros Percoridos:   "))
t1 = float(input("\nHora:  "))
v = d1/t1
a = v/t1
print("\nA velocidade é: ", v)
print("\nA aceleração é:", a)

#Questão 2
l1 = float(input("L1:   "))
l2 = float(input("\nL2:   "))
n1 = l1+l2
print("\nNota 1:  ", n1)
p1 = float(input("\nP1:   "))
l3 = float(input("\nL3:   "))
l4 = float(input("\nL4:   "))
n2 = p1+l3+l4 
print("\nNota 2:  ", n2)
p2 = float(input("\nP2:   "))
l5 = float(input("\nL5:   "))
n3 = p2+l5
print("\nNota 3:  ", n3)
p3 = float(input("\nP2:   "))
l6 = float(input("\nL6:   "))
l7 = float(input("\nL7:   "))
n4 = p3+l6+l7
print("\nNota 4:  ", n4)
media = (n1+n2+n3+n4)/4
print("A média é:   ", media)

#Questão 3 
salario = float(input("\nSalário: R$"))
imposto = salario*0.15
print("Desconto do imposto: R$", imposto, "\n")
inss = salario*0.10
print("Desconto do INSS: R$", inss, "\n")
final = inss+imposto
print("Salário Final: R$", salario-final )

#Questão 4 
metro = float(input("\nMetro: "))
km = metro/1000
print("Quilômetros: ", km, "\n")
cent = metro*100
print("Centímetro: ", cent, "\n")
mili = metro*1000
print("Milímetro: ", mili)
