# Sistema de Gerenciamento de Quentinhas

-----------------------------------------

# Objetivos

Automatizar e agilizar o registro das vendas de quentinhas, o cálculo do valor devido por cada cliente e o cálculo do valor total das vendas.

# Usuário do Sistema

- Administrador (a)

# Problemas Identificados

- Processo manual demorado.
- Possibilidade de erros nos cálculos.
- Risco de perda de informações.
- Informações espalhadas em registros de papel.


# levantamentos de requisitos

-------------------------------
 
 # requisitos funcionais
 <!-- Tudo que o sistem faz -->

- RF01 Exibi uma mensagem de saudação na tela.
- Rf02 Pergunte o nome, quantidade de quentinha compradas.
- RF03 Validar informações.
- RF04 calcule o valor que cada cliente deve, e exibe na tela.
- RF05 soma o valor de todos os clientes, gerando o valor total de lucros na tela.
- RF06 Pergunte se o usuário deseja continuar cadastrando ou não. 
- RF07 armazenar os dados das vendas em um arquivo Excel.

# requitos não funcionais
<!-- Como o sistema deve funcionar -->

- RNF01  O sistema deve possuir uma interface simples e fácil de utilizar.
- RNF02  O sistema deve realizar os cálculos rapidamente.
- RNF03  O sistema deve armazenar os dados de forma segura.

# Regras de Negócio
<!-- regras que determinam como o sistema deve funcionar de acordo com as necessidades do negócio. -->
<!-- regra que determina como aquilo deve funcionar -->

- RN01 Cada quentinha custa R$16
- RN02 Nome do usuário e quantidade de quentinha deve ser validado
- RN03 Quantidade de quentinha dever ser maior que 0
- RN04 Calculo do valor de cada cliente deve ser a Quantidade de quentinha deve ser x 16
- RN05 Cliente pode comprar várias Quentinhas
- RN06 Digite s para continuar cadastrando e n para encerrar
- RN07 Se o usuário não digitar s ou n, peça a ele para digitar uma informação válida

# Dúvidas para o cliente







 