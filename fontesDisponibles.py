from reportlab.pdfgen import canvas

cadea = "Tipo de letra de exemplo con ReportLab"
doc = canvas.Canvas("tiposLetra.pdf")

obxTexto = doc.beginText(20,500)

for tipo in doc.getAvailableFonts():
    obxTexto.setFont(tipo,12)
    obxTexto.textLine(tipo + ": "+cadea)
doc.drawText(obxTexto)

doc.showPage()
doc.save()