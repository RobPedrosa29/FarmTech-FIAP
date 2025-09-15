import csv
import os
from plantio_cana import parcelas_cana
from plantio_laranja import registros

# Caminho absoluto da pasta R dentro do projeto
caminho_r = os.path.join(os.path.dirname(__file__), "R")
os.makedirs(caminho_r, exist_ok=True)

def exportar_dados():
    # Exportar parcelas de cana
    if parcelas_cana:
        caminho_arquivo_cana = os.path.join(caminho_r, "dados_cana.csv")
        with open(caminho_arquivo_cana, "w", newline="", encoding="utf-8") as f:
            # Pega as chaves do primeiro dicionário como cabeçalho
            cabecalho = parcelas_cana[0].keys()
            writer = csv.DictWriter(f, fieldnames=cabecalho)
            writer.writeheader()
            for parcela in parcelas_cana:
                writer.writerow(parcela)
        print(f"[OK] Dados da cana exportados para {caminho_arquivo_cana}")

    # Exportar registros de laranja
    if registros:
        caminho_arquivo_laranja = os.path.join(caminho_r, "dados_laranja.csv")
        with open(caminho_arquivo_laranja, "w", newline="", encoding="utf-8") as f:
            cabecalho = registros[0].keys()
            writer = csv.DictWriter(f, fieldnames=cabecalho)
            writer.writeheader()
            for registro in registros:
                writer.writerow(registro)
        print(f"[OK] Dados da laranja exportados para {caminho_arquivo_laranja}")
