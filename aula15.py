class Carro:
    # iniciando uma classe
    # se ta dentro de uma classe (o def) é metodo
    def __init__(self, proprietario, modelo, cor, placa, preco, marca):
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.preco = preco
        self.marca = marca

    def __str__(self):
        return f"Olá {self.proprietario}, seu carro é o {self.modelo} - {self.marca}"
    # O self ele faz uma ligação entre os metodos dessa classe, sendo desnecessario chamar novamente os atributos

meu_carro = Carro(
    proprietario = 'jose',
    modelo = 'Logan',
    cor = 'rosa',
    placa = 'LIXOO0945',
    preco = 10000,
    marca = 'miau'
    )
print(meu_carro)
