pessoa = {
    'nome':'Anna',
    'idade':16,
    'email':'annabserikyaku@gmail.com'
}
#print("Ola ", pessoa["nome"], "bem-vindo ao sistema com o email", pessoa["email"])

pessoa['Esta trabalhando?'] = "sim"
print(pessoa)

pessoa.update({
    'Miau':'miau?'
})
print(pessoa)

