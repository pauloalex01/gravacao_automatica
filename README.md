# Gravação Automática de Ordens de Serviço

Descrição
---------
Script Python que automatiza a extração de dados de PDFs de ordens de serviço e gera a gravação das peças no formato **PN + Revisão + Serial**. O repositório contém apenas **PDFs de teste** (estrutura idêntica aos PDFs reais) para que a execução possa ser demonstrada sem expor dados da empresa.

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

Estrutura do projeto
--------------------
```
gravacao-automatica/
├─ main.py                # (seu script Python)
├─ requisitos.txt
├─ README.md
├─ .gitignore
└─ exemplos/              # PDFs de teste (NÃO incluir PDFs reais/confidenciais)
   ├─ tubos.pdf
   └─ ...
```

Como usar
---------
1. Coloque o PDF de teste em `exemplos/` (ou ajuste a variável `arquivo`).
2. Execute:
```bash
python3 main.py
```
3. Se o script criar `saida.txt`, o arquivo ficará na mesma pasta do script — pronto para copiar.

Boas práticas / Segurança
-------------------------
- **Não** faça upload de PDFs com dados reais da empresa. Use apenas PDFs de teste com a mesma estrutura.
- Use repositório **privado** caso haja qualquer dúvida sobre os arquivos.
- Adicione `__pycache__/`, `.venv/` e outros arquivos temporários no `.gitignore`.

Licença
-------
MIT (ou escolha outra de sua preferência)

Contato
-------
Seu nome / e-mail / LinkedIn
