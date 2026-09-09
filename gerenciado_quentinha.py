# Python, quero utilizar uma ferramenta da biblioteca openpyxl chamada Workbook
# Workbook é uma classe da biblioteca openpyxl usada para criar ou trabalhar com um arquivo Excel (.xlsx) em Python.
# load_workbook() significa: abrir uma planilha que já existe.
from openpyxl import Workbook, load_workbook
# Python, eu quero usar as ferramentas do sistema operacional.
# por exemplo, ver os arquivos de uma pasta
import os

# lista que vai armazena todos os dados clientes
dados_clientes = []
# valor da quentinha
valor_quentinha = 16
total = 0
valor = True
continuar = True

# saudação
print("------------------------------------------------------------------")
print("Seja Bem-vindo ao gerenciado de quentinhas!")
print("------------------------------------------------------------------")

# while continuar == True
while continuar:    

  nome = input("Seu nome: ")
  # enquanto nome for string vazia ou nome for numero, faça:
  while nome == "" or nome.isdigit():
      print("Digite um nome válido!")
      nome = input("Seu nome: ")
          
  # enquanto valor for verdadeiro, faça:
  while valor:
   # quantidade de quentinha comprada
   quantidade_quentinha = input("Quantidade de quentinha compradas: ")
   # se quantidade_quentinha for um número inteiro, então converta para inteiro
   if quantidade_quentinha.isdigit():
      quantidade_quentinha = int(quantidade_quentinha)
      
      # se quantidade_quentinha for maior que 0 entao
      if (quantidade_quentinha > 0):
        # calcula o valor que cada cliente deve
        valor_devido = valor_quentinha * quantidade_quentinha
        print("------------------------------------------------------------------")
        print("valor: ", valor_devido)
        print("------------------------------------------------------------------")
        # realizar a soma total do valor de cada cliente
        total = total + valor_devido
          # # Armazena os dados do cliente
        dados_clientes.append([nome, quantidade_quentinha, valor_devido])
        valor = False

      else:
          print("Quantidade de quentinhas inválida! Digite um número maior que 0.")
          valor = True
            
   else:
      print("Quantidade de quentinhas inválida! Digite um número inteiro.")
      valor = True

  resposta = input("Digite [s] para continuar cadastrando e [n] para encerrar: ").lower() 
  
  # enquanto resposta for diferente de "s" e diferente de "n", faça:
  while resposta != "s" and resposta != "n":    
         print("Digite uma opção válida!")
         resposta = input("Digite [s] para continuar cadastrando e [n] para encerrar: ").lower()

  if resposta == "n":
        continuar = False

  elif resposta == "s":
      continuar = True
      
# exibe a soma total de todos os clientes
  print("------------------------------------------------------------------")
  print("Total de Lucro: ", total)
  print("------------------------------------------------------------------")
  
# Esse arquivo existe nesse caminho?
# O arquivo quentinha.xlsx existe?
if os.path.exists("quentinha.xlsx"):
    # Abra o arquivo que já existe.
    planilha = load_workbook("quentinha.xlsx")
else:
    # Como não existe, crie uma planilha nova
    planilha = Workbook()

# planilha.active pega a aba ativa.
# "Vou trabalhar nessa aba.
pagina = planilha.active
# nome para a aba
pagina.title = "Quentinhas"
# adicionando uma linha na planilha | Nome | Quantidade | Valor Unitário | 
pagina.append(["Nome", "Quantidade", "Valor Devedor"])
# pessoa recebe a lista inteira de dados clientes a cada repetição
# Para cada pessoa que está dentro de dados, coloque uma linha na planilha.
for pessoa in dados_clientes:
  pagina.append(pessoa)
# adiciona uma linha vazia
pagina.append([])
# # Adiciona o total geral UMA ÚNICA VEZ
pagina.append([
  "TOTAL GERAL","", total
])
# Pegue essa planilha que eu montei e salve no computador com o nome quentinhas.xlsx.
planilha.save("quentinha.xlsx")








