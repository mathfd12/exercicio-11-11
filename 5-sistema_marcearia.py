resp = input("Tem mercadoria no carrinho? Responder com s ou n: ")
while resp == "s":
    nome = input("Digite o nome da mercadoria: ")
    quant = int(input("Digite a quantidade da mercadoria: "))
    valor = float(input("Digite o valor da mercadoria: "))

    valor = quant*valor

    print("Quantidade: ", quant,
          "\n Nome do produto: ", nome,
          "\n Valor total: ", valor)

    resp = input("Tem mercadoria no carrinho? Responder com s ou n: ")