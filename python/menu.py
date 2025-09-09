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


# FUNÇÕES:

def geometria_plantio():
        geometria_plantio = input("""Selecione abaixo o formato geométrico da área de plantio:
                1- Retângulo;
                2- Quadrado;
                3- Círculo;
                4- Triângulo;
                
                """).strip().lower()
        
        match geometria_plantio:
                case "1" | "um" | "retangulo" | "retângulo":
                        pass
                case "2" | "dois" | "quadrado":
                        pass
                case "3" | "tres" | "três" | "circulo" | "círculo":
                        pass
                case "4" | "quatro" | "triangulo" | "triângulo":
                        pass

def area_plantio():      
        area_plantio = input("""Digite o número de acordo com o desejado: 
                1- Informar área em metros quadrados;
                2- informar área em hectares;
                
                """).strip().lower()
        



# MENU:

print("""
              ＦＡＲＭ　ＴＥＣＨ
""")

option = input("""Bem-vindo à FarmTech! Selecione a opção desejada:
        
        1- Inserir dados
        2- Mostrar dados
        3- Atualizar dados
        4- Deletar dados
        5- Sair""")

match option:
        case "1" | "um" | "inserir":
                pass
        case "2" | "dois" | "mostrar dados":
                pass
        case "3" | "três" | "tres" | "atualizar":
                pass
        case "4" | "quatro" | "deletar" | "excluir":
                pass
        case "5" | "cinco" | "sair":
                pass
