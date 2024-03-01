

class Restaurante:
    def __init__(self, nome: str, categoria: str): # selt -> Referência da instância
        variaveis = [nome, categoria]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError("Nome e categoria devem ser strings")
        self.nome = nome
        self.categoria = categoria
        self.status = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Gourmet')

print(restaurante_praca)