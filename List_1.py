#XXXXXXXXXX - Informática 1º Ano

#Lista de Exercícios 1 - Python

#Questão 1

print("Nome: XXX\n\tIdade: XX\n\t\tSigno: XX\n\t\t\tAniversário: XX\n\t\tTime: XXX\n\tCidade: XXXXX\nSonho: XXXXXX")

print()
#Questão 2

nome= "Paulo Roberto"
salario= 1000
vendas= 500
final= 1000+500*0.15
print("Nome do vendedor:",nome,"\nSalário:R$",salario,"\nTotal de Vendas:",vendas,"\nSalário Final:R$",final)

print()
#Questão 3

nome= "João Paulo"
nota_1= 8.0
nota_2= 9.0
nota_3= 7.0
media= (8+9+7)//3
print("Nome do Aluno:",nome,"\nNota 1:",nota_1,"\nNota 2:",nota_2,"\nNota 3:",nota_3,"\nMédia:",media)

print()
#Questão 4

nome= "Conversão do Real pro Dólar"
real= 500
cotacao= 5.65
dolar= 500/5.65
print(nome,"\nReal:R$",real,"\nCotação Atual:R$",cotacao,"\nDólar:U$",dolar)

print()
#Questão 5

conta= "Caixa Poupança"
saldo_anterior= 2000
deposito= 250
saldo_conta= 2250
rendimento= 2250*0.007
saldo_total= 2250+15.75
print(conta,"\nSaldo Anterior:R$",saldo_anterior,"\nDepositado:+R$",deposito,"\nSaldo da Conta:R$",saldo_conta,"\nRendimento:+R$",rendimento,"\nSaldo Total:R$",saldo_total)

#Questão 6

import sys
print("\nVersão Python")
print(sys.version)
print("\nInformação da Versão")
print(sys.version_info)

print()
#Questão 7

raio= 3
pi= 3.14
area= pi*(raio**2)
comprimento= 2*pi*raio
print("Raio:",raio,"M","\nPi:",pi,"M","\nÁrea:",area,"M","\nComprimento da circuferência:",comprimento,"M")

#Questão 8 

z= "XXXXXXXXXXXXX"
print("\nNome:",z)
print(z[11]+z[10]+z[5]+z[4])
print(z[3]+z[4]+z[8]+z[4])
print(z[8]+z[10]+z[11]+z[12])
