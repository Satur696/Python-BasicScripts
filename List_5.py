print("\t\t     Informática - 1º Ano")

print("Questão 1.")

try:
    numero_1 = int(input("Digite o primeiro número (inteiro):"))
    numero_1 == int and numero_1 >= 0
    if numero_1 < 0:
        while numero_1 < 0:
            print("Erro! O número não pode ser menor que 0 (inteiro).")
            numero_1 = int(input("\nDigite novamente o número:"))
            if numero_1 < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

try:
    numero_2 = int(input("Digite o segundo número (inteiro):"))
    numero_2 == int and numero_2 >= 0
    if numero_2 < 0:
        while numero_2 < 0:
            print("Erro! O número não pode ser menor que 0 (inteiro).")
            numero_2 = int(input("\nDigite novamente o número:"))
            if numero_2 < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

try:
    numero_real = float(input("Digite o terceiro número (real):"))
    numero_real == float and numero_real != str
except ValueError:
    print("ERRO!")
    exit("Saindo...")

print("a)")
final = (numero_1*2) * (numero_2/2)
print("R=", final)

print("b)")
soma = (numero_1*3)+numero_real
print("R=", soma)

print("c)")
cubo = numero_real**3
print("R=", cubo)

print("\nQuestão 2.")
print()

try:
    peso = float(input("Digite o Peso dos Peixes:"))
    peso == float and peso >= 0
    if peso < 0:
        while peso < 0:
            print("Erro! O peso não pode ser negativo.")
            peso = float(input("Digite o Peso dos Peixes:"))
            if peso < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

multa_peixe = 4
print("Excesso:", peso-50, "KG")

if peso > 50:
    pesca = peso*multa_peixe
    print("O peso ultrapassou o limite (50KG), você pagará R$", pesca)
    print("Peso dos peixes:", peso, "KG")

if peso <= 50:
    print("O peso não ultrapassou o limite (50KG), não pagará multa.")
    print("Peso dos peixes:", peso, "KG")

print("\nQuestão 3.")
try:
    mb = float(input("Digite o tamanho do arquivo (em MB):"))
    if mb < 0:
        while mb < 0:
            print("Erro! O valor do arquivo não pode ser negativo.")
            mb = float(input("Digite o tamanho do arquivo novamente (em MB):"))
            if mb < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

try:
    link = float(input("Digite a velocidade de um link da internet (em Mbps):"))
    if link < 0:
        while link < 0:
            print("Erro! O valor da velocidade não pode ser negativo.")
            link = float(input("Digite a velocidade de um link da internet novamente (em Mbps):"))
            if link < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

tempo_aproximado = mb/(link/8)
segundos = tempo_aproximado
minutos = segundos//60
print("O tempo aproximado de download desse arquivo (em minutos):", minutos, "minutos")
print("Em segundos:", segundos, "segundos")
print("Tamanho do arquivo:", mb, "MB")
print("Velocidade da internet:", link, "Mbps")

print("\nQuestão 4.")

try:
    f = float(input("Digite a temperatura em graus Fahrenheit (ºF):"))
except ValueError:
    print("ERRO!")
    exit("Saindo...")

c = 5*((f-32)//9)

print("A temperatura em graus Celsius (ºC):", c)

print("\nQuestão 5.")

try:
    altura = float(input("Digite sua altura:"))
    if altura < 0:
        while altura < 0:
            print("Erro! a altura não pode ser negativa.")
            altura = float(input("Digite sua altura novamente:"))
            if altura < 0:
                continue
except ValueError:
    print("ERRO!")
    exit("Saindo...")

peso_ideal =  (72.7*altura) - 58
print("Seu peso ideal é:", peso_ideal, "KG")