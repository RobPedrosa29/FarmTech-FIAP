#Criar funções
#Inserir dados >>> area, insumo

# VETORES:
parcelas = []


# FUNÇÕES:
def parcela_cana_acucar():
    parcela = input(""""Selecione entre:
        1- Parcela existente;
        2- Criar nova parcela;
        3- Se não souber o que é parcela;
                    
        """).strip().lower()
    
    match parcela:
        case "1" | "parcela existente":
            pass
        case "2" | "criar parcela" | "criar nova parcela":
            pass
        case "3" | "nao sei" | "não sei":
            pass

def criar_parcela():
    novo_id = "P" + str(len(parcelas) + 1)

def parcela_existente():
    pass

def explica_parcela():
    print("Descrição de uma parcela")

def area_cana_acucar():
    area = input("""Selecione uma das opções abaixo: 
        1- Ja possuo o valor da área;
        2- Não possuo o valor da área;
        
        """).strip().lower()
    
    match area:
        case "1" | "um" | "ja possuo":
            pass   ### if m² ou ha
        case "2" | "dois" | "não possuo" | "nao possuo":
            pass   #### chamar função para calcular área

def calculo_area_cana():
    while True:
        try:
            comprimento = float(input("Digite o valor do comprimento, exemplo: 5000"))
            largura = float(input("Digite o valor da largura, exemplo: 2000"))
            break
        except ValueError:
            print("Por gentileza, digite apenas valores numéricos.")
    result_area = comprimento * largura
    return result_area