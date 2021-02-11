from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imaxes = []
imaxe = Image(150, 50, 589, 202, "/home/dam2a/Descargas/vaca-lechera.jpg")

debuxo = Drawing(500, 102)
debuxo.translate(0, 650)  #movelo de posición
debuxo.add(imaxe)

debuxo2 = Drawing(250, 51)
debuxo2.add(imaxe)
debuxo2.rotate(45)
debuxo2.scale(0.5, 1.5)
debuxo2.translate(150,-45)
imaxes.append(debuxo2)

imaxes.append(debuxo)
documento = Drawing(A4[0], A4[1])

for elemento in imaxes:
    documento.add(elemento)

renderPDF.drawToFile(documento, "segundoInforme.pdf")

