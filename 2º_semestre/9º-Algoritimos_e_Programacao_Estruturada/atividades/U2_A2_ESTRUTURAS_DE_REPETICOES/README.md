  <p align="center">
    <img src="../U1_A4_OPERADORES_E_EXPRESSOES/images/logo_linguagem_C_redondo.png" min-width="100px" width="100" min-height="100px" height="100px" alt="logo Python">
  </p>

# Projeto - Atividade Prática: Estruturas de Repetição While em C

## Disciplina: Algoritmos e Programação Estruturada

### Unidade 2 – Aula 2

Ministrado por _Dr. Gilberto Fernandes Junior_.

<br>

Abaixo segue o resultado do projeto concluído:

<br>

> 🎯 Objetivo da Atividade:
>
> - Compreender o funcionamento da estrutura de repetição `while` em linguagem de programação **_[C](https://en.cppreference.com/)_**.
> - Implementar um programa que utiliza laços de repetição para resolver problemas práticos.
> - Desenvolver habilidades no `controle de loops` baseados em condições.
> - Aprender a utilizar `valores sentinela` para encerramento de programas.

<br>

### 🧩 Features

- Leitura contínua de números inteiros via entrada do usuário.
- Implementação de estrutura de repetição while com condição de parada.
- Cálculo acumulativo de soma em tempo real.
- Utilização do número zero como valor sentinela.
- Interface interativa com feedback imediato.
- Exibição do resultado final após encerramento.

---

<table align="center">
  <tr>
    <td align="center">
      <a href="./images/result_activity_1.png">
        <img src="./images/result_activity_1.png" width="500px" height="800px" alt="print da atividade"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/result_activity_2.png">
        <img src="./images/result_activity_2.png" width="500px" height="800px" alt="print da atividade"/>
      </a>
    </td>
  </tr>  
</table>

---

### 📚 Pré-requisitos

- [ ] Antes de iniciar este projeto, você deve ter conhecimento básico nas seguintes áreas:

- **Linguagem C Básica:** Sintaxe, estrutura main, variáveis e tipos de dados.
- **Entrada/Saída:** Comandos printf e scanf para interação com usuário.
- **Estruturas Condicionais:** Compreensão de if-else para lógica básica.
- **Operadores Relacionais:** Uso de operadores como != (diferente).
- **OnlineGDB:** Familiaridade com a plataforma online.

---

### 🛠️ Tecnologias Utilizadas

A Atividade foi desenvolvida utilizando:

[![C Language](https://img.shields.io/badge/-Linguagem_C-333333?style=flat&logo=c&logoColor=A8B9CC)](https://en.cppreference.com/w/c/language)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<img src="https://github.com/ed-radanovis/Engenharia_Software_Repositorio_Central_01-2025_a_10-2028/blob/c7eac2d5a0cf3eefc1a3a4b51594e284a89f6d30/2%C2%BA_semestre/9%C2%BA-Algoritimos_e_Programacao_Estruturada/atividades/U1_A4_OPERADORES_E_EXPRESSOES/images/mini_logo_onlinegdb.png" width="20px" alt="OnlineGDB Icon">![OnlineGDB](https://img.shields.io/badge/-OnlineGDB-333333?style=flat&logo=gnu-debugger&logoColor=FF6B6B)](https://www.onlinegdb.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![GCC Compiler](https://img.shields.io/badge/-GCC_Compiler-333333?style=flat&logo=gnu&logoColor=FF6B6B)](https://gcc.gnu.org/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/ed-radanovis/Engenharia_Software_Repositorio_Central_01-2025_a_10-2028/blob/772cfa927b7993ea3592c099b8e89a9f9f612444/2%C2%BA_semestre/5%C2%BA-Linguagem_de_Programacao/atividades/U1_A4_FUNCOES_EM_PYTHON/images/mini_logo_vscode.png" width="21px" alt="VS Code Icon">[![Visual Studio Code](https://img.shields.io/badge/-Visual_Studio_Code-333333?style=flat&logo=visual-studio-code&logoColor=007ACC)](https://code.visualstudio.com/)

---

### 📂 Estrutura do Projeto

```bash
U2_A2_ESTRUTURAS_DE_REPETICOES/
├── images/
│   ├── estrutura_while.png
│   ├── entrada_dados.png
│   ├── calculo_soma.png
│   ├── resultado_final.png
│   └── logo_c.png
├── src/
│   └── soma_while.c                    # Código principal da atividade
├── ATIVIDADE_PRATICA_U2_A2_ESTRUTURAS_REPETICAO.pdf
├── README.md                           # Este arquivo
└── roteiro_U2_A2_ESTRUTURAS_DE_REPETICOES.pdf
```

---

### ⚙️ Configuração e Execução

- [ ] &nbsp;&nbsp;&nbsp;Pré-requisitos:

✔️ - Python 3.6+ ou Google Colab.

<br>

- [ ] &nbsp;&nbsp;&nbsp;Acesso à internet para instalação das bibliotecas.
- Para rodar localmente (opcional):

```bash
cd U4_A4_MACHINE_LEARNING_COM_PYTHON/src
python unit_four_lesson_four_machine_learning.py
```

<br>

- [x] &nbsp;&nbsp;&nbsp;Forma recomendada (conforme roteiro da disciplina) ➡ Abra o Google Colab, crie um novo notebook e implemente o sistema seguindo os passos:

```python
# Passo 1: Importar Bibliotecas e Carregar Dados
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data  # Características: comprimento/largura sépalas e pétalas
y = iris.target  # Espécies: 0=Setosa, 1=Versicolor, 2=Virginica

# Passo 2: Pré-processamento dos Dados
# Dividir em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Passo 3: Construir o Modelo de Rede Neural
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # 3 classes de saída
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Passo 4: Treinar o Modelo
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=1)

# Passo 5: Avaliar o Modelo
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Acurácia no conjunto de teste: {test_accuracy:.2f}")

# Passo 6: Fazer Previsões
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
```

---

### 🔬 Testes Realizados

✔️ - Testes manuais :

- [x] &nbsp;&nbsp;&nbsp;Carregamento correto do dataset Iris do Scikit-learn.
- [x] &nbsp;&nbsp;&nbsp;Divisão adequada dos dados em treino e teste (80/20).
- [x] &nbsp;&nbsp;&nbsp;Normalização eficaz com StandardScaler.
- [x] &nbsp;&nbsp;&nbsp;Construção da arquitetura da rede neural com camadas densas.
- [x] &nbsp;&nbsp;&nbsp;Treinamento do modelo com 100 épocas e validação.
- [x] &nbsp;&nbsp;&nbsp;Avaliação da acurácia no conjunto de teste (>90%).
- [x] &nbsp;&nbsp;&nbsp;Previsões consistentes para novas amostras.

---

### 🧠 Habilidades Desenvolvidas

✔️ - Ao concluir esta atividade, você terá adquirido as seguintes habilidades e sub-habilidades :

- Compreensão dos fundamentos de Machine Learning e redes neurais.
- Manipulação de datasets clássicos para problemas de classificação.
- Implementação de pré-processamento com Scikit-learn.
- Construção de arquiteturas de redes neurais com TensorFlow/Keras.
- Treinamento e avaliação de modelos de deep learning.
- Interpretação de métricas de performance (acurácia, loss).
- Realização de previsões com modelos treinados.
- Habilidade em otimização de hiperparâmetros e arquiteturas..

---

### 📜 Licença

Por se tratar de um projeto de caráter exclusivamente acadêmico, desenvolvido como atividade prática da disciplina de Linguagem de Programação, ainda não foi atribuída uma licença formal de software (como MIT, GPL ou outra).

O código tem finalidade educativa e de portfólio estudantil, sendo destinado apenas ao aprendizado e à avaliação no âmbito da faculdade. Caso deseje reutilizar ou adaptar o material para fins didáticos, sinta-se à vontade — apenas mantenha a referência ao autor original e ao contexto acadêmico.

---

<h4 align="center">
  👨‍💻 Desenvolvido por 
<h4/>
<br>

<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/edmar-radanovis/">
        <img src="/github/foto perfil (4).jpeg" width="100px" height="120px" alt="foto de perfil"/><br>
        <sub><b>Edmar Radanovis</b></sub><br>
        <sub>Desenvolvedor Full Stack &nbsp;&</sub><br>
        <sub>Bacharelando em</sub><br>
        <sub>Engenharia de Software</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://edwebdev.vercel.app/">
        <img src="/github/Logo_EWD_APEX_rounded-sem_fundo.png" width="200px" height="200px" alt="Logo EWD Apex"/><br>
        <sub><b>Ed Web Dev</b></sub><br>
      </a>
    </td>
  </tr>
</table>
<br>
<br>

[⬆ Voltar ao topo](#projeto---atividade-prática-machine-learning-com-python)
