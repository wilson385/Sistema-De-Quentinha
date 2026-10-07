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
continuar = True

# saudação
print("------------------------------------------------------------------")
print("Seja Bem-vindo ao gerenciado de quentinhas!")
print("------------------------------------------------------------------")

# while continuar == True
while continuar:

  valor = True

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

# se a célula A1 estiver vazia, então adicione uma linha com os títulos das colunas
if  pagina["A1"].value is None:  
  # adicionando uma linha na planilha | Nome | Quantidade | Valor Unitário | 
  pagina.append(["Nome", "Quantidade", "Valor Devedor"])

# "Por enquanto, não encontrei nenhuma linha de total."
linha_total = None

# pagina.max_row  quantidade/posição da última linha utilizada da planilha.
# max_row faz isso: Qual é o número da última linha utilizada?
# O + 1 existe porque o range() não inclui o número final.
# "Para cada número de linha existente na planilha, faça alguma coisa."
for linha in range(1, pagina.max_row + 1):
  #  "Pegue a célula localizada na linha X e coluna 1 (A).
  # "Se o valor da célula da coluna A dessa linha for igual a TOTAL GERAL..."
  if pagina.cell(linha, 1).value == "TOTAL GERAL":
    #  "Então, eu encontrei a linha de total."
     linha_total = linha
    #  pare o for imediatamente.
     break

# Números diferentes de zero são considerados verdadeiros em uma condição.
if linha_total:
  # pegue o valor da célula da coluna 3 (C) dessa linha."
   total_antigo = pagina.cell(linha_total, 3).value

  #  se total_antigo estiver vazio, considere 0
   if total_antigo is None:
      total_antigo = 0

else:
   total_antigo = 0      

# pessoa recebe a lista inteira de dados clientes a cada repetição
# Para cada pessoa que está dentro de dados, coloque uma linha na planilha.
for pessoa in dados_clientes:
  pagina.append(pessoa)

total = total_antigo

for pessoa in dados_clientes:
    # pessoa[2] representa o valor devido pelo cliente.
   total += pessoa[2]

if linha_total:
  #  Exclua a linha 5 inteira.
   pagina.delete_rows(linha_total)

# adiciona uma linha vazia
pagina.append([])
# # Adiciona o total geral UMA ÚNICA VEZ
pagina.append([
  "TOTAL GERAL","", total
])
# Pegue essa planilha que eu montei e salve no computador com o nome quentinhas.xlsx.
planilha.save("quentinha.xlsx")








