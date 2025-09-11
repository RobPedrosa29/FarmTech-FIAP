#Criar funções
#Inserir dados >>> area, insumo

# VETORES:
parcelas = []


# FUNÇÕES:


# FALTA: chamar functions (parcela_existente | criar_parcela | explica_parcela) no case
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
            explica_parcela()

            
# FALTA: chamar o resultado de outras functions para estruturar o ID
def criar_parcela():
    novo_id = "P" + str(len(parcelas) + 1)

# FALTA: mostrar as parcelas existentes para o user realizar a escolha delas
def parcela_existente():
    parcelas

# -----AGUARDANDO CHECK-----
def explica_parcela():
    print("""
          Parcela é um pedaço da área de plantio, identificado por um código (ex: P1, P2).\nÉ usada para organizar cálculos de área e insumos.""")

# -----AGUARDANDO CHECK-----
def area_cana_acucar():
    area = input("""Selecione uma das opções abaixo: 
        1- Ja possuo o valor da área;
        2- Não possuo o valor da área;
        
        """).strip().lower()
    
    match area:
        case "1" | "um" | "ja possuo":
            while  True:
                unidade = input("""Selecione entre:
            1- Metro quadrado;
            2- Hectare
                
            """).strip().lower()
                if unidade in ("1", "metro quadrado", "m²"):
                    valor = input("Digite o valor do m²: ")
                    try:
                        valor = float(valor)
                        return valor, "m²"
                    except ValueError:
                        print("Por gentileza, digite apenas números")
                elif unidade in ("2", "hectares", "hectare", "ha"):
                    valor = input("Digite o valor do hectare: ")
                    try: 
                        valor = float(valor)
                        return valor, "ha"
                    except ValueError:
                        print("Por gentileza, digite apenas números")
                else:
                    print("Opção inválida, tente novamente!")
        case "2" | "dois" | "não possuo" | "nao possuo":
            valor = calculo_area_cana()
            return valor, "m²"

# -----AGUARDANDO CHECK-----
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


# -----AGUARDANDO CHECK-----
def metroq_p_ha(metroq):
    return metroq / 1000

# -----AGUARDANDO CHECK-----
def ha_p_metroq(ha):
    return ha * 10000