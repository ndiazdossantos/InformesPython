from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

fila1 = ["", "Luns", "Martes", "Mercores", "Xoves", "Venres", "Sabado", "Domingo"]
fila2 = ["Mañan", "Clase", "Clase", "Clase", "Clase", "Clase", "Piscina", "Vermu"]
fila3 = ["Tarde", "Adestramento", "Instrumento", "Traballo", "Traballo", "Adestramento", "Traballo", "-"]
fila4 = ["Noite", "-", "Traballo", "-", "-","Traballo","-","-"]

taboa = Table([fila1, fila2, fila3, fila4])

taboa.setStyle([("TEXTCOLOR", (1, -4), (7, -4), colors.red), ("TEXTCOLOR", (0, 0), (0, 3), colors.blue)])
taboa.setStyle([("BACKGROUND", (1, 1), (-1, -1), colors.aliceblue)])
taboa.setStyle([("INNERGRID", (1, 1), (-1, -1), 0.25, colors.darkgrey)])

doc = [taboa]

documento = SimpleDocTemplate("informeTaboa.pdf", pagesize = A4, showBoundary=0)
documento.build(doc)