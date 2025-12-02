import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Ler o CSV
try:
    df = pd.read_csv("dados.csv")
    print("Dados carregados! Olha o resumo:")
    print(df.describe())
except:
    print("Ops! Checa se o 'dados.csv' tá na pasta, jovem Padawan!")

# Análise simples: total e média de vendas
total_vendas = df["Vendas"].sum()
media_vendas = df["Vendas"].mean()

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df["Produto"], df["Vendas"], color="skyblue")
plt.title("Vendas por Produto - Junho 2025")
plt.xlabel("Produto")
plt.ylabel("Vendas (R$)")
plt.savefig("vendas_grafico.png")
plt.close()

# Criar um PDF 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt='Relatório Automático de Vendas - Junho 2025', ln=1, align="C")
pdf.cell(200, 10, txt=f"Total de Vendas: R$ {total_vendas}", ln=1)
pdf.cell(200, 10, txt=f"Média de Vendas: R$ {media_vendas:.2f}", ln=1)
pdf.ln(10)
pdf.image("vendas_grafico.png", x=10, w=190)
pdf.output("relatorio_vendas.pdf")
print("Tcharan! Seu relatório 'relatorio_vendas.pdf' tá pronto!")