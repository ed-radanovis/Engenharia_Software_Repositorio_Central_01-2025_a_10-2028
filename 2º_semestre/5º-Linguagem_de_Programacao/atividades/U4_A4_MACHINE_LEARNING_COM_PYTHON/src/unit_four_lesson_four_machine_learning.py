# -*- coding: utf-8 -*-
# Sistema de Classificação de Flores Iris com Machine Learning
# Utilizando TensorFlow, Scikit-learn e Pandas

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Configuração de estilo para visualizações
plt.style.use('default')
sns.set_palette("husl")

print("=" * 60)
print("SISTEMA DE CLASSIFICAÇÃO DE FLORES IRIS")
print("USANDO MACHINE LEARNING COM TENSORFLOW")
print("=" * 60)

# Passo 1: Importar Bibliotecas e Carregar Dados
def carregar_dados():
    """Carrega e explora o conjunto de dados Iris"""
    print("\n📊 PASSO 1: CARREGANDO E EXPLORANDO OS DADOS")
    print("-" * 50)
    
    # Carregar o conjunto de dados Iris
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Criar DataFrame para melhor visualização
    df_iris = pd.DataFrame(X, columns=iris.feature_names)
    df_iris['target'] = y
    df_iris['species'] = df_iris['target'].apply(lambda x: iris.target_names[x])
    
    print("📋 Informações do dataset:")
    print(f"• Número de amostras: {X.shape[0]}")
    print(f"• Número de características: {X.shape[1]}")
    print(f"• Classes: {list(iris.target_names)}")
    print(f"• Características: {list(iris.feature_names)}")
    
    print("\n📈 Estatísticas descritivas:")
    print(df_iris.describe())
    
    return X, y, iris, df_iris

# Passo 2: Pré-processamento dos Dados
def preprocessar_dados(X, y):
    """Pré-processa os dados para o treinamento"""
    print("\n🔄 PASSO 2: PRÉ-PROCESSAMENTO DOS DADOS")
    print("-" * 50)
    
    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Normalizar os dados
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("✅ Dados divididos e normalizados:")
    print(f"• Conjunto de treino: {X_train.shape[0]} amostras")
    print(f"• Conjunto de teste: {X_test.shape[0]} amostras")
    print(f"• Dados normalizados (StandardScaler)")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

# Passo 3: Construir o Modelo
def construir_modelo(input_shape, num_classes):
    """Constrói o modelo de rede neural"""
    print("\n🧠 PASSO 3: CONSTRUINDO O MODELO DE REDE NEURAL")
    print("-" * 50)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,),                   kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    # Compilar o modelo
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("✅ Modelo construído com sucesso!")
    print("📊 Arquitetura da rede neural:")
    model.summary()
    
    return model

# Passo 4: Treinar o Modelo
def treinar_modelo(model, X_train, y_train, X_test, y_test):
    """Treina o modelo e mostra o progresso"""
    print("\n🎯 PASSO 4: TREINANDO O MODELO")
    print("-" * 50)
    
    # Callback para early stopping
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=10, restore_best_weights=True
    )
    
    # Treinar o modelo
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=16,
        validation_data=(X_test, y_test),
        callbacks=[early_stopping],
        verbose=1
    )
    
    print("✅ Treinamento concluído!")
    return history

# Passo 5: Avaliar o Modelo
def avaliar_modelo(model, X_test, y_test, history, iris):
    """Avalia o desempenho do modelo"""
    print("\n📈 PASSO 5: AVALIANDO O MODELO")
    print("-" * 50)
    
    # Avaliar a precisão
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"🎯 Acurácia no conjunto de teste: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
    
    # Fazer previsões
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    # Mostrar relatório de classificação
    print("\n📊 Relatório de Classificação:")
    print(classification_report(y_test, y_pred_classes, target_names=iris.target_names))
    
    # Plotar histórico de treinamento
    plotar_historico_treinamento(history)
    
    # Plotar matriz de confusão
    plotar_matriz_confusao(y_test, y_pred_classes, iris)
    
    return test_accuracy, y_pred_classes

# Funções de visualização
def plotar_historico_treinamento(history):
    """Plota o histórico de treinamento"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plotar acurácia
    ax1.plot(history.history['accuracy'], label='Acurácia Treino', color='#FF6B6B')
    ax1.plot(history.history['val_accuracy'], label='Acurácia Validação', color='#4ECDC4')
    ax1.set_title('Acurácia durante o Treinamento', fontweight='bold')
    ax1.set_xlabel('Época')
    ax1.set_ylabel('Acurácia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plotar loss
    ax2.plot(history.history['loss'], label='Loss Treino', color='#FF6B6B')
    ax2.plot(history.history['val_loss'], label='Loss Validação', color='#4ECDC4')
    ax2.set_title('Loss durante o Treinamento', fontweight='bold')
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plotar_matriz_confusao(y_test, y_pred_classes, iris):
    """Plota a matriz de confusão"""
    cm = confusion_matrix(y_test, y_pred_classes)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=iris.target_names, 
                yticklabels=iris.target_names)
    plt.title('Matriz de Confusão', fontweight='bold', fontsize=14)
    plt.ylabel('Verdadeiro')
    plt.xlabel('Predito')
    plt.show()

# Passo 6: Fazer Previsões
def fazer_previsoes(model, scaler, iris):
    """Faz previsões com novos dados"""
    print("\n🔮 PASSO 6: FAZENDO PREVISÕES COM NOVOS DADOS")
    print("-" * 50)
    
    # Dados de exemplo para previsão
    exemplos = np.array([
        [5.1, 3.5, 1.4, 0.2],  # Setosa
        [6.7, 3.0, 5.2, 2.3],  # Virginica
        [5.9, 3.0, 4.2, 1.5]   # Versicolor
    ])
    
    # Normalizar os dados
    exemplos_scaled = scaler.transform(exemplos)
    
    # Fazer previsões
    previsoes = model.predict(exemplos_scaled)
    classes_previstas = np.argmax(previsoes, axis=1)
    
    print("📋 Exemplos de previsões:")
    for i, (exemplo, classe) in enumerate(zip(exemplos, classes_previstas)):
        print(f"Exemplo {i+1}: {exemplo}")
        print(f"→ Classe prevista: {iris.target_names[classe]}")
        print(f"→ Probabilidades: {previsoes[i]}")
        print()

# Função principal
def main():
    """Função principal que executa todo o fluxo"""
    try:
        # Passo 1: Carregar dados
        X, y, iris, df_iris = carregar_dados()
        
        # Passo 2: Pré-processamento
        X_train, X_test, y_train, y_test, scaler = preprocessar_dados(X, y)
        
        # Passo 3: Construir modelo
        model = construir_modelo(X.shape[1], len(np.unique(y)))
        
        # Passo 4: Treinar modelo
        history = treinar_modelo(model, X_train, y_train, X_test, y_test)
        
        # Passo 5: Avaliar modelo
        accuracy, y_pred = avaliar_modelo(model, X_test, y_test, history, iris)
        
        # Passo 6: Fazer previsões
        fazer_previsoes(model, scaler, iris)
        
        print("=" * 60)
        print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

# Executar o programa
if __name__ == "__main__":
    # Verificar e instalar dependências se necessário
    try:
        import tensorflow as tf
    except ImportError:
        print("Instalando TensorFlow...")
        import subprocess
        subprocess.run(["pip", "install", "tensorflow", "scikit-learn", "pandas", "matplotlib", "seaborn"])
    
    main()