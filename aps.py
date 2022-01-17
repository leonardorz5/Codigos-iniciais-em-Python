import math
 
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ", x+y)
 
def subtrair():
    x = float(input("primeiro numero: "))
    y = float(input("segundo numero: "))
    print("subtrção : ", x-y)
 
def raiz():
    x = float(input("primeiro numero: "))
    print("raiz: ", math.sqrt(x))
 
def divisão():
    x = float(input("primeiro numero: "))
    y= float(input("segundo programa: "))
    print("divisão: ", x/y)
 
def fatorial():
    x = float(input("digite o numero: "))
    print("fatorial: ", math.factorial(x))
def coseno():
    x = float(input("digite o numero para tirar o coseno: "))
    print("o coseno é: ", math.acos(x))
def seno():
    x = float(input("digite o numero para tirar o seno: "))
    print("o seno é: ", math.asin(x))
    
opcao=1
while opcao !=0:
               
    print("0. sair")
    print("1. soma")
    print("2. subtrair")
    print("3. divisão")
    print("4. raiz")
    print("5. fatorial")
    print("6. coseno")
    print("7. seno")
    opcao = int(input("Opção: "))
 
   
 
    if(opcao==1):
        soma()
    if(opcao==2):   
        subtrair()
    if(opcao==3):   
        divisão()
    if(opcao==4):    
        raiz()
    if(opcao==5):    
        fatorial()
    if(opcao==6):
        coseno()
    if(opcao==7):
        seno()
    if (opcao==0):
        print("fim do programa")
