<div align="center">

<img src="../U1_A3_CARACTERISTICAS_DOS_SISTEMAS_OPERACIONAIS/images/logo_linux_sem_fundo.png" min-width="50px" width="80" min-height="50px" height="80px" alt="Logo Sistemas Operacionais">

<img src="../U1_A3_CARACTERISTICAS_DOS_SISTEMAS_OPERACIONAIS/images/logo_windows_sem_fundo.png" min-width="50px" width="120" min-height="50px" height="120px" alt="Logo Sistemas Operacionais">

</div>

# Atividade Prática: Monoprogramação sem Troca de Processos ou Paginação

## Disciplina: Sistemas Operacionais

### Unidade 4 – Aula 3

Ministrado por _Profº Me. Rômulo de Almeida Neves_.
<br>

Abaixo segue o resultado da atividade concluída:
<br>

> 🎯 Objetivo:
>
> - Compreensão, análise e aplicações relacionados a `paginação` em sistemas operacionais.
> - Explorar os conceitos de `memória virtual` e `gerência de memória` através do simulador **_[SOsim](https://www.training.com.br/sosim/)_**.
> - Configurar e analisar `políticas de busca de páginas antecipada`.
> - Visualizar `tabelas de páginas e bits de validade` em processos CPU-bound. ✅

<br>

### 🧩 Features

- Download e configuração do simulador SOsim para estudos avançados
- Configuração de escalonamento circular e políticas de memória virtual
- Criação e análise de processos CPU-bound com paginação ativa
- Ativação e monitoramento da janela de arquivos de paginação
- Visualização detalhada da tabela de páginas através do Contexto do Processo
- Análise dos bits de validade nas entradas das tabelas de páginas (ETP)
- Configuração de parâmetros avançados do sistema

---

<table align="center">
  <tr>
    <td align="center">
      <a href="./images/sosim_config_processador.png">
        <img src="./images/sosim_config_processador.png" width="250px" height="250px" alt="Configuração Processador"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_config_memoria.png">
        <img src="./images/sosim_config_memoria.png" width="250px" height="250px" alt="Configuração Memória"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_paginacao.png">
        <img src="./images/sosim_paginacao.png" width="250px" height="250px" alt="Janela Paginação"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_tabela_paginas.png">
        <img src="./images/sosim_tabela_paginas.png" width="250px" height="250px" alt="Tabela de Páginas"/>
      </a>
    </td>
  </tr>
</table>
<table align="center">
  <tr>
    <td align="center">
      <a href="./images/sosim_processo_cpu_bound.png">
        <img src="./images/sosim_processo_cpu_bound.png" width="250px" height="250px" alt="Processo CPU-bound"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_bits_validacao.png">
        <img src="./images/sosim_bits_validacao.png" width="250px" height="250px" alt="Bits de Validação"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_console.png">
        <img src="./images/sosim_console.png" width="250px" height="250px" alt="Console SOsim"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/sosim_gerencia_processos.png">
        <img src="./images/sosim_gerencia_processos.png" width="250px" height="250px" alt="Gerência de Processos"/>
      </a>
    </td>
  </tr>
</table>

---

### 📚 Pré-requisitos

- [ ] Antes de iniciar esta atividade, você deve ter conhecimento básico nas seguintes áreas:
      <br>

- **Conceitos de Memória Virtual:** Noções de paginação e memória virtual.
- **SOsim Básico:** Familiaridade com a interface do simulador.
- **Processos e Estados:** Compreensão de processos CPU-bound e seus estados.
- **Tabelas de Páginas:** Conceitos básicos de organização de memória.
- **Bits de Controle:** Noções de bits de validade e proteção.

---

### 🛠️ Tecnologias Utilizadas

A Atividade foi desenvolvida utilizando:

[![SOsim](https://img.shields.io/badge/-SOsim-333333?style=flat&logo=windowsterminal&logoColor=4D4D4D)](http://www.training.com.br/sosim/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Windows](https://img.shields.io/badge/-Windows-333333?style=flat&logo=windows&logoColor=0078D6)](https://www.microsoft.com/pt-br/windows/?r=1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Memória Virtual](https://img.shields.io/badge/-Memória_Virtual-333333?style=flat&logo=memory&logoColor=FF6B35)](http://www.training.com.br/sosim/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Paginação](https://img.shields.io/badge/-Paginação-333333?style=flat&logo=layers&logoColor=00AAFF)](https://pt.wikipedia.org/wiki/Paginação)

---

#### ⚙️ Configuração e Execução

- [x] &nbsp;&nbsp;&nbsp;Pré-requisitos:

✔️ - Download do SOsim em: http://www.training.com.br/sosim/
✔️ - Sistema Windows para execução do simulador.
✔️ - Conhecimento prévio de conceitos de paginação.

- [x] &nbsp;&nbsp;&nbsp;Configuração Inicial do SOsim:

```bash
# 1. Fazer download e executar o SOsim
# 2. Configurar Escalonamento Circular:
#    Console SOsim → Opções → Parâmetros do Sistema → Guia Processador

# 3. Configurar política de busca de páginas antecipada:
#    Console SOsim → Opções → Parâmetros do Sistema → Guia Memória

# 4. Reiniciar o simulador para aplicar as configurações

---

#### 🔬 Testes

✔️ - Testes práticos realizados:

- [x] &nbsp;&nbsp;&nbsp; Identificação correta da versão do kernel no Linux.
- [x] &nbsp;&nbsp;&nbsp; Listagem de processos ativos em ambos os sistemas.
- [x] &nbsp;&nbsp;&nbsp; Criação e configuração de permissões de arquivos.
- [x] &nbsp;&nbsp;&nbsp; Exploração da estrutura de diretórios raiz.
- [x] &nbsp;&nbsp;&nbsp; Comparação entre /home, /etc, /var (Linux) e C:\Users, C:\Windows (Windows).
- [x] &nbsp;&nbsp;&nbsp; Verificação de permissões aplicadas.

---

### 🧠 Habilidades Desenvolvidas

✔️ Ao concluir esta atividade, você terá adquirido as seguintes habilidades e sub-habilidades :

- Compreensão das funções do kernel e shell em sistemas operacionais.
- Habilidade em comandos essenciais do terminal Linux e PowerShell.
- Gerenciamento de permissões de arquivos e diretórios.
- Conhecimento da estrutura de sistemas de arquivos Linux e Windows.
- Capacidade de comparar arquiteturas de diferentes sistemas operacionais.
- Habilidade em troubleshooting básico de sistemas.
- Entendimento de ambientes multiusuário e segurança de acesso.

---

#### 📜 Licença

Por se tratar de um projeto de caráter exclusivamente acadêmico, desenvolvido como atividade prática da disciplina de Sistemas Operacionais, ainda não foi atribuída uma licença formal de software (como MIT, GPL ou outra).

O material tem finalidade educativa e de portfólio estudantil, sendo destinado apenas ao aprendizado e à avaliação no âmbito da faculdade. Caso deseje reutilizar ou adaptar o conteúdo para fins didáticos, sinta-se à vontade — apenas mantenha a referência ao autor original e ao contexto acadêmico..

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

[⬆ Voltar ao topo](#atividade-prática-características-dos-sistemas-operacionais)
```
