from main import(
    ler_float,
    selecionar_cultura
)

# VETOR:
parcelas_cana = []

########## PARCELAS E SELECIONAR CULTURA ##########

# -----Criar parcela-----
def criar_parcela():
    global parcelas_cana
    if len(parcelas_cana) >= 5:
        print("[Atenção!] Número máximo de parcelas atingido.")
        return
    
    numero = len(parcelas_cana) + 1 #add número do ID, exemplo P1, P2, P3
    nome_parcela = f"[P{numero}]"   #ID da parcela (P + número)

    cultura = "Cana-de-açucar"
    valor, unidade = area_cana_acucar()
    quantidade = insumo(valor, unidade)

    nova_parcela = {
        "ID": nome_parcela,
        "Cultura": cultura,
        "Área": valor,
        "Unidade": unidade,
        "Insumo": "Fertilizante NPK 20-05-20",
        "Quantidade de Insumo": quantidade
    }

    parcelas_cana.append(nova_parcela)
    print("\nParcela cadastrada com sucesso!")

# -----Mostrar parcela-----
def mostrar_parcela():
    if parcelas_cana:
        for parcela in parcelas_cana:
            print(f"\n{parcela['ID']}")
            for chave, valor in parcela.items():
                if chave == "Área":
                    print(f"{chave}: {valor:,.2f}")
                elif chave == "Quantidade de Insumo":
                    print(f"{chave}: {valor:,.2f} Kg")
                elif chave != "ID":
                    print(f"{chave}: {valor}")
                    
    else:
        print("\nNenhuma parcela cadastrada.")


# -----Atualizar parcela-----
def atualizar_parcela():
    nome = input("\nDigite o ID da parcela: ").strip()
    
    parcela = None
    for p in parcelas_cana:
        if p['ID'] == nome:
            parcela = p
            break

    if parcela is None:
        print("\nParcela não encontrada.")
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
            parcelas_cana["Área"] = valor
            parcelas_cana["Unidade"] = unidade
            parcelas_cana["Quantidade de Insumo"] = quantidade
        
        case "3" | "insumo":
            quantidade = ler_float("\nDigite a quantidade de fertilizante:\nResposta: ")
            parcelas_cana["Quantidade de Insumo"] = quantidade

        case _:
            print("\nOpção inválida.")

    print("\nParcela atualizada com sucesso!")

# -----Deletar parcela-----
def deletar_parcela():
    nome = input("Digite o ID da parcela: ").strip()
    parcela_encontrada = False
    for parcela in parcelas_cana:
        if parcela['ID'] == nome:
            parcelas_cana.remove(parcela)
            parcela_encontrada = True
            print(f"\nParcela removida com sucesso!")
            break
    if not parcela_encontrada:
        print("\nParcela não encontrada")





########## ÁREA DE CANA E CÁLCULOS ##########

# -----Área da cana-----
def area_cana_acucar():
    print("\n[Atenção!] Para um cálculo correto, evite valores com ',' (exemplo: 1,800) ou '.' (exemplo: 1.800), podendo ser valores inferiores a um (exemplo: 0,3)")
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
