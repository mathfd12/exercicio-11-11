i = 0
j = 0
nome = []
quant = []
valor = []
while i < 10:

    nome.append(input("Digite o nome do produto: "))
    quant.append(int(input("Digite a  quantidade: ")))
    valor.append(float(input("Digite o valor do produto: ")))
    i += 1

print("Nota fiscal")

while j<10:
    valor[j] = quant[j]*valor[j]
    print("Produto: ", nome[j], "Quantidade: ", quant[j], "Valor: ", valor[j])
    j+=1



