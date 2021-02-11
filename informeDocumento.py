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
cabeceira.keepWithNext = 0
cabeceira.backColor = colors.gainsboro
paragrafo = Paragraph("Cabeceira do documento", cabeceira)
doc.append(paragrafo)

informe = SimpleDocTemplate("exemploInforme.pdf", pagesize=A4, showBoundary = 1)
informe.build(doc)
