# =========================== #
# Code da cultura 2 - Laranja #
# =========================== #


registros = [] # vetor/lista para armazenar até 5 registros de entrada do usuario


def calcular_ruas(largura_terreno: float, espacamento_linhas: float) -> int:
    return int(largura_terreno // espacamento_linhas) # // realiza a divisão inteira do valor


def calcular_comprimento_ruas(total_ruas: int, comprimento_lavoura: float) -> float:
    return total_ruas * comprimento_lavoura


def calcular_area(largura_terreno: float, comprimento_lavoura: float) -> float:
    return largura_terreno * comprimento_lavoura


def calcular_herbicida(largura_terreno: float, comprimento_lavoura: float, dose_por_hectare: float) -> float:
    area_m2 = calcular_area(largura_terreno, comprimento_lavoura)
    area_ha = area_m2 / 10000 # converte a área do terreno "m2" em hectares "ha"
    return area_ha * dose_por_hectare


def inserir_dados():
    if len(registros) >= 5: # maximo de 5 para armazenamento na lista/vetor
        print("\n[Atenção!] Limite de 5 registros atingido! Delete algum registro antes de adicionar um novo.\n")
        return

    largura = float(input("Informe a largura do terreno (m): "))
    comprimento = float(input("Informe o comprimento do terreno (m): "))
    espacamento = float(input("Informe o espaçamento entre linhas (m): "))
    dose = float(input("Informe a dose de herbicida (L/ha): "))

    ruas = calcular_ruas(largura, espacamento)
    comprimento_total = calcular_comprimento_ruas(ruas, comprimento)
    area = calcular_area(largura, comprimento)
    litros = calcular_herbicida(largura, comprimento, dose)

    registro = {
        "largura": largura,
        "comprimento": comprimento,
        "espacamento": espacamento,
        "dose": dose,
        "ruas": ruas,
        "comprimento_total": comprimento_total,
        "area_m2": area,
        "area_ha": area / 10000,
        "litros": litros
    }

    registros.append(registro) 
    print("\n[OK] Registro adicionado com sucesso!\n")


def exibir_dados():
    if not registros: # Se lista vazia, alertar usuario. Senão, informar sucesso
        print("\n[Atenção!] Nenhum registro armazenado!\n")
        return

    print("\n--- Registros Salvos ---")
    for i, dados in enumerate(registros, start=1):
        print(f"\nRegistro {i}:")
        print(f"  Largura do terreno: {dados['largura']} m")
        print(f"  Comprimento do terreno: {dados['comprimento']} m")
        print(f"  Espaçamento entre linhas: {dados['espacamento']} m")
        print(f"  Dose de herbicida: {dados['dose']} L/ha")
        print(f"  Total de ruas: {dados['ruas']}")
        print(f"  Comprimento total das ruas: {dados['comprimento_total']:.2f} m")
        print(f"  Área total: {dados['area_m2']:.2f} m² ({dados['area_ha']:.2f} ha)")
        print(f"  Herbicida necessário: {dados['litros']:.2f} L")


def atualizar_dados():
    if not registros:
        print("\n[Atenção!] Nenhum registro para atualizar!\n")
        return

    exibir_dados()
    indice = int(input("\nDigite o número do registro que deseja atualizar: ")) - 1

    if 0 <= indice< len(registros):
        registros.pop(indice)
        print("\n[@] Insira os novos dados para este registro:\n")
        inserir_dados()
    else:
        print("\n[Atenção!] Registro inválido!\n")


def deletar_dados():
    if not registros:
        print("\n[Atenção!] Nenhum registro para deletar!\n")
        return
    
    exibir_dados()
    pos = input("\nDigite o número do registro que deseja deletar: ")
    if pos.isdigit():
        pos = int(pos)
        if 1 <= pos <= len(registros):
            removido = registros.pop(pos - 1)
            print(f"\n[x] Registro {pos} deletado com sucesso: {removido}\n")
        else:
            print("[ATENÇÃO!] Posição inválida!")
    else:
        print("[ATENÇÃO!] Entrada inválida, digite um número inteiro.")

