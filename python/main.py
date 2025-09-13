# VETORES:
parcela = {}


########## SELECIONAR CULTURA E PARCELAS ##########

# -----Float-----
def ler_float(prompt):
    while True:
        entrada = input(prompt).strip()
        entrada = entrada.replace(" ", "")
        
        if entrada.count(",") > 1 or entrada.count(".") > 1:
            print("\nFormato inválido, digite apenas um separador decimal!")
            continue
        
        if "," in entrada and "." in entrada:
            entrada = entrada.replace(".", "")
            entrada = entrada.replace(",", ".")
            entrada = entrada.replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("\nPor gentileza, digite apenas números válidos.")


# -----Selecionar cultura-----
def selecionar_cultura():
    while True:
        cultura = input("""\nQual cultura deseja?
1- Cana-de-açucar
2- Laranja
                        
---Resposta: """).strip().lower()
        match cultura:
            case "1" | "cana-de-açucar" | "cana de açucar":
                return "Cana-de-açucar"
            case "2" | "laranja":
                return "Laranja"
            case _:
                print("Cultura inválida, atualmente o sistema possui apenas Laranja e Cana-de-açucar.")

# -----Criar parcela-----
def criar_parcela():
    global parcela
    cultura = "Cana-de-açucar"
    valor, unidade = area_cana_acucar()
    quantidade = insumo(valor, unidade)

    parcela = {
        "Cultura": cultura,
        "Área": valor,
        "Unidade": unidade,
        "Insumo": "Fertilizante NPK 20-05-20",
        "Quantidade de Insumo": quantidade
    }

    print("\nParcela cadastrada com sucesso!")

# -----Mostrar parcela-----
def mostrar_parcela():
    if parcela:
        print("\n---Dados da Parcela---")
        for chave, valor in parcela.items():
            if chave == "Área":
                print(f"{chave}: {valor:,.2f}")
            elif chave == "Quantidade de Insumo":
                print(f"{chave}: {valor:,.2f} kg")
            else:
                print(f"{chave}: {valor}")
    else:
        print("\nNenhuma parcela cadastrada.")


# -----Atualizar parcela-----
def atualizar_parcela():
    if not parcela:
        print("\nNenhum dado para atualizar.")
        return
    
    escolha = input("""\nO que deseja atualizar?
                    
1- Cultura
2- Área
3- Insumo
                    
---Resposta: """).strip().lower()
    
    match escolha:
        case "1" | "cultura":
            cultura = selecionar_cultura()
            parcela["Cultura"] = cultura

        case "2" | "área" | "area":
            valor, unidade = area_cana_acucar()
            quantidade = insumo(valor, unidade)
            parcela["Área"] = valor
            parcela["Unidade"] = unidade
            parcela["Quantidade de Insumo"] = quantidade
        
        case "3" | "insumo":
            quantidade = ler_float("\nDigite a quantidade de fertilizante:\nResposta: ")
            parcela["Quantidade de Insumo"] = quantidade
    print("\nParcela atualizada com sucesso!")

# -----Deletar parcela-----
def deletar_parcela():
    global parcela
    parcela = {}
    print("\nParcela removida com sucesso!")






########## ÁREA DE CANA E CÁLCULOS ##########

# -----Área da cana-----
def area_cana_acucar():
    print("""\nAtenção: Para um cálculo correto, evite valores com "," (exemplo: 1,800) ou "." (exemplo: 1.800), podendo ser valores inferiores a um (exemplo: 0,3)

""")
    area = input("""\nSelecione entre:              
1- Possuo o valor da área
2- Não possuo o valor da área
        
---Resposta: """).strip().lower()
    
    match area:
        case "1" | "um" | "ja possuo":
            while  True:
                unidade = input("""\nSelecione a unidade:                             
1- Metro quadrado
2- Hectare
                
---Resposta: """).strip().lower()
                if unidade in ("1", "metro quadrado", "m²"):
                    valor = ler_float("\nDigite o valor do m²: ")
                    return valor, "m²"
                elif unidade in ("2", "hectares", "hectare", "ha"):
                    valor = ler_float("\nDigite o valor do hectare: ")
                    return valor, "ha"
                else:
                    print("\nOpção inválida, tente novamente!")
        case "2" | "dois" | "não possuo" | "nao possuo":
            valor = calculo_area_cana()
            return valor, "m²"

# -----Cálculo área da cana-----
def calculo_area_cana():
    comprimento = ler_float("""\nInforme o comprimento em metros.
    
---Resposta: """)
    largura = ler_float("""\nInforme a largura em metros.
                        
---Resposta: """)
    result_area = comprimento * largura
    print(f"\nÁrea: {result_area:,.0f} m² (metros quadrados).")
    return result_area

# -----Conversão m² em ha-----
def metroq_em_ha(metroq):
    return metroq / 10000

# -----Conversão ha em m²-----
def ha_em_metroq(ha):
    return ha * 10000

# -----Cálculo de insumo-----
def insumo(valor, unidade):
    print(f"\nAtenção: Para o cálculo de insumo da Cana-de-açucar será utilizada uma dosagem de 500 kg do fertilizante NPK 20-05-20 por hectare.\nRealizando cálculo...")
    
    if unidade == "m²":
        area_em_ha = metroq_em_ha(valor)
    else:
        area_em_ha = valor

    quantidade_insumo = area_em_ha * 500

    return quantidade_insumo
