

class Restaurante:

    restaurantes = []

    def __init__(self, nome: str, categoria: str): # selt -> Referência da instância
        variaveis = [nome, categoria]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError("Nome e categoria devem ser strings")
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self) # Adiciona o restaurante no próprio restaurante.

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.status}')

restaurante_praca = Restaurante('Praça', 'Gourmet')

Restaurante.listar_restaurantes()

#### ----- Exercício ----- ####

class Musica:
     def __init__(self, nome:str, artista:str, duracao:int):
        variaveis = [nome, artista]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError(f'Nome e Artista devem ser strings')
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
