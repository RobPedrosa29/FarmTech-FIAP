########## IMPORTS ##########
from main import (
        selecionar_cultura,
        ler_float
)

from plantio_cana import (
        criar_parcela,
        mostrar_parcela,
        atualizar_parcela,
        deletar_parcela
)

from plantio_laranja import (
        inserir_dados,
        exibir_dados,
        atualizar_dados,
        deletar_dados
)

from export import exportar_dados





########## MENU ##########
distancia_titulo = 50
titulo = "ＦＡＲＭ　ＴＥＣＨ"


print("\n" + titulo.center(distancia_titulo, " ") + "\n")

print(f"""\nBem-vindo(a) à Farm Tech!""")
cultura = selecionar_cultura()

while True:
        opção = input("""\nO que deseja?                  
1- Inserir dados
2- Mostrar dados
3- Atualizar dados
4- Deletar dados
5- Exportar dados para análise           
6- Selecionar outra cultura
7- Sair
                                          
---Resposta: """)
        
        if cultura == "Cana-de-açucar":
                match opção:
                        case "1" | "um" | "inserir":
                                criar_parcela()
                        case "2" | "dois" | "mostrar dados":
                                mostrar_parcela()
                        case "3" | "três" | "tres" | "atualizar":
                                atualizar_parcela()
                        case "4" | "quatro" | "deletar" | "excluir":
                                deletar_parcela()
                        case "5" | "exportar":
                                exportar_dados()
                        case "6" | "seis" | "selecionar cultura" | "outra cultura":
                                cultura = selecionar_cultura()
                        case "7" | "sete" | "sair":
                                print("\nEncerrando o programa!")
                                break
                        case _:
                                print("\nOpção inválida, tente novamente.")

        elif cultura == "Laranja":
                match opção:
                        case "1" | "um" | "inserir":
                                inserir_dados()
                        case "2" | "dois" | "mostrar dados":
                                exibir_dados()
                        case "3" | "três" | "tres" | "atualizar":
                                atualizar_dados()
                        case "4" | "quatro" | "deletar" | "excluir":
                                deletar_dados()
                        case "5" | "exportar":
                                exportar_dados()
                        case "6" | "seis" | "selecionar cultura" | "outra cultura":
                                cultura = selecionar_cultura()
                        case "7" | "sete" | "sair":
                                print("\nEncerrando o programa!")
                                break
                        case _:
                                print("\nOpção inválida, tente novamente.")
        else:
                print("\nCultura indisponível, tente novamente.")