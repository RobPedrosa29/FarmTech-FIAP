# ==================== #
# Estruturação do menu #
# ==================== #

import subprocess
import os
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
from clima_api import obter_clima


########## FUNÇÃO PARA CHAMAR O SCRIPT R ##########
def analisar_dados():
    caminho_r = os.path.join(os.path.dirname(os.path.dirname(__file__)), "R", "analise.R")
    
    if not os.path.exists(caminho_r):
        print(f"\n[Erro] Script {caminho_r} não encontrado!")
        return

    try:
        # Executa o script R e mostra a saída no terminal
        subprocess.run(["Rscript", caminho_r], check=True)
    except FileNotFoundError:
        print("\n[Erro] Rscript não encontrado. Certifique-se de que o R esteja instalado e no PATH.")
    except subprocess.CalledProcessError as e:
        print("\n[Erro] Ocorreu um problema ao executar o script R:", e)


########## MENU ##########
distancia_titulo = 30
titulo = "ＦＡＲＭ　ＴＥＣＨ"

print("\n" + titulo.center(distancia_titulo, " ") + "\n")
print(f"\nBem-vindo(a) à Farm Tech!")
cultura = selecionar_cultura()

while True:
        opção = input("""\nO que deseja?

--- DADOS ---                                 
1- Inserir dados
2- Mostrar dados
3- Atualizar dados
4- Deletar dados
5- Exportar dados para análise
                  
--- OUTROS ---            
6- Selecionar outra cultura
7- Exibir clima
8- Analisar CSVs
9- Sair
                                 
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
                        case "7" | "sete" | "clima":
                                cidade = input("Digite a cidade (ex: São Paulo, SP): ")
                                obter_clima(cidade)
                        case "8" | "oito" | "analisar csvs":
                                analisar_dados()
                        case "9" | "nove" | "sair":
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
                        case "7" | "sete" | "clima":
                                cidade = input("Digite a cidade ou coordenadas (ex: São Paulo ou -22.59,-47.90): ")
                                obter_clima(cidade)
                        case "8" | "oito" | "analisar csvs":
                                analisar_dados()
                        case "9" | "nove" | "sair":
                                print("\nEncerrando o programa!")
                                break 
                        case _:
                                print("\nOpção inválida, tente novamente.")
        else:
               print("\nCultura indisponível, tente novamente.")
