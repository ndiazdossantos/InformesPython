from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

datos = [
    ['Arriba/esquerda', '', '02', '03', '04'],
    ['', '', '12', '13', '14'],
    ['20', '21', '22', 'Abaixo/dereita', ''],
    ['30', '31', '32', '', '']
]

estilo = [
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (1,1), 'MIDDLE'),
    ('BACKGROUND', (0,0), (1,1), colors.azure),
    ('SPAN', (0,0), (1,1)),#span une un intervalo de celdas que indiquemos
    ('BACKGROUND', (3,2), (4,3), colors.burlywood),
    ('SPAN', (-2,-2), (-1,-1))
]

taboa = Table(data=datos, style=estilo)


doc = [taboa]

documento = SimpleDocTemplate("informeCombinacionesCelda.pdf", pagesize = A4, showBoundary=0)
documento.build(doc)