from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

arquivo_teste = "tubos.pdf"

c = canvas.Canvas(arquivo_teste, pagesize=A4)
largura, altura = A4

# Adicionando linhas semelhantes ao PDF original
c.drawString(50, altura - 50, "FQ 25617.2022")
c.drawString(50, altura - 70, "ORDEM DE SERVIÇO Nº 190245 Revisão 01")
c.drawString(50, altura - 90, "19/02/2025")
c.drawString(50, altura - 110, "CLIENTE QUANT. DESCRICAO_PRODUTO_SERVICO DESENHO REVIS.")
c.drawString(50, altura - 130, "TUBOS 1023 TUBO PARA ENGATE RAPIDO TUBO2345-A AZ1")
c.showPage()
c.save()
print("PDF de teste criado!")
