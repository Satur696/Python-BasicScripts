print("\t\tInformática - 1º Ano")
print("\t\t    Desafio - Q7\n")

try:
    inteiro = int(input("Digite o valor de i:"))
    if inteiro<0:
        print("O valor de i não pode ser menor que 0")
        exit("Saindo...")
    
except:
    print("Erro no Sistema!\nMotivo: O valor de 'i' não pode ser uma String")
    exit("Saindo...")

try:
    a = float(input("Digite o valor de a:"))
except:
    print("Erro no Sistema!\nMotivo: O valor de 'a' não pode ser uma String")
    exit("Saindo...")
try:
    b  = float(input("Digite o valor de b:"))
except:
    print("Erro no Sistema!\nMotivo: O valor de 'b' não pode ser uma String")
    exit("Saindo...")
try:
    c = float(input("Digite o valor de c:"))
except:
    print("Erro no Sistema!\nMotivo: O valor de 'c' não pode ser uma String")
    exit("\nSaindo...")

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
