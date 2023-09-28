#Desenvolver um programa em python que solicite ao usuario dois numeros inteiros, base e expoente,
#calcule e mostre o primeiro numero elevao ao segundo numero. Não pode altilizar a função de potencia da linguagem.
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

result = num1*num1
for i in range(1,num2):
    result = result*num1
        
print(result)