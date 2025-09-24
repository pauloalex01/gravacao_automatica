import pdfplumber
import os

"""
Esse script gera a marcação no modelo selecionado, altere aqui o nome do pdf e escolha o tipo de gravação.
"""
# Encontrando o arquivo, o arquivo .pdf tem que estra no mesmo local que  o main.py
base_dir = os.path.dirname(os.path.abspath(__file__))  # pasta do script
arquivo = os.path.join(base_dir, "osMPI.pdf") # insira o nome do arquivo

def checar_item():
    """Checa os itens dos pedidos de compra e corrige para a forma correta"""

def gravacao_simples():
    """A gravação padrão mais utilizada: """
    pn = dicionario['DESENHO']
    rev = dicionario['REVIS.']
    serial = dicionario['QUANT.']

    if serial == 1:
        return pn + " " + rev + " " + f"001"
    elif serial < 10:
        return pn + " " + rev + " " + f"001 a 00{serial}"
    elif serial >= 10 and serial < 100:
        return pn + " " + rev + " " + f"001 a 0{serial}"
    elif serial >= 100:
        return pn + " " + rev + " " + f"001 a {serial}"



def gravacao_comum():
    """Gravação comum com pedido de compra: """
    
    pn = dicionario['DESENHO']
    rev = dicionario["REVIS."]
    item = list(dicionario2.values())
    serial = dicionario['QUANT.']

    if serial == 1:
        return pn + " - " + rev + " - " + item[0] + " - " + f"001"
    elif serial < 10:
        return pn + " - " + rev + " - " + item + " - " + f"001 a 00{serial}"
    elif serial >= 10 and serial < 100:
        return pn + " - " + rev + " - " + item + " - " + f"001 a 0{serial}"
    elif serial >= 100:
        return pn + " - " + rev + " - " + item + " - " + f"001 a {serial}"



with pdfplumber.open(arquivo) as pdf:
    pagina = pdf.pages[0]
    texto = pagina.extract_text()
    #print(texto)


# separar por linhas
linhas = texto.splitlines()

# procurar cabeçalho
for i, linha in enumerate(linhas):
    if linha.startswith("CLIENTE"):
        cabecalho = linha.split()
        
        # Correção do cabeçalho, para armazenamento correto dos dados:
        
        cabecalho_corrigido = cabecalho[:2] + ["DESCRICAO_PRODUTO_SERVICO"] + cabecalho[-2:]
        valores = linhas[i+1].split()
        
        # juntar descrição (caso tenha espaços)
        
        valores = valores[:len(cabecalho)-2] + [" ".join(valores[len(cabecalho)-2:-2])] + valores[-2:]
        
        # Correção dos valores:
        
        valores_corrigidos = valores[:2] + [" ".join(valores[2:-2])] + valores[-2:]
        
        # Criação de dicionário
        
        dicionario = dict(zip(cabecalho_corrigido, valores_corrigidos))
        dicionario["QUANT."] = int(dicionario["QUANT."])
        pass
    
    if linha.startswith("PEDIDO DE COMPRA"):
        
        lista = []
        
        cabecalho2 = linha.split()

        valores2 = linhas[i+2].split()
        
        pedido_de_compra = " ".join(cabecalho2[:3])
        item = " ".join(valores2[:2])

        dicionario2 = {pedido_de_compra: item}
        
        break
    

print("""
1 - Gravação Simples: PN + REV + SERIAL
2 - Gravação Comum: PN + PEDIDO DE COMPRA + SERIAL
\n""")

opcao = int(input('Escolha a opção de gravação: '))

if opcao == 1:
    
    resultado = f"\nA gravação é: {gravacao_simples()}\n"
    print(resultado)
elif opcao == 2:
    resultado = f"\nA gravação é: {gravacao_comum()}\n"
    print(resultado)
else:
    resultado = "\nOpção Inválida\n"
    print(resultado)

# Gerar arquivo de saída
"""
saida_path = os.path.join(base_dir, "saida.txt")
with open(saida_path, "w", encoding="utf-8") as f:
    f.write(resultado)

print(f"Arquivo de saída gerado em: {saida_path}")
"""