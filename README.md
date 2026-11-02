# Saúde mental

Este repositório reúne dados, notebooks e materiais de apoio para preparar e
analisar dados de saúde mental, além de estudos de modelos supervisionados e
não supervisionados. O fluxo principal identificado nos notebooks utiliza
arquivos NHIS Adult 2025; há também uma consulta independente à PNS 2019.

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `01 Preparação dos dados/` | Dados brutos, selecionados e limpos do NHIS Adult 2025; notebooks de seleção, substituição de valores, tratamento de ruído e verificação de duplicatas. Inclui também um CSV processado e um script de consulta à PNS. |
| `02 Análise exploratória/` | Análises exploratórias, estatísticas com SciPy e análise de redundância. |
| `03 Modelos supervisionados/` | Estudos de Random Forest, XGBoost, SVM e KNN. Os notebooks usam a base limpa centralizada em `01 Preparação dos dados/dados/limpos/`. |
| `04 Modelos não supervisionados/` | Preparação e clusterização hierárquica, K-means e K-modes, com os dados derivados da clusterização junto ao fluxo hierárquico. |
| `repositorio imagens/` | Figuras exportadas pelos notebooks visuais, organizadas pela mesma área e pelo notebook que as gerou. |
| `05 Apresentação/` | Espaço reservado para apresentações. |
| `06 Material de referência/` | Artigo em PDF e planilhas de correlações usadas como material de apoio. |
| `07 Material legado/` | Notebooks e arquivos antigos, incluindo estudos de 2024 e versões anteriores de preparação. |

O fluxo de preparação principal é:

1. `01_selecao_variaveis_2025.ipynb`: lê `dados/brutos/adult25.csv` e gera
   `dados/selecionados/adult25_selecionados.csv`.
2. `02_substituicao_valores_2025.ipynb`: lê a base selecionada e gera
   `dados/limpos/adult25_limpo.csv`.
3. `03_tratamento_ruido_2025.ipynb` e
   `04_verificacao_duplicatas_2025.ipynb`: verificações sobre a base limpa.

Entre os notebooks de análise estão `06_analise_exploratoria_dados_2025.ipynb`,
`estudo_scipy_stats.ipynb` e `05_analise_redundancia_2025.ipynb`. Os demais
estudos de modelos estão agrupados por técnica nas pastas 03 e 04.

As figuras ficam em `repositorio imagens/`, com subpastas para cada notebook
que as produz. Por exemplo, os gráficos da análise de redundância são salvos em
`repositorio imagens/02 Análise exploratória/05_analise_redundancia_2025/`;
os demais seguem os diretórios correspondentes em análise exploratória,
modelos supervisionados e modelos não supervisionados.

## Ambiente e execução

O repositório não contém `requirements.txt`, `pyproject.toml` ou arquivo de
ambiente, portanto as versões das dependências não estão fixadas. Os arquivos
principais são notebooks Jupyter; use um ambiente Python com Jupyter e instale
as bibliotecas exigidas pelos imports do notebook que deseja executar. Para os
notebooks executados neste repositório, os pacotes usados foram:

```bash
python3 -m pip install jupyter ipykernel pandas numpy matplotlib seaborn scipy scikit-learn xgboost kmodes umap-learn
```

No macOS, o XGBoost também requer o runtime OpenMP (`brew install libomp`). O
script `01 Preparação dos dados/scripts/PesquisaNacionaldeSaúdeQuery.py` usa
`basedosdados` e requer esse pacote, além de substituir o placeholder
`SEU_BILLING_ID` por um `billing_id` válido antes da execução.

Abra os notebooks no Jupyter e execute as células na ordem apresentada. Os
caminhos de dados são relativos ao repositório e os notebooks devem ser
executados com o diretório de trabalho na pasta do próprio notebook. Os
notebooks de preparação leem os arquivos de entrada e gravam os resultados nas
pastas de dados correspondentes. A execução da consulta à PNS depende de acesso
e configuração próprios do BasedosDados.

## Referências e observações sobre os dados

- [Pesquisa Nacional de Saúde (PNS) no Base dos Dados](https://basedosdados.org/dataset/86bac6cc-575f-4289-a857-13f3f52c9a1d?table=f8b6030c-3fb1-4f64-81ef-3c5c3c888b6c)
- [NHIS Adult 2024 — arquivo de referência registrado anteriormente](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip)

O arquivo bruto `adult25.csv` e os notebooks atuais são identificados como
NHIS Adult 2025, mas o repositório não registra uma fonte/versionamento
inequívoco que associe esse arquivo à referência NHIS Adult 2024 acima. O CSV
`01 Preparação dos dados/dados/processados/nhis_saude_mental_processado.csv` foi
preservado, mas não é
referenciado pelos notebooks ativos; confirme sua origem e uso antes de
integrá-lo ao fluxo principal.

O arquivo `adult24.csv` não é versionado (está no `.gitignore`). Para executar
os notebooks de NHIS 2024 em `07 Material legado/`, baixe o arquivo do link
acima e extraia `adult24.csv` diretamente nessa pasta.
