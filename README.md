# Pandas Data Analysis Portfolio

> Demonstrating data analysis skills progression with Python Pandas | Demonstrando evolução de habilidades em análise de dados com Python Pandas

[English](#english) | [Português](#português)

---

## English

### About This Project

This repository showcases my learning journey and practical skills with the Pandas library for data analysis. Through real-world restaurant data, I demonstrate data manipulation, statistical analysis, and visualization capabilities.

### Skills Demonstrated

#### Data Manipulation
- Loading data from multiple sources (Excel, CSV)
- Working with multi-sheet Excel files
- Data filtering and transformation
- GroupBy operations for aggregation
- Multi-level indexing

#### Statistical Analysis
- Descriptive statistics calculation
- Customer behavior analysis
- Product performance metrics
- Per-customer consumption ratios
- Sales trend identification

#### Data Visualization
- Creating horizontal bar charts with Matplotlib
- Custom chart formatting and labeling
- Visual data storytelling

#### Automation
- Automated PDF report generation
- Integration of data analysis with document creation
- End-to-end data pipeline

### Technical Stack

```python
- Python 3.x
- pandas: Data manipulation and analysis
- matplotlib:  Data visualization
- fpdf: PDF report generation
```

### Project Structure

```
inicio/          # Initial analysis and data exploration
├── org.ipynb    # Main analysis notebook
└── dados. xlsx   # Source data

relatorio/       # Automated reporting
├── auto_relatorio.py  # Report generation script
└── dados.csv    # Sales data
```

### Key Analyses

#### 1. Customer Traffic Analysis
Analyzed customer flow across two restaurant locations with 168 records spanning multiple dates and service modes.

#### 2. Product Consumption Patterns
Processed 814 product records to identify consumption trends across DRINKS and SOFT DRINKS categories. 

#### 3. Per-Customer Metrics
Calculated consumption ratios to understand customer behavior: 
- Average drinks per customer by location
- Category preference analysis
- Peak consumption identification

#### 4. Top Products Ranking
Implemented ranking algorithm to identify top 5 products per category and location. 

### Code Highlights

**Data Loading & Filtering**
```python
df1 = pd.read_excel('dados.xlsx', sheet_name='Por Canal')
df2 = pd.read_excel('dados.xlsx', sheet_name='Consumo de Produtos')
df2 = df2[df2['T. Categoria'].isin(['DRINKS', 'SOFT DRINKS'])]
```

**Aggregation & Analysis**
```python
n_pessoas = df1. groupby('Estabelecimento')['N. Pessoas'].sum()
quant = df2.groupby(['Estabelecimento', 'T. Categoria'])['Quant.'].sum()
quant_por_pessoa = quant / n_pessoas
```

**Top N Selection**
```python
top5 = df2.groupby(['Estabelecimento', 'T. Categoria', 'Descrição'])['Quant.'].sum()
top5 = top5.sort_values(ascending=False)
top5 = top5.groupby(['Estabelecimento', 'T. Categoria']).head(5)
```

### Results

**ANALIA FRANCO Location:**
- 13,088 customers served
- 1. 03 drinks per customer
- 0.72 soft drinks per customer

**BARRA SHOPPING Location:**
- 26,563 customers served
- 0.05 drinks per customer
- 1.07 soft drinks per customer

### Learning Progression

1. **Data Loading**:  Mastered reading from Excel with multiple sheets
2. **Data Filtering**: Applied conditional filtering with `.isin()`
3. **Grouping Operations**: Used single and multi-level groupby
4. **Calculations**: Performed division operations between Series
5. **Visualization**: Created formatted charts with custom labels
6. **Automation**:  Built automated reporting pipeline

### Installation & Usage

```bash
# Install dependencies
pip install pandas matplotlib fpdf

# Run Jupyter notebook
jupyter notebook inicio/org.ipynb

# Generate automated report
python relatorio/auto_relatorio.py
```

### Contact

Open to opportunities in Data Analysis and Python Development. 

GitHub: [@C2002G](https://github.com/C2002G)

---

## Português

### Sobre Este Projeto

Este repositório demonstra minha jornada de aprendizado e habilidades práticas com a biblioteca Pandas para análise de dados. Através de dados reais de restaurantes, demonstro capacidades de manipulação de dados, análise estatística e visualização. 

### Habilidades Demonstradas

#### Manipulação de Dados
- Carregamento de dados de múltiplas fontes (Excel, CSV)
- Trabalho com arquivos Excel multi-abas
- Filtragem e transformação de dados
- Operações GroupBy para agregação
- Indexação multi-nível

#### Análise Estatística
- Cálculo de estatísticas descritivas
- Análise de comportamento de clientes
- Métricas de performance de produtos
- Razões de consumo por cliente
- Identificação de tendências de vendas

#### Visualização de Dados
- Criação de gráficos de barras horizontais com Matplotlib
- Formatação e rotulagem personalizada de gráficos
- Storytelling visual com dados

#### Automação
- Geração automática de relatórios PDF
- Integração de análise de dados com criação de documentos
- Pipeline de dados end-to-end

### Stack Técnica

```python
- Python 3.x
- pandas: Manipulação e análise de dados
- matplotlib: Visualização de dados
- fpdf: Geração de relatórios PDF
```

### Estrutura do Projeto

```
inicio/          # Análise inicial e exploração de dados
├── org.ipynb    # Notebook principal de análise
└── dados.xlsx   # Dados fonte

relatorio/       # Relatórios automatizados
├── auto_relatorio.py  # Script de geração de relatórios
└── dados.csv    # Dados de vendas
```

### Análises Principais

#### 1. Análise de Fluxo de Clientes
Analisei o fluxo de clientes em duas localizações de restaurantes com 168 registros abrangendo múltiplas datas e modos de serviço.

#### 2. Padrões de Consumo de Produtos
Processei 814 registros de produtos para identificar tendências de consumo nas categorias DRINKS e SOFT DRINKS.

#### 3. Métricas por Cliente
Calculei razões de consumo para entender o comportamento do cliente:
- Média de bebidas por cliente por localização
- Análise de preferência de categoria
- Identificação de picos de consumo

#### 4. Ranking de Produtos Top
Implementei algoritmo de ranking para identificar os top 5 produtos por categoria e localização.

### Destaques do Código

**Carregamento & Filtragem de Dados**
```python
df1 = pd.read_excel('dados. xlsx', sheet_name='Por Canal')
df2 = pd.read_excel('dados.xlsx', sheet_name='Consumo de Produtos')
df2 = df2[df2['T.  Categoria'].isin(['DRINKS', 'SOFT DRINKS'])]
```

**Agregação & Análise**
```python
n_pessoas = df1.groupby('Estabelecimento')['N.Pessoas'].sum()
quant = df2.groupby(['Estabelecimento', 'T. Categoria'])['Quant.'].sum()
quant_por_pessoa = quant / n_pessoas
```

**Seleção Top N**
```python
top5 = df2.groupby(['Estabelecimento', 'T. Categoria', 'Descrição'])['Quant.'].sum()
top5 = top5.sort_values(ascending=False)
top5 = top5.groupby(['Estabelecimento', 'T. Categoria']).head(5)
```

### Resultados

**Localização ANÁLIA FRANCO:**
- 13.088 clientes atendidos
- 1,03 drinks por cliente
- 0,72 soft drinks por cliente

**Localização BARRA SHOPPING:**
- 26.563 clientes atendidos
- 0,05 drinks por cliente
- 1,07 soft drinks por cliente

### Progressão de Aprendizado

1. **Carregamento de Dados**: Domínio de leitura de Excel com múltiplas abas
2. **Filtragem de Dados**: Aplicação de filtros condicionais com `.isin()`
3. **Operações de Agrupamento**: Uso de groupby simples e multi-nível
4. **Cálculos**:  Operações de divisão entre Series
5. **Visualização**:  Criação de gráficos formatados com rótulos customizados
6. **Automação**: Construção de pipeline automatizado de relatórios

### Instalação & Uso

```bash
# Instalar dependências
pip install pandas matplotlib fpdf

# Executar Jupyter notebook
jupyter notebook inicio/org.ipynb

# Gerar relatório automatizado
python relatorio/auto_relatorio.py
```

### Contato

Aberto a oportunidades em Análise de Dados e Desenvolvimento Python.

GitHub: [@C2002G](https://github.com/C2002G)
