# -*- coding: utf-8 -*-
# Sistema de Análise de Dados de Vendas
# Utilizando SQLite, Pandas, Matplotlib e Seaborn

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')

# Configuração do estilo visual
plt.style.use('default')
sns.set_palette("bright")

# Passo 1: Conectar ao banco de dados SQLite e criar tabela
def criar_banco_dados():
    """Cria o banco de dados SQLite e popula com dados de exemplo"""
    try:
        # Definir caminho do banco dentro da pasta U3
        caminho_bd = 'U3_A4_VISUALIZACAO_DE_DADOS_EM_PYTHON/data_base_sales.db'
        
        # Garantir que a pasta existe
        os.makedirs(os.path.dirname(caminho_bd), exist_ok=True)
        
        # Conectar ao banco de dados (cria se não existir)
        conexao = sqlite3.connect(caminho_bd)
        cursor = conexao.cursor()
        
        # Criar tabela (se não existir)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda DATE,
            produto TEXT,
            categoria TEXT,
            valor_venda REAL
        )
        """)
        
        # Verificar se a tabela já tem dados
        cursor.execute("SELECT COUNT(*) FROM vendas")
        if cursor.fetchone()[0] == 0:
            # Inserir dados de exemplo
            dados_exemplo = [
                ('2023-01-01', 'Produto A', 'Eletrônicos', 1350.00),
                ('2023-01-05', 'Produto B', 'Roupas', 250.00),
                ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
                ('2023-03-15', 'Produto D', 'Livros', 200.00),
                ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
                ('2023-04-02', 'Produto F', 'Roupas', 400.00),
                ('2023-05-05', 'Produto G', 'Livros', 150.00),
                ('2023-06-10', 'Produto H', 'Eletrônicos', 900.00),
                ('2023-07-20', 'Produto I', 'Roupas', 600.00),
                ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
                ('2023-09-30', 'Produto K', 'Livros', 300.00),
                ('2023-10-05', 'Produto L', 'Roupas', 450.00),
                ('2023-11-15', 'Produto M', 'Eletrônicos', 700.00),
                ('2023-12-20', 'Produto N', 'Livros', 250.00)
            ]
            
            cursor.executemany("""
            INSERT INTO vendas (data_venda, produto, categoria, valor_venda)
            VALUES (?, ?, ?, ?)
            """, dados_exemplo)
            
            conexao.commit()
            print("✅ Banco de dados criado e populado com dados de exemplo!")
        else:
            print("✅ Banco de dados já existe com dados!")
            
        conexao.close()
        
    except Exception as e:
        print(f"❌ Erro ao criar banco de dados: {e}")

# Passo 2: Explorar e preparar os dados
def carregar_dados():
    """Carrega os dados do SQLite para um DataFrame do Pandas"""
    try:
        # Usar o mesmo caminho da criação
        caminho_bd = 'U3_A4_VISUALIZACAO_DE_DADOS_EM_PYTHON/data_base_sales.db'
        conexao = sqlite3.connect(caminho_bd)
        df_vendas = pd.read_sql_query("SELECT * FROM vendas", conexao)
        conexao.close()
        
        # Converter tipos de dados
        df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
        df_vendas['mes'] = df_vendas['data_venda'].dt.month
        df_vendas['trimestre'] = df_vendas['data_venda'].dt.quarter
        
        print("✅ Dados carregados com sucesso!")
        print(f"📊 Total de registros: {len(df_vendas)}")
        
        return df_vendas
        
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return None

# Passo 3: Análise dos dados
def analisar_dados(df):
    """Realiza análises específicas nos dados de vendas"""
    print("\n" + "="*80)
    print("ANÁLISE DE DADOS DE VENDAS")
    print("="*80)
    
    # Estatísticas básicas
    print("\n📈 ESTATÍSTICAS GERAIS:")
    print(f"Total de vendas: R$ {df['valor_venda'].sum():.2f}")
    print(f"Média de vendas: R$ {df['valor_venda'].mean():.2f}")
    print(f"Maior venda: R$ {df['valor_venda'].max():.2f}")
    print(f"Menor venda: R$ {df['valor_venda'].min():.2f}")
    
    # Vendas por categoria
    print("\n🏷️ VENDAS POR CATEGORIA:")
    vendas_categoria = df.groupby('categoria')['valor_venda'].agg(['sum', 'count'])
    vendas_categoria['sum'] = vendas_categoria['sum'].round(2)
    print(vendas_categoria)
    
    # Vendas por mês
    print("\n📅 VENDAS POR MÊS:")
    vendas_mes = df.groupby('mes')['valor_venda'].sum().round(2)
    print(vendas_mes)
    
    return {
        'vendas_categoria': df.groupby('categoria')['valor_venda'].sum(),
        'vendas_mes': df.groupby('mes')['valor_venda'].sum(),
        'contagem_categoria': df['categoria'].value_counts()
    }

# Passo 4: Visualização dos dados
def visualizar_dados(df, analises):
    """Cria visualizações dos dados de vendas"""
    print("\n🎨 CRIANDO VISUALIZAÇÕES...")
    
    # Configuração do layout dos gráficos
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análise de Vendas - Ano 2023', fontsize=16, fontweight='bold', color='#2E4053')
    
    cores_pizza = ['#0000FF', '#FF0000', '#FFFF00']  
    cores_barras = ["#00FF15"]  
    cores_boxplot = ['#0000FF', '#FF0000', '#FFFF00']
    
    # Gráfico 1: Vendas por Categoria (Pizza)
    categorias = analises['vendas_categoria'].index
    valores = analises['vendas_categoria'].values
    
    axes[0, 0].pie(valores, labels=categorias, autopct='%1.1f%%', colors=cores_pizza,textprops={'fontsize': 10, 'fontweight': 'bold'})
    axes[0, 0].set_title('Distribuição de Vendas por Categoria', fontweight='bold', fontsize=12)
    
    # Gráfico 2: Vendas por Mês (Barras)
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    vendas_mes_completo = analises['vendas_mes'].reindex(range(1, 13), fill_value=0)
    
    bars = axes[0, 1].bar(meses, vendas_mes_completo.values, color=cores_barras, alpha=0.8)
    axes[0, 1].set_title('Vendas Mensais', fontweight='bold', fontsize=12)
    axes[0, 1].set_ylabel('Valor de Vendas (R$)', fontweight='bold')
    axes[0, 1].tick_params(axis='x', rotation=0)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 40,
                        f'R$ {height:.0f}', ha='center', va='bottom', 
                        fontweight='bold', fontsize=9)
    
    # Gráfico 3: Distribuição de Vendas (Boxplot)
    boxplot = sns.boxplot(data=df, x='categoria', y='valor_venda', ax=axes[1, 0], palette=cores_boxplot)
    axes[1, 0].set_title('Distribuição de Valores por Categoria', fontweight='bold', fontsize=12)
    axes[1, 0].set_ylabel('Valor de Venda (R$)', fontweight='bold')
    axes[1, 0].set_xlabel('Categoria', fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Gráfico 4: Contagem de Vendas por Categoria (Barras)
    countplot = sns.countplot(data=df, x='categoria', ax=axes[1, 1], palette=cores_boxplot, hue='categoria', legend=False)
    axes[1, 1].set_title('Quantidade de Vendas por Categoria', fontweight='bold', fontsize=12)
    axes[1, 1].set_ylabel('Número de Vendas', fontweight='bold')
    axes[1, 1].set_xlabel('Categoria', fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    
    # Adicionar valores nas barras do countplot
    for container in countplot.containers:
        for bar in container:
            height = bar.get_height()
            axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom', 
                        fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    # Gráfico adicional: Tendência temporal
    plt.figure(figsize=(12, 6))
    df.groupby('data_venda')['valor_venda'].sum().plot(
        marker='o', color='#0000FF', linewidth=3, markersize=8
    )
    plt.title('Tendência de Vendas ao Longo do Tempo', fontweight='bold', fontsize=14)
    plt.ylabel('Valor de Vendas (R$)', fontweight='bold')
    plt.xlabel('Data', fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Passo 5: Conclusão e insights
def gerar_insights(df, analises):
    """Gera insights baseados na análise dos dados"""
    print("\n" + "="*80)
    print("INSIGHTS E RECOMENDAÇÕES")
    print("="*80)
    
    # Encontrar o mês com maior venda
    mes_max_venda = analises['vendas_mes'].idxmax()
    valor_max_venda = analises['vendas_mes'].max()
    
    # Encontrar a categoria mais vendida
    categoria_max_venda = analises['vendas_categoria'].idxmax()
    valor_categoria_max = analises['vendas_categoria'].max()
    
    print(f"📈 **Insight 1:** Mês de maior faturamento foi {mes_max_venda}º mês com R$ {valor_max_venda:.2f}")
    print(f"🏆 **Insight 2:** Categoria '{categoria_max_venda}' foi a mais lucrativa (R$ {valor_categoria_max:.2f})")
    
    # Calcular participação percentual
    participacao = (analises['vendas_categoria'] / analises['vendas_categoria'].sum() * 100).round(1)
    
    print(f"📊 **Insight 3:** Participação por categoria:")
    for categoria, percentual in participacao.items():
        print(f"   • {categoria}: {percentual}%")
    
    # Recomendações
    print("\n💡 **Recomendações Estratégicas:**")
    print("1. Investir mais em marketing para a categoria de maior faturamento")
    print("2. Analisar sazonalidade para planejar estoques")
    print("3. Desenvolver promoções para categorias com menor participação")
    print("4. Expandir portfólio na categoria mais lucrativa")
    print("5. Focar em estratégias para os meses de menor performance")

# Função principal
def main():
    """Função principal que executa todo o fluxo de análise"""
    print("\nSISTEMA DE ANÁLISE DE DADOS DE VENDAS")
    print("="*80)
    
    # Passo 1: Criar banco de dados
    criar_banco_dados()
    
    # Passo 2: Carregar dados
    df_vendas = carregar_dados()
    
    if df_vendas is not None:
        # Exibir primeiras linhas
        print("\n📋 PRIMEIRAS LINHAS DO DATASET:")
        print(df_vendas.head())
        
        # Passo 3: Analisar dados
        resultados_analise = analisar_dados(df_vendas)
        
        # Passo 4: Visualizar dados
        visualizar_dados(df_vendas, resultados_analise)
        
        # Passo 5: Gerar insights
        gerar_insights(df_vendas, resultados_analise)

# Executar o programa
if __name__ == "__main__":
    # Instalar dependências se necessário (no Colab)
    try:
        import seaborn
    except ImportError:
        print("Instalando bibliotecas necessárias...")
        import subprocess
        subprocess.run(["pip", "install", "seaborn", "matplotlib", "pandas"])
    
    main()