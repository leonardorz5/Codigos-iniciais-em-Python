print('Bem-vindo a calculadora de salário da Tabajara Corp. digite abaixo o valor do seu salário para saber o reajuste')
seuSalario = float(input('digite o valor do seu salário para calcularmos o reajuste: ' ))
if (seuSalario <= 280):
    porcent= seuSalario * 0.2
    a= seuSalario + porcent
    print(f'seu salário após o aumento é de {a}')
    print(f'o valor do aumento foi de {20}%')
elif (seuSalario <=700):
    porcenta= seuSalario * 0.15
    b= seuSalario + porcenta
    print(f'seu salário após o aumento é de {b}')
    print(f'o valor do aumento foi de {15}%')
    
elif (seuSalario <=1500):
    porcentag= seuSalario * 0.01
    c= seuSalario + porcentag
    print(f'seu salário após o aumento é de {c}')
    print(f'o valor do aumento foi de {10}%')
elif (seuSalario >1500):
    porcentage= seuSalario * 0.05
    d= seuSalario + porcentage
    print(f'seu salário após o aumento é de {d}')
    print(f'o valor do aumento foi de {5}%')

