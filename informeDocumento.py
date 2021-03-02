import os
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo = getSampleStyleSheet()

doc = []

cabeceira = follaEstilo["Heading4"]
cabeceira.pageBreakBefore = 0
cabeceira.keepWithNext = 1
cabeceira.backColor = colors.gainsboro
paragrafo = Paragraph("Cabeceira do documento", cabeceira)
doc.append(paragrafo)

cadea = "Creamos unha cadea de recheo. " * 700

#escollemos o estilo
#no momento que utilizamos o mesmo nome dunha variable ó chegar a ese punto a sobreescribimos
corpoTexto = follaEstilo["BodyText"]
paragrafo = Paragraph(cadea, corpoTexto)
doc.append(paragrafo)

doc.append(Spacer(0, 20))

imaxe = Image(os.path.realpath("/home/noe/Descargas/vaca-lechera.jpg"), width=396, height=106)
doc.append(imaxe)


informe = SimpleDocTemplate("exemploInforme.pdf", pagesize=A4, showBoundary = 1)
informe.build(doc)

#showboundary sirve para rodear con un cuadro la página