# Projeto SQLite para Gestão de imagens

Este projeto é um editor de imagens web interativo que permita ao utilizador criar, editar e manipular imagens diretamente no navegador. 

Esta aplicação permite funções básicas de edição, como redimensionamento, rotação, ajustes de brilho e contraste, e a criação de imagens do zero

## Estrutura do Projeto

A estrutura do diretório está organizada da seguinte forma:
```
/modulo_imagens
│── app.py  # Aplicação principal
│── /templates
│   │── index.html 
│   │── img.html 
│   │── about.html
│   │── paint.html  # Nova pagina para desenho
│── /static
│   │── /aigispics
│   │── /js
│       │── paint.js 
|
|──README.md
```
## Funcionalidades

o Carregar Imagens: O utilizador pode carregar imagens do seu dispositivo local através do
frontend.

o Edição de Imagens: O editor permite as seguintes funcionalidades de edição:

▪ Redimensionamento de imagem.

▪ Rotação da imagem.

▪ Ajuste de brilho e contraste.

▪ Aplicação de filtros básicos (como preto e branco, sepia, etc.).

▪ Adição de texto e formas geométricas simples (como linhas e círculos).

o Criação de Imagens: O utilizador pode criar imagens a partir do zero, utilizando ferramentas
de desenho (ex.: desenhar formas e escrever textos).

o Visualização de Resultados: O sistema deve permitir a visualização em tempo real das alterações
feitas na imagem antes de salvar.

o Salvar Imagens: O utilizador pode baixar as imagens editadas ou criadas diretamente no seu
dispositivo.

## Utilização

### Instalação

1. Certifica-te de que tens o Python instalado (versão 3.10+).
2. Instala os requisitos com:

   ```bash
   pip install -r requirements.txt

### Passos para Executar

1. Clone este repositório ou copie os ficheiros para o seu computador local.
2. Navegue até o diretório do projeto.
3. Execute o script principal para iniciar o servidor da página:

   ```bash
   python app.py
   ```


## Contribuições

Contribuições são bem-vindas! Por favor, abra uma *issue* ou envie um *pull request* se desejar sugerir melhorias ou adicionar novas funcionalidades.
