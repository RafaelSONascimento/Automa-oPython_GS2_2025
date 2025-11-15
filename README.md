# Global Solution 2025.2 - Future Skills Lab

**Curso:** Ciência da Computação (1º Ano)
**Disciplina:** Pensamento Computacional e Automação com Python
**Professor:** Alexandre Russi Jr.

**Integrantes:** 

565415 - Rafael Silva Oliveira 

563651 - Henrique Boscoli

563578 - Joao Henrique Queiroz Gil

---

## Future Skills Lab: Orientador de Carreiras

Este projeto é um sistema inteligente de orientação de carreiras desenvolvido em Python. Ele simula uma ferramenta que analisa o perfil de competências de um profissional e recomenda carreiras do futuro, alinhando-se ao tema "Future at Work" da Global Solution.

O sistema coleta competências técnicas (como `python`, `logica`) e comportamentais (como `colaboracao`, `criatividade`) do usuário e as compara com um banco de dados de carreiras emergentes, sugerindo as mais adequadas e indicando quais habilidades ainda precisam ser desenvolvidas.

---

##  Estrutura do Projeto e Conceitos Aplicados

O código foi desenvolvido aplicando os conceitos fundamentais de **Programação Orientada a Objetos (OOP)** e estruturas de dados essenciais do Python.

### 1. Classes (Orientação a Objetos)

O sistema é modelado usando três classes principais, localizadas no arquivo `modelos.py`:

* `class Perfil:`
    * **Propósito:** Representa o usuário.
    * **Atributos:** `nome` (str) e `competencias_usuario` (list).
    * **Metodos:** `adicionar_competencia()` para construir o perfil do usuário.

* `class Carreira:`
    * **Propósito:** Representa uma carreira futura.
    * **Atributos:** `nome` (str), `descricao` (str) e `competencias_necessarias` (tuple).

* `class OrientadorCarreira:`
    * **Propósito:** É o "cérebro" do sistema. Orquestra a análise.
    * **Atributos:** `banco_carreiras` (dict).
    * **Metodos:** `_inicializar_banco_carreiras()` (para criar o "banco de dados"), `analisar_perfil()` (para fazer a lógica de match) e `exibir_recomendacoes()` (para formatar a saída).

### 2. Estrutura de Dados (Requisito 1)

* **Listas (`list`):** Usada na classe `Perfil` (em `competencias_usuario`). Escolhemos listas por serem **mutáveis**, permitindo que o usuário adicione dinamicamente várias competências ao seu perfil.
* **Tuplas (`tuple`):** Usada na classe `Carreira` (em `competencias_necessarias`). Escolhemos tuplas por serem **imutáveis**, garantindo que as competências necessárias para uma carreira não sejam alteradas acidentalmente durante a execução do programa.
* **Dicionários (`dict`):** Usado na classe `OrientadorCarreira` (em `banco_carreiras`). Um dicionário foi a escolha ideal para criar um "banco de dados" de carreiras, pois permite acesso rápido e organizado a cada objeto `Carreira` através de uma chave (ex: `"cientista_dados"`).
* **Conjuntos (`set`):** Dentro do método `analisar_perfil()`, as listas e tuplas são convertidas para `sets` (conjuntos). Esta é uma boa prática de lógica de programação, pois permite usar operações de conjunto (como `intersection` e `difference`) para encontrar competências em comum e faltantes de forma extremamente eficiente.

### 3. Estrutura de Arquivos

O projeto está dividido em dois módulos para melhor organização (Boas Práticas):

* `modelos.py`: Contém as classes (a lógica de negócios e o modelo de dados).
* `main.py`: Contém a interface com o usuário (CLI) e o ponto de entrada da aplicação (a função `main()`).

---

## 📸 Demonstração de Uso

O programa primeiro pergunta seu nome e, em seguida, lista as competências:



```
========================================
   Bem-vindo ao Future Skills Lab!
  Seu orientador de carreiras do futuro
========================================
Digite seu nome: Alexandre
--- Selecione suas Competências Atuais ---
Digite o número de uma competência e pressione Enter.
Você pode adicionar várias. Digite '0' para finalizar.
1. adaptabilidade
2. analise_dados
3. colaboracao
4. comunicacao
5. criatividade
6. design
7. empatia
8. etica
9. lideranca
10. logica
11. pensamento_critico
12. python

0. Concluir e Gerar Recomendações

Alexandre, escolha uma opção (ou '0' para sair): 10
  [+] Competência 'logica' adicionada ao seu perfil.

Alexandre, escolha uma opção (ou '0' para sair): 12
  [+] Competência 'python' adicionada ao seu perfil.

Alexandre, escolha uma opção (ou '0' para sair): 0
```

Após a seleção, o sistema processa e exibe as recomendações:



```
--- Analisando seu perfil... ---

=== Suas Recomendações de Carreira ===

**Especialista em IA e Ética**
  Descrição: Desenvolve modelos de IA, garantindo que sejam justos, transparentes e éticos.
  Match: 2 de 4 competências.
  Competências que você possui: logica, python
  Trilha de Aprendizado (o que falta): etica, pensamento_critico
------------------------------

**Cientista de Dados**
  Descrição: Analisa grandes volumes de dados para extrair insights e tomar decisões.
  Match: 2 de 4 competências.
  Competências que você possui: logica, python
  Trilha de Aprendizado (o que falta): analise_dados, comunicacao
------------------------------

Obrigado por usar o Future Skills Lab!
```