bandas = { 'titulo': 'teste', 'duracao': '2 horas'}
print(bandas['titulo'])

bandas['Author'] = "MIau"
print(bandas)

del bandas['Author']
print(bandas)