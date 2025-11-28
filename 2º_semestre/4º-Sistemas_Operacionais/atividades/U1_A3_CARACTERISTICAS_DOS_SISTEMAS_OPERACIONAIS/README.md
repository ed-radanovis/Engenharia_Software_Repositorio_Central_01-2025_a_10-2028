<div align="center">

<img src="./images/logo_linux_sem_fundo.png" min-width="50px" width="80" min-height="50px" height="80px" alt="Logo Sistemas Operacionais">

<img src="./images/logo_windows_sem_fundo.png" min-width="50px" width="120" min-height="50px" height="120px" alt="Logo Sistemas Operacionais">

</div>

# Atividade Prática: Características dos Sistemas Operacionais

## Disciplina: Sistemas Operacionais

### Unidade 1 – Aula 3

Ministrado por _Profº Me. Rômulo de Almeida Neves_.
<br>

Abaixo segue o resultado da atidade concluída:

> <br>
> 🎯 Objetivo:
>
> - Desenvolver a compreensão dos principais componentes dos sistemas operacionais **_[Linux](https://www.linux.org/)_** e **_[Windows](https://www.microsoft.com/pt-br/windows/?r=1)_**.
> - Explorar o `kernel` , `shell` e `gerenciamento de arquivos` nos sistemas operacionais.
> - Aprender sobre organização do sistema de arquivos e configuração de permissões.
> - Comparar estruturas de diretórios entre `Linux` e `Windows`. ✅

<br>

### 🧩 Features

- Identificação de versão do kernel nos sistemas Linux e Windows
- Listagem de processos ativos em ambos os sistemas operacionais
- Criação e gerenciamento de permissões de arquivos e diretórios
- Exploração da estrutura de diretórios raiz e principais pastas
- Comparação das arquiteturas de sistemas de arquivos Linux vs Windows

---

<table align="center">
  <tr>
    <td align="center">
      <a href="./images/linux_1.png">
        <img src="./images/linux_1.png" width="250px" height="250px" alt="print da atividade"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/linux_2.png">
        <img src="./images/linux_2.png" width="250px" height="250px" alt="print da atividade"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/linux_3.png">
        <img src="./images/linux_3.png" width="250px" height="500px" alt="print da atividade"/>
      </a>
    </td>
    <td align="center">
      <a href="./images/windows_1.0.png">
        <img src="./images/windows_1.0.png" width="250px" height="500px" alt="print da atividade"/>
      </a>
    </td>
  </tr>
</table>

---

### 📚 Pré-requisitos

- [ ] Antes de iniciar este projeto, você deve ter conhecimento básico nas seguintes áreas:
      <br>

- **HTML Básico :** Estrutura semântica de páginas web, tags fundamentais (`<header>` , `<nav>` , `<ul>` , `<li>`), e atributos.
- **CSS Intermediário :** Seletores, box model, Flexbox/Grid, media queries, e propriedades de animação / transição.
- **JavaScript Essencial :** Manipulação do DOM, eventos (click, mouseover), funções, e condicionais.
- **Design Responsivo :** Conceitos de breakpoints, mobile-first, e adaptação a diferentes tamanhos de tela.
- **Acessibilidade Web :** Noções básicas de ARIA attributes e navegação por teclado.

---

### ✨ Ajustes e melhorias

O proposta da atividade foi totalmente concluída, o que Inclui a HomePage e AboutPage.

> 📝 Nota: As demais pages não foram criadas por questões de gestão de tempo, e serão criadas posteriormente.

---

### 🛠️ Tecnologias Utilizadas

A Atvidade foi desenvolvida utilizando:

- [x] **Frontend**:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![HTML5](https://img.shields.io/badge/-HTML5-333333?style=flat&logo=HTML5)](https://developer.mozilla.org/en-US/docs/Web/HTML) &nbsp;&nbsp;[<img src="https://raw.githubusercontent.com/ed-radanovis/Soft-App-Memes-Machine-DIO-11-2022/refs/heads/master/assets/github/mini_logo_css.png" width="16px" alt="CSS Icon">![CSS](https://img.shields.io/badge/-CSS-333333?style=flat&logo=CSS3&logoColor=1572B6)](https://developer.mozilla.org/en-US/docs/Web/CSS)&nbsp;&nbsp;[![JavaScript](https://img.shields.io/badge/-JavaScript-333333?style=flat&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
      <br>

- [x] **Ferramentas de Desenvolvimento e Testes**:&nbsp;&nbsp;&nbsp;[<img src="https://raw.githubusercontent.com/ed-radanovis/Soft-App-Memes-Machine-DIO-11-2022/refs/heads/master/assets/github/mini_logo_liveserver.png" width="21px" alt="Live Server Icon">![Live Server](https://img.shields.io/badge/-Live%20Server-333333?style=flat&logo=live-server)](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)&nbsp;&nbsp;`Manual testing with Browser DevTools`
      <br>

- [x] **Hospedagem e Implantação**:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![GitHub Pages](https://img.shields.io/badge/-GitHub%20Pages-333333?style=flat&logo=github&logoColor=ffffff)](https://pages.github.com/)
      <br>

- [x] **Planejamento e Edição**:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Figma](https://img.shields.io/badge/-Figma-333333?style=flat&logo=figma&logoColor=007ACC)](https://figma.com/)&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/ed-radanovis/Soft-App-Memes-Machine-DIO-11-2022/6c046ddb9cd516f3cea41a8abbb1318fc3e6d8d1/assets/github/mini_logo_vscode.png" width="21px" alt="VS Code Icon">[![Visual Studio Code](https://img.shields.io/badge/-Visual_Studio_Code-333333?style=flat&logo=visual-studio-code&logoColor=007ACC)](https://code.visualstudio.com/)
      <br>

#### ⚙️ Etapas do projeto

✔️ - Planejamento: O projeto foi estruturado com foco em um miniaplicativo funcional, **evitando dependências complexas** e priorizando um código limpo e **de fácil manutenção**.<br>
✔️ - Configurar o ambiente:

- [ ] Se desejar, clone o repositório:

```bash

📝 Nota => Método recomendado - para clonar apenas este diretório e não todo o repositório :

git clone --depth 1 --filter=blob:none --sparse https://github.com/ed-radanovis/Engenharia_Software_Repositorio_Central_01-2025_a_10-2028.git
cd Engenharia_Software_Repositorio_Central_01-2025_a_10-2028
git sparse-checkout set "1º_semestre/1º-Desenvolvimento_Responsivo_disciplina_isolada/atividades/Frontend_com_Framework_HTML_CSS_JS"
```

- [ ] Navegue até a pasta do projeto: `cd Frontend_com_Framework_HTML_CSS_JS` ou a pasta que você criou e nomeou.

---

#### 🖥️ Frontend

✔️ - Navegue até a raiz do projeto: onde estão localizados os arquivos `index.html`, `src/css/`, `src/js/` e `src/images/`.<br>
✔️ - Certifique-se de que as dependências estejam disponíveis:

- [x] &nbsp;&nbsp;&nbsp;Baixe bibliotecas externas como `typed.js`, `jquery`, `jquery-easing` e `ionicons`, conforme os links no cabeçalho (`<head>`) do arquivo `index.html`.

- [x] &nbsp;&nbsp;&nbsp;Certifique-se de que a pasta `src/images/` contenha os recursos necessários (por exemplo, `background.png`, `logo.png`, `mascote.png`, etc.).

✔️ - Abra o arquivo `index.html` diretamente no navegador ou hospede-o no `GitHub Pages`.<br>

---

#### 🌐 Implantação

✔️ - Hospedagem no GitHub Pages (plano gratuito):

- [x] &nbsp;&nbsp;&nbsp; Acesse o [GitHub](https://github.com).
- [x] &nbsp;&nbsp;&nbsp; Navegue até o seu repositório (por exemplo, `https://github.com/repository-created-by-you`).
- [x] &nbsp;&nbsp;&nbsp; Habilite o GitHub Pages: Acesse as configurações do repositório, role até a seção **_`"Pages"`_**, selecione a branch (por exemplo, `main` ou `gh-pages`) e defina o diretório raiz como `/` (raiz do projeto).
- [x] &nbsp;&nbsp;&nbsp; Suba e acesse a URL gerada (por exemplo, `https://seu-nome-de-usuário.github.io/nome-do-repositório/`).

✔️ - Hospedagem opcional no Render (plano gratuito):

- [ ] &nbsp;&nbsp;&nbsp; Acesse o [Render](https://render.com).
- [ ] &nbsp;&nbsp;&nbsp; Crie um novo Site Estático e conecte-o ao repositório `https://github.com/repository-created-by-you`.
- [ ] &nbsp;&nbsp;&nbsp; Defina o diretório raiz como `/` (raiz do projeto).
- [ ] &nbsp;&nbsp;&nbsp; Suba e acesse a URL gerada (por exemplo, `https://nome-do-seu-aplicativo.onrender.com`).

---

#### 🔬 Testes

✔️ - Testes Manuais:

- [x] &nbsp;&nbsp;&nbsp; Verifique o comportamento responsivo com as Ferramentas de Desenvolvedor (F12 > Alternar Barra de Ferramentas do Dispositivo) ou outra ferramenta de sua escolha, para simular em smartphones (largura máxima: 885px), tablets (886px-1024px), telas Full HD (1920px+) e 4K (3840px+).
- [x] &nbsp;&nbsp;&nbsp; Teste a alternância do menu hambúrguer e as interações do submenu em dispositivos móveis.
- [x] &nbsp;&nbsp;&nbsp;Verifique os recursos de acessibilidade (por exemplo, tags semânticas, navegação por teclado, Acesso Não Visual à Área de Trabalho (NVDA)) usando as Ferramentas de Desenvolvedor do Navegador, garantindo compatibilidade e usabilidade.

---

#### 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

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

[⬆ Voltar ao topo](#projeto---atividade-prática-construção-de-front-end-baseado-em-framework)
