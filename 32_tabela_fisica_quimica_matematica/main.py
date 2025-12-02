from utils.enum import Categoria, Matematica, Fisica, Quimica
from module.matematica.matematica import CalculoMatematica

def main():
    print("Bem-vindo ao programa de Tabela Física, Química e Matemática!")

    #categoria = int(input("Escolha uma categoria (1-Física, 2-Química, 3-Matemática): "))

    categoria = 3

    get_categoria = Categoria(categoria)

    print(f"Você escolheu a categoria: {get_categoria.value} - {get_categoria.name}")

    match get_categoria.value:
        case 1:
            sub_categoria = int(input(f"{Fisica.__members__}\nEscolha uma subcategoria: "))
            print(f"Você escolheu Física - {Fisica(sub_categoria).name}.")

        case 2:
            sub_categoria = int(input(f"{Quimica.__members__}\nEscolha uma subcategoria: "))
            print(f"Você escolheu Química - {Quimica(sub_categoria).name}.")

        case 3:
            # sub_categoria = int(input(f"{Matematica.__members__}\nEscolha uma subcategoria: "))
            sub_categoria = 19
            print(f"Você escolheu Matemática - {Matematica(sub_categoria).name}.")

            value = CalculoMatematica.service(Matematica(sub_categoria).name, 'area_quadrado')

        case _:
            print("Categoria inválida.")

    print(f"Resultado do cálculo: {value}")


if __name__ == "__main__":
    main()
