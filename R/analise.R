library(readr)

# Ler os arquivos CSV exportados do Python
cana <- read_csv("R/dados_cana.csv", show_col_types = FALSE)
laranja <- read_csv("R/dados_laranja.csv", show_col_types = FALSE)

cat("\n===== ANÁLISE DA CANA-DE-AÇÚCAR =====\n")
print(cana)
cat("\nMédia da área (m²): ", mean(cana$Área))
cat("\nDesvio padrão da quantidade de insumo (kg): ", sd(cana$`Quantidade de Insumo`))

cat("\n\n===== ANÁLISE DA LARANJA =====\n")
print(laranja)
cat("\nMédia da área (m²): ", mean(laranja$area_m2))
cat("\nDesvio padrão dos litros de herbicida: ", sd(laranja$litros))
