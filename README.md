# Criador de Fichas de RPG em Linha de Comando

Este é um projeto em Python para a criação e gerenciamento de fichas de personagens de RPG diretamente do terminal. O objetivo é oferecer uma ferramenta simples, rápida e extensível para jogadores que precisam criar uma ficha sem o uso de interfaces gráficas complexas.

## Funcionalidades

- **Criação Guiada de Fichas:** O programa guia o usuário passo a passo na criação do personagem, desde a escolha do sistema até a definição de atributos e perícias.
- **Múltiplos Sistemas:** A estrutura do projeto permite adicionar facilmente novos sistemas de RPG (como D&D, Call of Cthulhu, etc.) através de um dicionário de dados.
- **Salvar e Carregar:** As fichas podem ser salvas em formato `.json`, um formato de dados estruturado e legível, permitindo que sejam carregadas e utilizadas em sessões futuras.
- **Exportação para `.txt`:** Para facilitar a visualização e impressão, o programa oferece uma opção para exportar a ficha para um arquivo de texto (`.txt`) formatado de forma clara e organizada.
- **Interface de Menus:** A navegação é feita através de menus simples e intuitivos no terminal, tornando a experiência de uso direta e eficiente.

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.
2.  **Estrutura de Arquivos:** O projeto é composto por dois arquivos principais:
    -   `main.py`: Contém toda a lógica do programa.
    -   `Data_Sistemas.py`: Contém o dicionário `SISTEMAS` com os dados dos jogos.
3.  **Execução:** Abra o terminal na pasta onde os arquivos estão localizados e execute o seguinte comando:
    ```bash
    python main.py
    ```
4.  Siga as instruções exibidas no terminal para criar, carregar ou gerenciar suas fichas.

## Estrutura do Código

O código é organizado de forma modular, com funções específicas para cada tarefa:

-   **Funções de Interface (`escolher_opção`):** Gerenciam a interação com o usuário.
-   **Funções de Criação (`criar_ficha`, `escolher_sistema`, etc.):** Cuidam da lógica de construção dos dados da ficha.
-   **Funções de Arquivo (`salvarFicha`, `carregar_ficha`, `exportarTXT`):** Lidam com a leitura e escrita de arquivos.
-   **Funções de Menu (`menu`, `menuFicha`):** Controlam o fluxo de navegação do programa.

## Próximos Passos (Possíveis Melhorias)

-   [ ] Implementar uma função para **editar** uma ficha já carregada.
-   [ ] Expandir o arquivo `Data_Sistemas.py` com mais sistemas de RPG.
-   [ ] Adicionar validação de dados mais robusta (ex: limites para valores de atributos).
-   [ ] Criar um sistema de "rolagem de dados" para gerar atributos aleatoriamente.
-   [ ] Formatar o código para o sistem WEB de maneira editável a qualquer momento.
-   [ ] Adicionar outros elementos do atual sistema desenvolvido (D&D), como itens, armas, etc.
