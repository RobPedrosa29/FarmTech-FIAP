import csv
import os
from plantio_cana import parcelas_cana
from plantio_laranja import registros

# Caminho da raiz do projeto (um nível acima de onde está este arquivo)
caminho_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pasta R dentro da raiz do projeto
caminho_r = os.path.join(caminho_raiz, "R")
os.makedirs(caminho_r, exist_ok=True)

def exportar_dados():
    # Exportar parcelas de cana
    if parcelas_cana:
        caminho_arquivo_cana = os.path.join(caminho_r, "dados_cana.csv")
        with open(caminho_arquivo_cana, "w", newline="", encoding="utf-8") as f:
            cabecalho = parcelas_cana[0].keys()
            writer = csv.DictWriter(f, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(parcelas_cana)
        print(f"[OK] Dados da cana exportados para {caminho_arquivo_cana}")

    # Exportar registros de laranja
    if registros:
        caminho_arquivo_laranja = os.path.join(caminho_r, "dados_laranja.csv")
        with open(caminho_arquivo_laranja, "w", newline="", encoding="utf-8") as f:
            cabecalho = registros[0].keys()
            writer = csv.DictWriter(f, fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(registros)
        print(f"[OK] Dados da laranja exportados para {caminho_arquivo_laranja}")
