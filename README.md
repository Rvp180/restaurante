# Sistema de Reservas de Restaurante

## Descrição
Este é um projeto simples para um **sistema de reservas de restaurante**. Ele permite que os clientes façam reservas de mesas, visualizem as reservas existentes, atualizem ou cancelem reservas. O sistema utiliza o conceito de **Programação Orientada a Objetos (POO)** para gerenciar as reservas e oferece uma interface simples para interação com o usuário.

## Funcionalidades

- **Adicionar Reserva:** Permite ao usuário registrar uma nova reserva com dados como nome do cliente, data e hora, número de pessoas e número da mesa.
- **Listar Reservas:** Exibe todas as reservas registradas, com informações detalhadas sobre cada uma.
- **Atualizar Reserva:** Permite atualizar uma reserva existente, incluindo alterações no nome do cliente, data, número de pessoas ou mesa.
- **Cancelar Reserva:** Exclui uma reserva existente, tornando a mesa disponível para outros clientes.

## Como Funciona

### 1. Cadastro de Reservas
O usuário pode adicionar uma nova reserva informando os seguintes dados:
- Nome do cliente
- Data e hora da reserva
- Número de pessoas
- Número da mesa

### 2. Visualização de Reservas
O sistema exibe todas as reservas existentes, facilitando a visualização para o usuário.

### 3. Atualização de Reservas
O usuário pode selecionar uma reserva existente e atualizá-la, alterando os dados de nome, número de pessoas, mesa ou data.

### 4. Cancelamento de Reservas
A qualquer momento, o usuário pode cancelar uma reserva, liberando a mesa para outros clientes.

## Fluxo de Desenvolvimento

Este projeto foi organizado utilizando **Git** e **branches** para um desenvolvimento modular. As etapas seguidas no processo de desenvolvimento foram:

1. **Planejamento e Estruturação**: Definição do escopo do projeto e estrutura de arquivos.
2. **Desenvolvimento da Classe Reserva**: Implementação da classe `Reserva` para armazenar as informações de cada reserva.
3. **Implementação do Gerenciador de Reservas**: Desenvolvimento da classe `GerenciadorReservas` para controlar as operações de CRUD (adicionar, listar, atualizar e excluir).
4. **Interface do Usuário**: Criação de um menu interativo para o usuário gerenciar as reservas.
5. **Testes e Ajustes Finais**: Realização de testes e ajustes para garantir o bom funcionamento do sistema.

## Desafios Enfrentados

- **Gerenciamento de dados de reservas:** Garantir que as reservas fossem gerenciadas de forma eficiente, com facilidade para adicionar, listar, atualizar e excluir.

## Conclusão

Esse projeto oferece uma solução simples e eficiente para gerenciar reservas em restaurantes, utilizando as melhores práticas de **POO** e **Git**. Ele serve como uma excelente base para futuros aprimoramentos, como a adição de persistência de dados em banco de dados ou a criação de uma interface gráfica.