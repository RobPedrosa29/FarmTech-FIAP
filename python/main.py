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
        cultura = input("""Selecione entre as culturas disponíveis:
1- Cana-de-açucar
2- Laranja
                        
---Resposta: """).strip().lower()
        
        print("Acessando as informações da cultura escolhida...")
        
        match cultura:
            case "1" | "cana-de-açucar" | "cana de açucar":
                return "Cana-de-açucar"
            case "2" | "laranja":
                return "Laranja"
            case _:
                print("\nCultura indisponível, atualmente o sistema possui apenas Laranja e Cana-de-açucar.")
