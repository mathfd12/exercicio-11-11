def inss(salario):
    INSS = salario* 0.09
    salario -=INSS
    print("Seu salário descontando o INSS: ", salario)

def vt(salario):
    vale = salario*0.03
    salario -=vale
    print("Seu salário descontando o Vale Transporte: ", salario)

def plan_s(salario):
    ps = 347*0.15
    salario -=ps
    print("Seu salario descontando o Plano de Saúde: ", salario)

def val_li(salario):
    vliquido = salario - (salario* 0.09 + salario*0.03 + 347*0.15)
    print("Seu salário líquido: ", vliquido)

sal = float(input("Digite seu salário: "))

inss(sal)
vt(sal)
plan_s(sal)
val_li(sal)

