i = 0
j = 0
acumulador = 0
notas = []
while i<4:
    notas.append(float(input("Digite a nota: ")))
    i +=1
#media = (notas[0]+notas[1]+notas[2]+notas[3])/i
while j<4:
    acumulador = acumulador + notas[j]
    j+=1

media = acumulador/j

if media >7:
    print("Parabens! Sua média é: ", media, "você passou de ano")

elif 7 > media > 5.5:
    print("Você esta de recuperação, sua média é: ", media)

else:
    print("Você esta reprovado :(. Sua média é: ", media)
