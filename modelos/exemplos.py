#### ----- Exercício aula 2----- ####

class Musica:
     def __init__(self, nome:str, artista:str, duracao:int):
        variaveis = [nome, artista]
        if not all(isinstance(var, str) for var in variaveis):
            raise TypeError(f'Nome e Artista devem ser strings')
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

### ---- Exemplo aula 3 ---- ###

class Contador:
    '''
    Classe que representa um contador.
    A instância mantém um contador específico, enquanto um contador global é compartilhado por todas as instâncias.
    '''

    contador_global = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f'Contador: {self.valor}'

    def incrementar(self):
        self.valor += 1

    @classmethod
    def zerar_contador_global(cls):
        cls.contador_global = 0
        return 'Contador global foi zerado.'

### ---- Exercício aula 3 ---- ###

class Pessoa:


    def __init__(self, nome:str, idade:int, profissao:str):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()

    def __str__(self):
        return f' Nome: {self.nome} \n Idade: {self.idade} \n Profisão: {self.profissao}'
    
    def aumenta_idade(self):
        self.idade += 1
        return f'{self.idade}'
    
    @property
    def saudacao(self):
        return f'Parabéns por ser {self.profissao}!'
    
### ---- End ---- ###