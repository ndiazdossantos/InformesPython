from reportlab.pdfgen import canvas

documento = canvas.Canvas("primeiroInforme.pdf")
documento.drawString(0, 0, "Posicion (X,Y) = (0,0)")
documento.drawString(50, 100, "Posicion (X,Y) = (50,100)")
documento.drawString(150, 40, "Posicion (X,Y) = (150,40)")
documento.drawString(150, 150, "Posicion (X,Y) = (150,150)")
documento.drawImage("/home/dam2a/Descargas/vaca-lechera.jpg", 200, 200, 356, 497)
documento.showPage()
documento.save()