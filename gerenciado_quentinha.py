# Python, quero utilizar uma ferramenta da biblioteca openpyxl chamada Workbook
# Workbook é uma classe da biblioteca openpyxl usada para criar ou trabalhar com um arquivo Excel (.xlsx) em Python.
from openpyxl import Workbook

# lista que vai armazena todos os dados clientes
dados_clientes = []
# valor da quentinha
valor_quentinha = 16
total = 0
continuar = True

# saudação
print("------------------------------------------------------------------")
print("Seja Bem-vindo ao gerenciado de quentinhas!")
print("------------------------------------------------------------------")

# while continuar == True
while continuar:    

  nome = input("Seu nome: ")
      # quantidade de quentinha comprada
  quantidade_quentinha = int(input("Quantidade de quentinha compradas: "))
      # se quantidade_quentinha for maior que 0 entao
  if (quantidade_quentinha > 0):
      # calcula o valor que cada cliente deve
      valor_devido = valor_quentinha * quantidade_quentinha
      print("valor: ", valor_devido)
      # realizar a soma total do valor de cada cliente
      total = total + valor_devido
        # # Armazena os dados do cliente
      dados_clientes.append([nome, quantidade_quentinha, valor_devido])
      #  senao
  else:
        print("Digite um valor válido!") 
         
  resposta = input("Digite [s] para continuar e [n] para encerrar: ").lower() 

  while resposta != "s" and resposta != "n":    
         print("Digite uma opção válida!")
         resposta = input("Digite [s] para continuar e [n] para encerrar: ").lower()

  if resposta == "n":
        continuar = False

  elif resposta == "s":
      continuar = True
      

# exibe a soma total de todos os clientes
  print("Total de Lucro: ", total)

# ==================================================
# CRIANDO O ARQUIVO EXCEL
# ==================================================
# Crie uma nova pasta de trabalho do Excel
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








