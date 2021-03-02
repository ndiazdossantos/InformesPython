import sqlite3 as dbapi
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing


listaTaboa = []
listaDatosEdade=[]
listaTaboa.append(("Dni", "Nome", "Direccion", "Edade", "Sexo"))
listaDatosNome=[]


try:
    bbdd = dbapi.connect("baseDatosTV.dat")
except dbapi.StandardError as e:
    print(e)
else:
    print("Base de datos aberta")
try:
    cursor = bbdd.cursor()
    cursor.execute("select * from usuarios")

    for fila in cursor.fetchall():
        listaTaboa.append(fila)
        listaDatosEdade.append(fila[3])
        listaDatosNome.append(fila[1])

except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: " + str(e))
else:
    print("Consulta executada")
finally:
    cursor.close()
    bbdd.close()

taboa = Table(listaTaboa)

taboa.setStyle([("TEXTCOLOR", (0, 0), (-1, 0), colors.red)])
taboa.setStyle([("BACKGROUND", (0, 1), (-1, -1), colors.aliceblue)])
taboa.setStyle([("INNERGRID", (0, 1), (-1, -1), 0.25, colors.darkgray)])
doc = []
doc = [taboa]

d = Drawing (400,200)
gb = VerticalBarChart()
gb.x = 50
gb.y = 50
gb.height = 125
gb.width = 300
gb.data = [listaDatosEdade]
gb.strokeColor=colors.black
gb.valueAxis.valueMin = 0
gb.valueAxis.valueMax = 100
gb.valueAxis.valueStep = 10
gb.categoryAxis.labels.boxAnchor = 'ne'
gb.categoryAxis.labels.dx = 8
gb.categoryAxis.labels.dy = -2
gb.categoryAxis.labels.angle = 30
gb.categoryAxis.categoryNames = listaDatosNome
gb.groupSpacing = 10
gb.barSpacing = 2
d.add(gb)
doc.append(d)


documento = SimpleDocTemplate ("informeDB.pdf", pagesize=A4, showBoundary=0)
documento.build(doc)

