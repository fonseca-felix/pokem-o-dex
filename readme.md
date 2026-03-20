# 🔴 Pokédex do F3l1z

[cite_start]Uma aplicação web moderna e responsiva construída com **Python (Flask)** que consome a [PokeAPI](https://pokeapi.co/) para exibir informações detalhadas sobre os Pokémon[cite: 1]. [cite_start]O projeto utiliza um sistema de cache interno para os primeiros 64 Pokémon, busca dinâmica por nome ou ID, e carregamento assíncrono (AJAX) para melhor performance[cite: 1].

## 🚀 Funcionalidades

* [cite_start]**Listagem Dinâmica:** Carregamento inicial de 64 Pokémon com sistema de "Carregar Mais" via API interna para otimizar o tráfego de dados[cite: 1].
* [cite_start]**Busca em Tempo Real:** Permite pesquisar Pokémon específicos pelo nome ou número oficial da Pokédex[cite: 1].
* **Página de Detalhes Completa:** Inclui informações detalhadas como:
    * **Estatísticas Base:** HP, Ataque, Defesa, Ataque Especial, Defesa Especial e Velocidade exibidos com barras de progresso visuais.
    * **Descrição Traduzida:** Busca descrições oficiais com prioridade para o idioma Português (PT/PT-BR).
    * **Dados Físicos:** Exibição de altura e peso convertidos para o sistema métrico.
* **Linha Evolutiva:** Visualização completa da cadeia de evolução de cada Pokémon diretamente na página de detalhes.
* **Cache de Performance:** Dados básicos dos primeiros 64 Pokémon (Kanto) pré-carregados para navegação instantânea.
* **Interface Responsiva:** Design limpo e adaptável para dispositivos móveis e desktops utilizando CSS Grid e Flexbox.

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Backend:** [Flask](https://flask.palletsprojects.com/) (Python 3.12)[cite: 1].
* **Frontend:** HTML5, CSS3 (Variáveis, Grid, Flexbox) e JavaScript puro (Fetch API).
* **API Externa:** [PokeAPI](https://pokeapi.co/).
* **Deployment:** Configurado para [Vercel](https://vercel.com/) via `@vercel/python`.

## 📂 Estrutura do Projeto

* [cite_start]`app.py`: Gerencia as rotas principais (Home, Detalhes e API de paginação)[cite: 1].
* `funcoes.py`: Contém a lógica de consumo da PokeAPI e processamento de dados.
* `cache_data.py`: Armazena dados estáticos e estruturas iniciais para os primeiros 64 Pokémon.
* `static/style.css`: Estilização completa, incluindo cores temáticas por tipo de Pokémon.
* `templates/`: Arquivos HTML utilizando o motor de busca Jinja2.
* `vercel.json`: Arquivo de configuração para hospedagem na plataforma Vercel.

## 🔧 Como Executar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/pokedex-f3l1z.git](https://github.com/seu-usuario/pokedex-f3l1z.git)
    cd pokedex-f3l1z
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Inicie o servidor:**
    ```bash
    python app.py
    ```

4.  **Acesse no navegador:**
    `http://127.0.0.1:5000`

---
**Desenvolvido com ⚡ por F3l1z**
