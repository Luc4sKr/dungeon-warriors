# dungeon-warriors

O projeto dungeon-warriors é dividido em 3 outros projetos:

- [Requisitos AV6](#requisitos-av6)
- [Backend](#backend)
- [Frontend](#frontend)
- [Game](#game)

## Requisitos AV6

Para atender aos requisitos da avaliação AV6, o projeto contemplou:

- Organização do repositório por pastas, cada uma indicando um projeto específico.
- Continuação do projeto original e criação de um "remake" do jogo utilizando a game engine Godot (disponível em dungeon-warriors-II).
- Implementação de upload de imagens no sistema, permitindo a listagem das mesmas.
- Utilização das seguintes tecnologias para estilização do frontend: [MUI](https://mui.com/material-ui/getting-started/) e [styled components](https://styled-components.com/)

## Backend

O backend foi feito em Python usando o frameword Flask seguindo o padrao de REST API

### Como rodar

#### Windows

``` shell
cd backend && python server.py
```

## Frontend

O frontend foi feito usando a biblioteca React + Vite + TypeScript

### Como rodar

``` shell
cd frontend && npm run build
```

## Game

O Jogo foi feito em Python utilizando a biblioteca Pygame

### Como rodar

Para rodar o jogo primeiro é necessário estar rodando o backend pois o jogo necessita do backend para funcionar

#### Windows

``` shell
cd game && python main.py
```

