from main import(
    ler_float,
    selecionar_cultura
)

from plantio_laranja import (inserir_dados)

# VETOR:
parcela_cana = {}

########## PARCELAS E SELECIONAR CULTURA ##########

# -----Criar parcela-----
def criar_parcela():
    global parcela_cana
    cultura = "Cana-de-açucar"
    valor, unidade = area_cana_acucar()
    quantidade = insumo(valor, unidade)

    parcela_cana = {
        "Cultura": cultura,
        "Área": valor,
        "Unidade": unidade,
        "Insumo": "Fertilizante NPK 20-05-20",
        "Quantidade de Insumo": quantidade
    }

    print("\nParcela cadastrada com sucesso!")

# -----Mostrar parcela-----
def mostrar_parcela():
    if parcela_cana:
        print("\n  [Dados da Parcela]")
        for chave, valor in parcela_cana.items():
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
    if not parcela_cana:
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
            parcela_cana["Cultura"] = cultura

        case "2" | "área" | "area":
            valor, unidade = area_cana_acucar()
            quantidade = insumo(valor, unidade)
            parcela_cana["Área"] = valor
            parcela_cana["Unidade"] = unidade
            parcela_cana["Quantidade de Insumo"] = quantidade
        
        case "3" | "insumo":
            quantidade = ler_float("\nDigite a quantidade de fertilizante:\nResposta: ")
            parcela_cana["Quantidade de Insumo"] = quantidade
    print("\nParcela atualizada com sucesso!")

# -----Deletar parcela-----
def deletar_parcela():
    global parcela_cana
    if not parcela_cana:
        print("\nNenhuma parcela para deletar")
        return
    parcela_cana = {}
    print("\nParcela removida com sucesso!")
    





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
