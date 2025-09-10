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

