def imprimir_dados():
    print("miau")

#imprimir_dados()

def somar_numero(n1,n2):
    soma = n1 +n2
    return soma

resultado = somar_numero(10,10)
#print(resultado)

def titulos_copa(pais,*miau):
   # print(pais)
    for titulos in miau:
        print()
#print(titulos)

titulos_copa("Brasil", "1994", "2002")

