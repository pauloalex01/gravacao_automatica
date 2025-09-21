# Gravação Automática de Ordens de Serviço

Descrição
---------
Script Python que automatiza a extração de dados de PDFs de ordens de serviço e gera a gravação das peças no formato desejado, futuras versões adicionaram novos formatos. O repositório contém apenas **PDFs de teste** (estrutura idêntica aos PDFs reais) para que a execução possa ser demonstrada sem expor dados da empresa.
Os dados coletados com o pdfplumber ficam no exato formato dos pdfs de teste, mas por motivos de não vazamentos de dados, não posso mostrar os pdf's reais.
Utilizarei como uma forma de automatizar as gravações

Funcionalidade
--------------
- Lê PDF usando `pdfplumber`.
- Extrai os campos: CLIENTE, QUANT., DESCRIÇÃO DO PRODUTO/SERVIÇO, DESENHO, REVIS.
- Gera a gravação com a regra padrão: `PN + REV + SERIAL`.
- Gera um arquivo `saida.txt` com o resultado (quando o script estiver na versão que grava saída).

Requisitos
----------
- Python 3.8+  
- Dependências (instalar via `requisitos.txt`)

Instalação
---------
No Linux Mint (terminal):

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requisitos.txt
```

Como usar
---------
1. Ajuste a variável `arquivo` com o nome do pdf em questão (Não esqueça do .pdf).
2. Execute:
```bash
python3 main.py
```
3. Se o script criar `saida.txt`, o arquivo ficará na mesma pasta do script — pronto para copiar.
