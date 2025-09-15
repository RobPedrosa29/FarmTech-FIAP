
# Dados da Cana-de-açucar
cana <- read.csv("R/dados_cana.csv")   # Lê o CSV exportado do Python
print(cana)                             # Mostra os dados lidos

# Calcular média da área
media_area <- mean(cana$Área)
print(paste("Média da Área:", media_area))

# Calcular desvio padrão da área
desvio_area <- sd(cana$Área)
print(paste("Desvio padrão da Área:", desvio_area))



# Dados da Laranja
laranja <- read.csv("R/dados_laranja.csv")   # Lê o CSV exportado do Python
print(laranja)                               # Mostra os dados lidos

# Calcular média da área em m²
media_area_laranja <- mean(laranja$area_m2)
print(paste("Média da Área (Laranja):", media_area_laranja))

# Calcular desvio padrão da área em m²
desvio_area_laranja <- sd(laranja$area_m2)
print(paste("Desvio padrão da Área (Laranja):", desvio_area_laranja))
