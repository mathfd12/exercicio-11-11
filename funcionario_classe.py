class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f"Olá {self.nome}, seu cadastro foi feito com sucesso"

    def aumentar_salario(self, aumento):
        return self.salario + aumento

fun = Funcionario(
    nome = 'Carlos',
    email = 'ajnsdjsbjda',
    rg = '23231',
    idade = 21,
    salario = 2000
)

print(fun)
print(fun.aumentar_salario(15)) # usar ponto para chamar metodo 'individual'