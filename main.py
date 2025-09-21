import pdfplumber
import os

"""
Esse script gera a marcação no modelo selecionado, altere aqui o nome do pdf e escolha o tipo de gravação.
"""
# Encontrando o arquivo, o arquivo .pdf tem que estra no mesmo local que  o main.py
base_dir = os.path.dirname(os.path.abspath(__file__))  # pasta do script
arquivo = os.path.join(base_dir, "os_teste.pdf") # insira o nome do arquivo


def gravacao_simples():
    """A gravação padrão mais utilizada: """
    pn = dicionario['DESENHO']
    rev = dicionario['REVIS.']
    serial = dicionario['QUANT.']

    if serial == 1:
        return pn + " " + rev + " " + f"00{serial}"
    elif serial < 10:
        return pn + " " + rev + " " + f"001 a 00{serial}"
    elif serial >= 10 and serial < 100:
        return pn + " " + rev + " " + f"001 a 0{serial}"
    elif serial >= 100:
        return pn + " " + rev + " " + f"001 a {serial}"


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
        break


print("""
1 - Gravação Simples: PN + REV + SERIAL
\n""")

opcao = int(input('Escolha a opção de gravação: '))

if opcao == 1:
    
    resultado = f"\nA gravação é: {gravacao_simples()}\n"
else:
    resultado = "\nOpção Inválida\n"

# Gerar arquivo de saída

saida_path = os.path.join(base_dir, "saida.txt")
with open(saida_path, "w", encoding="utf-8") as f:
    f.write(resultado)

print(f"Arquivo de saída gerado em: {saida_path}")