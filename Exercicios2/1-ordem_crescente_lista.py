quant = int(input("Quantos números quer ter na lista?"))
i = 0
cres = []
n1 = 0
n2 = 0

while i<quant:
    cres.append(int(input("Digite os valores: ")))
    i +=1

cres.sort() #crescente
#cres.sort(reverse = true) descrescente
print(cres)