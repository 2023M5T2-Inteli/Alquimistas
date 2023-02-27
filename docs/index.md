<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Concepção de sistema de automação industrial
</center></font>

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
    - [Escopo Macro](#escopo-macro)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Análise da área de atuação](#análise-da-área-de-atuação)
  - [Análise do cenário: Matriz SWOT](#análise-do-cenário-matriz-swot)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
  - [Matriz Oceano Azul](#matriz-oceano-azul)
  - [Análise Financeira](#análise-financeira)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Jornada do Usuário](#jornada-do-usuário)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Arquitetura da Solução - Versão 1](#arquitetura-da-solução---versão-1)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard](#wireframe--storyboard)
  - [Design de Interface - Guia de Estilos](#design-de-interface---guia-de-estilos)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
  - [Testes Unitários](#testes-unitários)
  - [Teste de Usabilidade](#teste-de-usabilidade)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
- [Referências](#referências)


# Autores

* Bruno Leão
* Filipi Kikuchi
* Gabriela Rodrigues
* Henrique Santos
* Jackson Aguiar
* Luana Parra
* Vitor Zeferino


# Visão Geral do Projeto

## Empresa

<br>	O Instituto de Pesquisas Tecnológicas (IPT), vinculado à Secretaria de Desenvolvimento Econômico do Estado de São Paulo,  há 123 anos colabora para o processo de desenvolvimento do País, provê soluções tecnológicas para a indústria, governos e sociedade, habilitando-os a superar os desafios da nossa época. </br>
<br>	Desse modo, como um dos maiores institutos de pesquisas do Brasil, o IPT conta com laboratórios capacitados e equipe de pesquisadores e técnicos altamente qualificados, atuando basicamente em quatro grandes áreas - inovação, pesquisa e desenvolvimento; serviços tecnológicos; desenvolvimento & apoio metrológico, e informação & educação em tecnologia. </br>

## O Problema

<br>	Considerando que a separação magnética pode ser uma excelente técnica para avaliação da liberação de minerais/materiais com propriedades magnéticas e que, em uma etapa preliminar exploratória, não estão disponíveis grandes quantidades de amostras para serem submetidas a ensaios em equipamentos de separação magnética com operação contínua, a automação deste procedimento é benéfica do ponto de vista de agilidade e precisão. </br>
<br>	Posto isso, o processo atual é manual, ou seja, o operador aproxima um ímã de ferrite ou de terras raras, envolto em um saco plástico, do material submerso em água, espalhado em uma bandeja plástica, tentando manter uma distância constante e, consequentemente, o campo eletromagnético aplicado sobre as partículas. O material ferromagnético gruda no ímã e é posteriormente depositado em outro recipiente. </br>
<br>	Assim, por ser um processo manual, a constância da distância é imprecisa e, considerando que o campo eletromagnético é inversamente proporcional à distância, o campo aplicado sobre as partículas também é impreciso, dificultando a determinação do campo necessário para a separação dos minerais. Além disso, para testar diferentes campos é necessário a troca dos ímãs utilizados, resultando na necessidade de se ter diversos ímãs disponíveis. </br>

## Objetivos

### Objetivos gerais

<br>	Desenvolver um equipamento automatizado que tenha capacidade de aplicar um campo magnético constante, com intensidade e distância ajustáveis, ao longo de todo a amostra promovendo assim uma separação dos minerais magnéticos, que serão depositados em um recipiente diferente dos minerais não magnéticos que permanecerão depositados na bandeja original.</br>

### Objetivos específicos

<br> A seguir estão os objetivos/benefícios esperados com o desenvolvimento do projeto: </br>
* Manutenção de uma campo magnético constante sobre toda a amostra, reduzindo os erros de ensaio decorrentes da ação humana;
* Maior qualidade na execução do ensaio, principalmente no que tange a repetibilidade e reprodutibilidade;  
* Maior flexibilidade de ensaios, pois o uso de eletroímãs ajustáveis dispensa a necessidade de se ter ímãs com o campo desejado; 
* Determinação mais precisa do campo magnético adequado para diferentes ensaios. 

### Escopo Macro

* Um braço robótico capaz de posicionar um manipulador em posição e distância controladas sobre a bandeja de amostras;
* Eletroímã montado no manipulador do braço robótico com campo magnético ajustável na faixa de 800 a 12.000 Gauss; 
* Estrutura para calibração de posicionamento do braço; 
* Estrutura para calibração de eletroímã; 
* Automação da bandeja de amostra para promover a agitação das partículas; 
* Recipiente com automatização de pesagem para receber material coletado (opcional); 
* Relatório apresentando todos os dados pertinentes do ensaio (opcional). 

## Partes interessadas

* IPT - Instituto de Pesquisas Tecnológicas
* INTELI - Instituto de Tecnologia e Liderança

# Análise do Problema

*Descrição_da_análise_do_problema*

## Análise da área de atuação

*Descrição_da_análise_da_área_de_atuação*

## Análise do cenário: Matriz SWOT

*Matriz_SWOT*

## Proposta de Valor: Value Proposition Canvas

![Alt text](\img\sprint1\proposta-de-valor.png)

## Matriz de Risco

![Alt text](\img\sprint1\matriz-de-riscos.png)

## Matriz Oceano Azul

![Alt text](\img\sprint1\matriz-oceano-azul.png)

## Análise Financeira

![Alt text](\img\sprint1\roi.png)

# Requisitos do Sistema

*Descrição_dos_requisitos*

## Personas

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/persona.png)
João Silva, 35 anos
Formação: Engenheiro Químico
Empresa: Instituto de Pesquisa e Tecnologia (IPT) - Setor: Materiais Avançados - Salário: R$3000,00 por mês
Projeto de trabalho: Separação Magnética em Projetos de Mineração
Interesses/Hobbies: Tecnologia, robótica, automação industrial, jogar futebol, viajar e ler sobre novas descobertas científicas
Personalidade: Dinâmico, curioso e apaixonado por soluções tecnológicas inovadoras.

## Jornada do Usuário

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/jornada-do-usuario.png)

## Histórias dos usuários (user stories)

1. Como pesquisador, eu quero acionar o robô, para que ele inicie o processo de limpar a amostra.
2. Como supervisor, eu quero automatizar o processo, para melhorar a acurácia do relatório.
3. Como supervisor, eu quero automatizar o processo, para melhorar a gestão de tempo com a equipe.

# Arquitetura do Sistema

## Arquitetura da Solução - Versão 1

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/arquitetura-da-solucao-v1.png)

## Módulos do Sistema e Visão Geral (Big Picture)

## Descrição dos Subsistemas

### Requisitos de software


## Tecnologias Utilizadas


# UX e UI Design

## Wireframe + Storyboard

## Design de Interface - Guia de Estilos


# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico


# Teste de Software

## Testes Unitários

## Teste de Usabilidade


# Análise de Dados


# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências
