# FarmTech-FIAP
Projeto acadêmico do curso de Inteligência Artificial na FIAP — Sistema para Agricultura Digital utilizando Python e R

## Descrição
Aplicação desenvolvida para apoiar a **Agricultura Digital**, permitindo gerenciar plantio e insumos de diferentes culturas e realizar análises estatísticas.

---

## Funcionalidades

### Python
- Suporte a **Cana-de-açúcar** e **Laranja**.
- Cadastro, atualização e deleção de parcelas/registros.
- Cálculo de área plantada e insumos (fertilizantes/herbicidas).
- Menu interativo com opções:
  - Inserir, mostrar, atualizar e deletar dados.
  - Exportar dados para análise em R.
  - Consultar clima via API pública.
  - Analisar CSVs gerados com R.
  - Selecionar outra cultura e sair do programa.

### R
- Script `analise.R` realiza:
  - Leitura dos CSVs exportados pelo Python.
  - Cálculo de **média** e **desvio padrão** das colunas numéricas.

### API Climática
- `clima_api.py` consulta o clima atual de qualquer cidade:
  - Usa **OpenStreetMap** para coordenadas.
  - Usa **Open-Meteo** para dados meteorológicos.
  - Exibe temperatura, vento e condição climática.

---

## Como Usar

1. **Execute o menu Python e selecione as opções dele**:
```bash
python menu.py

