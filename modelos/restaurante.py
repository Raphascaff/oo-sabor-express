from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome: str, categoria: str): # selt -> Referência da instância
        self._nome = nome
        self._categoria = categoria
        self.validar_restaurante()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # Adiciona o restaurante no próprio restaurante.

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def validar_restaurante(self):
        variaveis = [self._nome, self._categoria]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError("Nome e categoria devem ser strings")
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.title().ljust(25)} | {restaurante._categoria.upper().ljust(25)} | ' +
                  f'{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.status}')


    @property
    def status(self):
        return '✅' if self._status else '❌'
    
    def ativa_restaurante(self):
        self._status = not self._status 
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qnt_notas = len(self._avaliacao)
        media = soma_das_notas / qnt_notas
        return media.__round__(1)