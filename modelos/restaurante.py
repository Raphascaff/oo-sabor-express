

class Restaurante:

    restaurantes = []

    def __init__(self, nome: str, categoria: str): # selt -> Referência da instância
        variaveis = [nome, categoria]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError("Nome e categoria devem ser strings")
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        Restaurante.restaurantes.append(self) # Adiciona o restaurante no próprio restaurante.

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.status}')


    @property
    def status(self):
        return '✅' if self._status else '❌'
    
    def ativa_restaurante(self):
        self._status = not self._status

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.ativa_restaurante()

Restaurante.listar_restaurantes()