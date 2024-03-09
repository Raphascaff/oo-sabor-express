class Avaliacao:
    def __init__(self, cliente: str, nota: int):
        self._cliente = cliente
        self._nota = nota
        self.validar_cliente_e_nota()

    def validar_cliente_e_nota(self):
        if not isinstance(self._cliente, str):
            raise TypeError("O cliente deve ser uma string.")
        if not isinstance(self._nota, int):
            raise TypeError("A nota deve ser um número inteiro.")
        if not (0 <= self._nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")