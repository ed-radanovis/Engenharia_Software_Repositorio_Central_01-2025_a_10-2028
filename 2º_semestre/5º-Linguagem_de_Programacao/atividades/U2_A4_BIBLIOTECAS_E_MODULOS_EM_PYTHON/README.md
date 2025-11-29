  <p align="center">
    <img src="../U1_A4_FUNCOES_EM_PYTHON/images/logo_python2.png" min-width="100px" width="150" min-height="100px" height="150px" alt="logo Python">
  </p>

# Projeto - Atividade Prática: Bibliotecas e Módulos em Python

## Disciplina : Linguagem de Programação

### Unidade 2 – Aula 4

Ministrado por _Profº Anderson I. S. Abreu_.

<br>

Abaixo segue o resultado do projeto concluído:

<br>

> 🎯 Objetivo da Atividade:
>
> - Compreender a importância dos `recursos` de **_[Python](https://www.python.org/)_** como `bibliotecas` e `módulos`.
> - Aplicar `Programação Orientada a Objetos` com classes e métodos em um cenário realista.
> - Desenvolver um `sistema de gerenciamento de biblioteca` com cadastro, busca e relatórios.
> - Utilizar a biblioteca `Matplotlib` para geração de gráficos e visualização de dados.

<br>

### 🧩 Features

- Definição de classe **Livro** com atributos: título, autor, gênero e quantidade
- Cadastro de novos livros no sistema da biblioteca
- Listagem completa de todos os livros disponíveis
- Busca inteligente de livros por título
- Geração de gráfico de quantidade de livros por gênero
- Interface intuitiva no Google Colab para execução interativa
- Validação de dados e tratamento de entradas

---

<table align="center">
  <tr>
    <td align="center">
      <a href="./images/result_activity_1.png">
        <img src="./images/result_activity_1.png" width="500px" height="600px" alt="print da atividade"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/result_activity_2.png">
        <img src="./images/result_activity_2.png" width="500px" height="600px" alt="print da atividade"/>
      </a>
    </td>
  </tr>
</table>
---

### 📚 Pré-requisitos

- [ ] Antes de iniciar este projeto, você deve ter conhecimento básico nas seguintes áreas:
      <br>

- **Programação Orientada a Objetos:** Conceitos de classes, objetos, atributos e métodos.
- **Python Intermediário:** Sintaxe da linguagem, listas, dicionários e funções.
- **Estruturas de Dados:** Manipulação de listas e iteração com loops.
- **Bibliotecas Python:** Instalação e importação de módulos externos.
- **Google Colab:** Ambiente de desenvolvimento em nuvem para execução de código.

---

### 🛠️ Tecnologias Utilizadas

A Atividade foi desenvolvida utilizando:

[![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python&logoColor=3776AB)](https://www.python.org/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Google Colab](https://img.shields.io/badge/-Google_Colab-333333?style=flat&logo=google-colab&logoColor=F9AB00)](https://colab.research.google.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/ed-radanovis/Engenharia_Software_Repositorio_Central_01-2025_a_10-2028/blob/772cfa927b7993ea3592c099b8e89a9f9f612444/2%C2%BA_semestre/5%C2%BA-Linguagem_de_Programacao/atividades/U1_A4_FUNCOES_EM_PYTHON/images/mini_logo_vscode.png" width="21px" alt="VS Code Icon">[![Visual Studio Code](https://img.shields.io/badge/-Visual_Studio_Code-333333?style=flat&logo=visual-studio-code&logoColor=007ACC)](https://code.visualstudio.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=python&logoColor=3776AB)](https://matplotlib.org/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![POO](https://img.shields.io/badge/-Programação_Orientada_a_Objetos-333333?style=flat&logo=blueprint&logoColor=FFD700)](https://pt.wikipedia.org/wiki/Programação_orientada_a_objetos)

---

### 📂 Estrutura do Projeto

```bash
U2_A4_BIBLIOTECAS_E_MODULOS_EM_PYTHON/
├── images/
│   ├── result_activity_1.png
│   └── result_activity_2.png
├── src/
│   └── unit_two_lesson_four_libraries_and_modules.py             # Código principal da atividade
├── ATIVIDADE_PRATICA_U2_A4_BIBLIOTECAS_E_MODULOS_EM_PYTHON.pdf
├── README.md                                                     # Este arquivo
└── roteiro_U2_A4_BIBLIOTECAS_E_MODULOS_EM_PYTHON.pdf
```

---

### ⚙️ Configuração e Execução

- [ ] &nbsp;&nbsp;&nbsp;Pré-requisitos:
      ✔️ - Python 3.6+ ou Google Colab.

<br>

- [ ] &nbsp;&nbsp;&nbsp;Acesso à internet para instalação da Matplotlib.
- Para rodar localmente (opcional):

```bash
cd U2_A4_BIBLIOTECAS_MODULOS_PYTHON
python sistema_biblioteca.py
```

<br>

- [x] &nbsp;&nbsp;&nbsp;Forma recomendada (conforme roteiro da disciplina) :
      &nbsp;&nbsp;&nbsp;Abra o Google Colab, crie um novo notebook e implemente o sistema seguindo os passos:

```python
      # Passo 1: Instalar e importar bibliotecas
!pip install matplotlib
import matplotlib.pyplot as plt

      # Passo 2: Definir classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} | Gênero: {self.genero} | Disponível: {self.quantidade}"

      # Passo 3: Implementar funções do sistema
biblioteca = []

def cadastrar_livro(titulo, autor, genero, quantidade):
    # Implementação da função
    pass

def listar_livros():
    # Implementação da função
    pass

def buscar_livro(titulo):
    # Implementação da função
    pass

def gerar_grafico_generos():
    # Implementação da função
    pass
```

---

### 🔬 Testes Realizados

✔️ - Testes manuais :

- [x] &nbsp;&nbsp;&nbsp;Cadastro de múltiplos livros com diferentes gêneros.
- [x] &nbsp;&nbsp;&nbsp;Listagem completa de todos os livros cadastrados.
- [x] &nbsp;&nbsp;&nbsp;Busca por título (casos: encontrado e não encontrado).
- [x] &nbsp;&nbsp;&nbsp;Geração correta do gráfico de livros por gênero.
- [x] &nbsp;&nbsp;&nbsp;Validação de entradas e tratamento de dados.
- [x] &nbsp;&nbsp;&nbsp;Teste de instalação e importação da Matplotlib.

---

### 🧠 Habilidades Desenvolvidas

✔️ Ao concluir esta atividade, você terá adquirido as seguintes habilidades e sub-habilidades :

- Criação e utilização de classes em Python (Programação Orientada a Objetos).
- Implementação de sistemas de gerenciamento de dados com listas e objetos.
- Manipulação e visualização de dados com a biblioteca Matplotlib.
- Desenvolvimento de funções modulares para operações específicas.
- Habilidade em buscar e filtrar dados em estruturas complexas.
- Geração de relatórios visuais com gráficos personalizados.
- Boas práticas de organização de código e documentação.
- Experiência com ambientes de desenvolvimento em nuvem (Google Colab).

---

### 📜 License

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

[⬆ Voltar ao topo](#projeto---atividade-prática-bibliotecas-e-módulos-em-python)
