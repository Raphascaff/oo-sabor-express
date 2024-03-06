from modelos.restaurante import Restaurante


restaurante_praca = Restaurante(nome='Praça', categoria='Gourmet')
restaurante_mexicano = Restaurante(nome='Mexicolindo', categoria='Mexicano').ativa_restaurante()
restaurante_japones = Restaurante(nome='JapaGuei', categoria='Japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()