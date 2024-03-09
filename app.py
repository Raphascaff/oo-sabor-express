from modelos.restaurante import Restaurante


restaurante_praca = Restaurante(nome='Praça', categoria='Gourmet')
restaurante_praca.receber_avaliacao('Raphael', 10)
restaurante_praca.receber_avaliacao('Amanda', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()