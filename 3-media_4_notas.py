n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4)/4

if media > 7:
    print("Parabens! Sua média é: ", media, "você passou de ano")

if 7 > media > 5.5:
    print("Você esta de recuperação, sua média é: ", media)

else:
    print("Você esta reprovado :(. Sua média é: ", media)
