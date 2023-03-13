<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://camo.githubusercontent.com/2dec1e5c541f0802d0d2e49a39062ea6d9a375d8a8086ffed7e69e686b2f227e/68747470733a2f2f7777772e696e74656c692e6564752e62722f77702d636f6e74656e742f75706c6f6164732f323032312f30382f32303137323032382f6d617263615f312d322e706e67" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
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
    - [Análise de custo do processo atual](#análise-de-custo-do-processo-atual)
    - [Análise de custo da solução](#análise-de-custo-da-solução)
    - [ROI - Return Over Investment](#roi---return-over-investment)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Jornada do Usuário](#jornada-do-usuário)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Arquitetura da Solução - Versão 1](#arquitetura-da-solução---versão-1)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Bloco de Interface](#bloco-de-interface)
    - [Braço Robótico](#braço-robótico)
    - [Backend - Computador](#backend---computador)
    - [Embarcados](#embarcados)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
    - [Bloco de Interface](#bloco-de-interface-1)
    - [Braço Robótico](#braço-robótico-1)
    - [Backend - Computador](#backend---computador-1)
    - [Embarcados](#embarcados-1)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard - Versão 1](#wireframe--storyboard---versão-1)
  - [Design de Interface - Guia de Estilos](#design-de-interface---guia-de-estilos)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Hardware - Versão 1](#teste-de-hardware---versão-1)
  - [Braço robótico (Dobot Magician)](#braço-robótico-dobot-magician)
  - [Eletroimã](#eletroimã)
  - [Shaker](#shaker)
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

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/proposta-de-valor.png)

## Matriz de Risco

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/matriz-de-risco.png)

## Matriz Oceano Azul

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/matriz-oceano-azul.png)

## Análise Financeira

### Análise de custo do processo atual

Inicialmente, os custos relacionados ao processo atual provém da compra dos
equipamentos (ímãs de neodímio) e remuneração de mão de obra. Em um primeiro
momento, projetamos que o salário médio de um Técnico é de R$ 2.833/mês.
Considerando uma carga horária de 8 horas por dia, podemos chegar na estimativa de
R11,80/hora. Através de entrevistas com o parceiro, cada sessão de separação
magnética dura cerca de 30 minutos. Consequentemente, o custo do processo é de
R$5,90. Somado à isso o custo médio dos ímãs projetados em R$663,00 cada, que
devido à sua natureza, não precisam ser substituídos a curto prazo.

### Análise de custo da solução
A solução contempla a utilização de um braço robótico (Dobot Magician Lite),
microcontroladores Raspberry Pi Pico W, sensores e atuadores como componentes
físicos.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/analise_financeira.png)

### ROI - Return Over Investment
Analisando os gastos atuais e os custos com equipamento, pode-se estimar o tempo
necessário para recuperar o valor do investimento. Segue a análise:

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/roi.png)

# Requisitos do Sistema

*Descrição_dos_requisitos*

## Personas

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint1/persona.png)
João Silva, 35 anos

Formação: Engenheiro Químico

Empresa: Instituto de Pesquisa e Tecnologia (IPT) - Setor: 

Materiais Avançados - Salário: R$3000,00 por mês

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

### Bloco de Interface 
O Bloco de Interface consiste em um sistema visual para o usuário poder realizar o controle dos componentes do projeto. Sendo o principal processo o ciclo de coleta de materiais por meio de campos magnéticos. Mas podendo também interagir de forma individual com os demais componentes do sistema. 

### Braço Robótico
O componente do braço robótico é o Dobot Magician Lite, desse modo, esse é o principal responsável por executar a trajetória do processo descrito no item "Bloco de Interface". 

O Magician Lite é um braço robótico inteligente leve e multifuncional, tornou-se um excelente produto para educação e aprendizado em inteligência artificial.

### Backend - Computador
Sistema integrado que abarca o código do servidor de interface, assim como os controles do Microcontrolador Raspberry Pi Pico. 

### Embarcados 
1. Raspberry Pi Pico: A Raspberry Pi Pico é uma placa microcontrolada de baixo custo e alta performance, com interfaces digitais flexíveis. 
2. Ponte H: A ponte H é um circuito que serve para variar o sentido da corrente em uma determinada carga, bem como controlar sua potência.
  <br>2.1. Elétroimã: O eletroímã é um dispositivo formado por um núcleo de ferro envolto por um solenoide (bobina) que, mediante uma indução de corrente, gera campo magnético.
  <br>2.2. Shaker: O Micro Motor Vibracall é um tipo de motor de tamanho bem reduzido, responsável por produzir vibrações.

## Relatório de entrada e saídas
Com base na estrutura de Arquitetura desenvolvida para a solução proposta, avaliamos os inputs e outputs esperados para cada sistema de blocos e cada componente do sistema. 
|Indice|Bloco              |Componente de Entrada|Leitura da Entrada              |Componente de Saída |Leitura da Saída                    |Descrição                                                                                                                       |
|------|-------------------|---------------------|--------------------------------|--------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|1	   |Robô               |Computador 	         |Sinal de Inicio                 |Dobot Magician Lite |Movimentação                        |Ao acionarmos via computador, o robô irá se movimentar de acordo com as coordenadas corretas.                                   |
|2	   |Robô               |Computador 	         |Sinal de Encerramento	          |Dobot Magician Lite |Pausa no Movimento	                |Ao encerrarmos o movimento via computador, o robô irá parar de se movimentar.                                                   |
|3	   |Backend 	       |Computador 	         |Acionamento da Raspberry Pi Pico|Raspberry Pi Pico   |Inicia o Código no Microcontrolador	|Ao iniciar o código o raspberry pi pico se torna responsável pela atuação de alguns componentes no sistema.                     |
|4	   |Sistemas Embarcados|Raspberry Pi Pico	 |Sinal de Inicio - Acionamento   |Ponte H	           |Alimentação do Shaker e do Eletroimã|Ao iniciar o código o raspberry pi pico ele alimenta a ponte H e essa por sua vez alimenta os componentes do Shaker e Eletroimã |
|5	   |Sistemas Embarcados|Ponte H	             |Sinal de Inicio - Acionamento   |Shaker 	           |Vibração do Shaker 	                |Ao iniciar a alimentação do shaker haverá um botão de acionamento na interface que irá permitir o acionamento do Shaker.        |
|6	   |Sistemas Embarcados|Ponte H	             |Sinal de Inicio - Acionamento   |Eletroimã	       |Criação de Campo Magnético	        |Ao iniciar a alimentação do eletroimã haverá um botão de acionamento na interface que irá permitir o acionamento do mesmo.      |
|7	   |Interface	       |Computador 	         |Acionamento do Shaker           |Shaker 	           |Vibração do Shaker 	                |Ao acionar o shaker via interface, ele inicia sua atuação.                                                                      |
|8	   |Interface	       |Computador 	         |Acionamento do Eletroimã	      |Eletroimã	       |Criação de Campo Magnético	        |Ao acionar o eletroimã via interface, ele inicia sua atuação.                                                                   |
## Testes de Componentes - Versão 1 

### Braço robótico (Dobot Magician)
O braço mecânico foi testado nas seguintes etapas.

1. Inicialmente, foi realizada a conexão do braço via USB. Posto isso, foi possível explorar as movimentações e funcionalidades do robô (além dos 'acessórios' do robô, como a garra, caneta, sucção) a partir do software Dobot Studio.
2. Com o conhecimento dos limites da movimentação do braço e seu alcance em relação as três bandejasjá posicionadas para a realização da separação magnética, foi instalada a biblioteca pronta, PyDobot, que realiza a comunicação com o robô e códigos em Python, onde testamos os movimentos do Dobot. Posteriormente, criamos uma classe para o desenvolvimento do script da movimentação do robô.
3. Após um feedback do cliente, criamos um movimento da garra em uma das bandejas, que poderá funcionar como um "shaker".

[Vídeo do Braço Robótico](https://www.youtube.com/embed/9Ak5891op9U)

[Vídeo do Braço Robótico funcionando com o Eletroimã](https://youtube.com/shorts/RmgzJqTKww4)


### Eletroimã (na Ponte H)

A partir da arquitetura da solução, estudamos o método de PWM para o funcionamento do eletroimã. Contudo, após discussões no grupo foi utilizada a ponte H que aciona o imã com um botão liga e desliga básico. Posteriormente, será possível conectar esse script ao servidor, e consequentemente ao frontend. 

Assim, abaixo é possível observar o teste do eletroimã sendo acionado: 

[Vídeo do Eletroimã](https://youtube.com/shorts/ryoXvXvyKvg?feature=share)

### Shaker (na Ponte H)

Assim como o eletroimã, e a partir da arquitetura da solução, para o funcionamento do shaker (atuador) foi testado na ponte H, por ser um método mais simples. 

Posto isso, é possível observar o teste do shaker sendo acionado: 

[Vídeo do Shaker](https://youtube.com/shorts/p4DXiTl25Kk?feature=share)

### Requisitos de software

## Tecnologias Utilizadas

### Bloco de Interface 
- HTML 
- CSS 
- JavaScript 
- Bootstrap
- Python

### Braço Robótico
- Dobot Magician Lite 
- Software - Dobot 
- Python 

### Backend - Computador
- IDE: Thonny 
- Python 
- MicroPython 

### Embarcados 
- IDE: Thonny 
- Python 
- MicroPython 

# UX e UI Design

## Wireframe + Storyboard - Versão 1

Para o desenvolvimento da interface do usuário optamos por uma aplicação web, com uma estrutura desenvolvida com base nas necessidades de entradas e saídas vinculadas ao bloco de Interface na Arquitetura da Solução.

Dessa maneira, a primeira versão consiste em uma página com um modal para realizar o acionamento dos componentes do sistema: Wifi, Shaker e Eletroimã.

![img](https://github.com/2023M5T2-Inteli/alquimistas/blob/main/docs/img/sprint2/interface.png)

[Wireframe no Figma](https://www.figma.com/file/SURaYJTPLilelYLFrS4gdi/Front-IPT?node-id=0%3A1&t=6frlueaWTHFUkmnN-0)


## Design de Interface - Guia de Estilos

Desse modo, foi desenvolvida uma interface gráfica no Figma que tem como objetivo o acionamento de componentes do sistema: 

# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico

# Teste de Software
### Implementação de Servidor 
Para podermos estruturar a renderização das páginas construídas para o software, foi necessário realizar o desenvolvimento de um servidor utilizando a biblioteca Flask para Python. O Flask é um framework web leve e flexível que permite a construção de aplicativos web de forma fácil e eficiente. Com o Flask, é possível criar rotas de acesso às páginas do aplicativo, além de realizar o gerenciamento das solicitações e respostas HTTP.

Desse modo, as páginas do software são acionadas por meio das rotas desenvolvidas no servidor. Inicialmente, o servidor foi composto pelas páginas de acionamento, parada e envio de relatório. Cada uma dessas páginas é responsável por uma funcionalidade específica do software, como a ativação dos dispositivos eletrônicos, a parada do sistema e o envio de relatórios de funcionamento.

O funcionamento do servidor está ocorrendo de forma local, de modo que é necessário realizar o seguinte processo para acessar a interface do software:

1) Acessar a pasta src/backend: A pasta onde está localizado o código do servidor Flask.
2) Rodar o seguinte comando: `python app.py` 
Este comando irá iniciar o servidor Flask e disponibilizar as rotas de acesso às páginas do software.
3) Assim, irá iniciar o servidor e você precisará acessar o IP fornecido pelo servidor para acessar localmente

### Servidor com Acionamento de Hardware 
Para que se estabeleça a conexão entre as APIs que acionam o servidor em Flask e o Raspberry Pi Pico W, o microcontrolador responsável por controlar a Ponte H e, consequentemente, acionar o Eletroímã, é necessário um processo de transmissão de um código específico que conecte o Raspberry a um provedor de rede. Isso é fundamental para garantir que tanto o servidor quanto o microcontrolador estejam vinculados à mesma rede, viabilizando assim a comunicação entre eles.

O Módulo Sensor de Campo Magnético - Efeito Hall também desempenha um papel importante nesse processo, já que ele é responsável por captar as informações de campo magnético geradas pelo Eletroímã e enviá-las para o Raspberry, que as utiliza para controlar a Ponte H.

Dessa forma, com a conexão estabelecida e o Módulo Sensor devidamente configurado, o servidor pode iniciar o funcionamento do Eletroímã por meio de um endpoint específico, que aponta diretamente para o endpoint do microcontrolador responsável pela Ponte H. Ao ser acionado, o microcontrolador ativa o funcionamento da Ponte H, permitindo que o Eletroímã seja controlado e operado de acordo com as instruções recebidas do servidor.

# Prototipação de Hardware
## Projeto dos dispositivos mecânicos
Inicialmente o projeto consiste na utilização dos dispositivos disponibilizados pelo laboratório de eletrônica. E os sistêmas mecânicos se baseiam em uma integração entre componentes eletrônicos e as estruturas disponíveis do Dobot Magician Lite. 

## Projeto dos dispositivos eletrônicos
### Listagem de Placa: 
1) Placa Central: Foi desenvolvida a proposta de uma placa central única para o acionamento dos dispositivos eletrônicos do sistema em questão. A placa em questão engloba os sistemas principais que serão acionados, como a Ponte H, o Elétroimã, o Módulo de Transistor de Efeito Hall e o Raspberry Pi Pico.

A escolha por uma única placa de acionamento se justifica pela necessidade de uma integração eficiente dos sistemas, visando maximizar a eficiência e a segurança do sistema como um todo. A placa central permite que os diversos sistemas sejam conectados e acionados de maneira mais organizada e simplificada, minimizando a ocorrência de erros e falhas de comunicação.

Dentre os sistemas presentes na placa central, destaca-se a presença do Raspberry Pi Pico, responsável pela conexão com o servidor em Flask descrito no item "Teste de Software". Este dispositivo é capaz de realizar diversas funções, como o processamento de dados, a execução de códigos e a comunicação com outros dispositivos, tornando-se peça fundamental do sistema como um todo.

Em resumo, a placa central desenvolvida para o acionamento dos dispositivos eletrônicos do sistema foi projetada de forma cuidadosa e criteriosa, visando a integração eficiente dos diversos sistemas e a maximização da eficiência e segurança do sistema. A presença do Raspberry Pi Pico, por sua vez, permite uma conexão eficiente com o servidor em Flask e a execução de diversas funções essenciais para o funcionamento do sistema.

### Esquemático da Placa:
A seguir, apresentamos o diagrama esquemático da estrutura eletrônica da placa em questão. Este diagrama foi elaborado com base nas informações e descrições previamente mencionadas referentes à placa principal.

O processo de desenvolvimento do esquemático envolveu uma análise minuciosa das especificações técnicas da placa e das funcionalidades desejadas. Foram considerados aspectos como a configuração dos componentes eletrônicos, a disposição física dos mesmos na placa, bem como as conexões elétricas necessárias entre eles.

O resultado desse processo foi o esquemático completo da estrutura eletrônica da placa, que serve como guia para o desenvolvimento do layout da placa propriamente dita. A partir desse esquemático, é possível obter informações precisas sobre os componentes eletrônicos e suas respectivas conexões, permitindo uma construção precisa e eficiente da placa.

Em resumo, o esquemático da estrutura eletrônica da placa foi desenvolvido de forma cuidadosa e detalhada, levando em consideração todas as informações e especificações técnicas pertinentes. Este documento é essencial para o sucesso do projeto e garantirá a qualidade e eficiência da placa final.

<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/Esquemático_v1.png" width="30%">

### Layout da Placa:
Com base no diagrama desenvolvido por meio do software EasyEDA, tornou-se possível estruturar o layout fundamental da placa, assim como obter uma visualização do modelo tridimensional correspondente.

- Imagem do Layout
- Imagem Base 3D 

### Lista de Materiais:
1) Placa de Trilhas com Fenolite 
2) Raspberry Pi Pico W 
3) Soquete para Raspberry Pi Pico W 
4) Conjunto de Jumpers 
5) Ponte H - L298N
6) Amplificador 
7) Módulo de Transistor de Efeito Hall 
8) 2 Eletroimãs 
9) Fonte de 5V - Alimentação 

### Método de fabricação:
1) Inicialmente foi desenvolvido o esquemático de base para o circuito por meio do software EasyEDA: O processo de desenvolvimento do esquemático envolve a elaboração de um diagrama que representa as conexões elétricas entre os componentes eletrônicos que compõem o circuito. Nesta etapa, é considerado aspectos como a disposição dos componentes e as conexões elétricas necessárias. O software EasyEDA é uma ferramenta de design eletrônico que permite a criação de esquemas e layouts de placas de circuito impresso.

2) Em seguida foi realizado o posicionamento de componentes: Com base no esquemático desenvolvido na etapa anterior, os componentes eletrônicos são posicionados fisicamente na placa de circuito impresso. Nesta etapa, é importante considerar aspectos como a disposição física dos componentes, o espaço disponível na placa e as conexões elétricas necessárias.

3) A próxima etapa foi a soldagem de componentes: Após o posicionamento dos componentes na placa, é necessário realizar a soldagem dos mesmos. Este processo consiste na aplicação de calor em pontos específicos da placa, de modo a fixar os componentes eletrônicos na placa. A soldagem deve ser realizada com cuidado e precisão, visando garantir a qualidade e a segurança do circuito.

4) Por fim, foram realizados os testes de funcionamento do circuito: Após a conclusão da soldagem dos componentes, é necessário realizar testes para verificar o funcionamento do circuito. Os testes podem envolver o uso de instrumentos como multímetros e osciloscópios, que permitem medir e analisar os sinais elétricos presentes no circuito. Os resultados dos testes são utilizados para verificar se o circuito está operando de acordo com as especificações previamente definidas e, caso necessário, realizar ajustes ou correções.

## Fabricação dos Dispositivos Eletrônicos
1) Inicialmente foi realizado o teste com o circuito em protoboard para garantir o funcionamento do circuito. 
2) Posicionamento dos componentes na placa 
3) Soldagem do Soquete - Principal 
4) Soldagem de Jumpers 
5) Posicionamento do Amplificador e Soldagem 
6) Posicionamento do Módulo do Transistor de Efeito Hall e Soldagem 
7) Conexão de Jumpers 

Estruturadas todas as etapas, foi desenvolvido o circuito demonstrado nas imagens abaixo:
<br>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito1.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito2.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito3.jpeg" style="width: 20%"/>
<img src="https://github.com/2023M5T2-Inteli/alquimistas/blob/dev/docs/img/sprint3/circuito4.jpeg" style="width: 20%"/>

## Validação dos Dipositivos Eletrônicos
### Métodos de Validação e Testes 


# Análise de Dados

# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências


