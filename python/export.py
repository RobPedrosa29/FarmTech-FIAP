import csv
import os
from plantio_cana import parcela_cana
from plantio_laranja import registros

# Caminho absoluto da pasta R dentro do projeto
caminho_r = os.path.join(os.path.dirname(__file__), "R")  # __file__ é menu.py ou export.py
os.makedirs(caminho_r, exist_ok=True)  # cria a pasta se não existir

def exportar_dados():
    if parcela_cana:
        with open(os.path.join(caminho_r, "dados_cana.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=parcela_cana.keys())
            writer.writeheader()
            writer.writerow(parcela_cana)

    if registros:
        with open(os.path.join(caminho_r, "dados_laranja.csv"), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=registros[0].keys())
            writer.writeheader()
            writer.writerows(registros)

    print("\n[OK] Dados exportados para a pasta R com sucesso!")
