############### PSEUDOCÓDIGO ###############

#criar loop de menu:
#---ENTRADA
#   # pedir dados da parcela(área de plantio da cultura), cultura, geometria, insumo
#   # armazenar nos vetores correspondentes
#---SAÍDA DE DADOS
#   # imprimir todos os dados com info das parcelas
#---ATUALIZAR DADOS
#   # escolher índice/parcela e atualizar
#   # permitir alteração dos valores
#---DELEÇÃO
#   # escolher índice/parcela e deletar
#   # remover os dados em todos os vetores
#---SAIR DO PROGRAMd
#   # encerrar o loop

#############################################

# MENU:
from main import(

        criar_parcela,
        mostrar_parcela,
        atualizar_parcela,
        deletar_parcela

)


while True:
        print("""
                ＦＡＲＭ　ＴＥＣＨ
        """)

        option = input("""\nBem-vindo(a) à Farm Tech! Selecione a opção desejada:              
1- Inserir dados
2- Mostrar dados
3- Atualizar dados
4- Deletar dados
5- Sair
                 
Resposta: """)


# FALTA: chamar as funções
        match option:
                case "1" | "um" | "inserir":
                        criar_parcela()
                case "2" | "dois" | "mostrar dados":
                        mostrar_parcela()
                case "3" | "três" | "tres" | "atualizar":
                        atualizar_parcela()
                case "4" | "quatro" | "deletar" | "excluir":
                        deletar_parcela()
                case "5" | "cinco" | "sair":
                        print("\nEncerrando o programa!")
                        break
