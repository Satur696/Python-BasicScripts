print("\t\tInformática - 1º Ano")
print("\t\t    Desafio - Q7\n")

try:
    inteiro = int(input("Digite o valor de i:"))
except:
    print("Erro no Sistema!")
try:
    a = float(input("Digite o valor de a:"))
except:
    print("Erro no Sistema!")
try:
    b  = float(input("Digite o valor de b:"))
except:
    print("Erro no Sistema!")
try:
    c = float(input("Digite o valor de c:"))
except:
    print("Erro no Sistema!")

if inteiro==2:
    calculo = (a+b+c)/3

elif inteiro==4:
    calculo = (a+b+c)/3

elif inteiro==6:
    calculo = (a+b+c)/3

elif inteiro==8:
    calculo = (a+b+c)/3

elif inteiro==10:
    calculo = (a+b+c)/3

elif inteiro>10:
    calculo = (2*a+3*b+4*c)/9

else:
    calculo = "Erro no sistema!"

print("Media:", calculo)