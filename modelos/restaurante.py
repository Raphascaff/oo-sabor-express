

class Restaurante:
    nome = ''
    categoria = ''
    status = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

print(vars(restaurante_praca))