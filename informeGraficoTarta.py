from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate


guion= []

d = Drawing (300, 200)
tarta = Pie()
tarta.x = 65
tarta.y = 15
tarta.width = 170
tarta.height = 170
tarta.data =[10,20,30,40,50]
tarta.labels = ['Brave', 'Opera', 'Edge', 'Firefox', 'Chrome']

tarta.slices.strokeWidth = 0.5
tarta.slices[3].popout = 10
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [2,5]
tarta.slices[3].labelRadius = 1.75
tarta.slices[3].fontColor = colors.red

tarta.sideLabels = 1

lenda = Legend ()
lenda.x = 370
lenda.y = 0
lenda.dx = 8
lenda.dy = 8
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.darkgrey
lenda.deltax = 75
lenda.deltay = 10
lenda.autoXPadding = 10
lenda.yGap = 0
lenda.dxTextSpace = 10
lenda.alignment = 'right'
lenda.dividerLines = 7
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30

colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.pink]
for i, color in enumerate (colores):
    tarta.slices[i].fillColor = color

lenda.colorNamePairs =[(tarta.slices[i].fillColor,
                        (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])
                        ) for i in range (len(tarta.data))]

d.add (tarta)
d.add (lenda)

guion.append (d)


doc = SimpleDocTemplate("exemploTarta.pdf", pagesize = A4)
doc.build(guion)
