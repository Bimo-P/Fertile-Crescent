#1. add Open Street Map Background (basemap)
tms = 'type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0'
OSM = QgsRasterLayer(tms,'OSM', 'wms')
QgsProject.instance().addMapLayer(OSM)

#2. Create Polygon
Layer = QgsVectorLayer('Polygon?EPSG : 3857','Fertile Crescent','memory')

Geom = [QgsPointXY(38.86,33.53),    
        QgsPointXY(39.64,33.54),
        QgsPointXY(40.05,33.43),
        QgsPointXY(41.11,32.86),
        QgsPointXY(41.86,32.34),
        QgsPointXY(42.53,31.88),
        QgsPointXY(43.51,31.44),
        QgsPointXY(44.11,31.09),
        QgsPointXY(44.71,30.71),
        QgsPointXY(45.34,30.44),
        QgsPointXY(45.76,30.32),
        QgsPointXY(46.25,30.08),
        QgsPointXY(46.86,30.03),
        QgsPointXY(47.78,29.98),
        QgsPointXY(47.89,30),
        QgsPointXY(48.26,29.95),
        QgsPointXY(48.44,29.88),
        QgsPointXY(48.62,29.94),
        QgsPointXY(48.68,30.03),
        QgsPointXY(48.93,30.11),
        QgsPointXY(48.89,30.22),
        QgsPointXY(48.86,30.35),
        QgsPointXY(49.15,30.26),
        QgsPointXY(49.26,30.15),
        QgsPointXY(49.48,30.14),
        QgsPointXY(49.58,30.03),
        QgsPointXY(49.9,30.21),
        QgsPointXY(50.09,30.2),
        QgsPointXY(50.15,30),
        QgsPointXY(50.27,29.74),
        QgsPointXY(50.57,29.54),
        QgsPointXY(50.68,29.46),
        QgsPointXY(50.68,29.33),
        QgsPointXY(50.64,29.2),
        QgsPointXY(50.66,29.15),
        QgsPointXY(50.73,29.11),
        QgsPointXY(50.8,29.14),
        QgsPointXY(50.92,29.07),
        QgsPointXY(50.91,29),
        QgsPointXY(50.85,28.96),
        QgsPointXY(50.84,28.82),
        QgsPointXY(50.98,28.83),
        QgsPointXY(51.05,28.7),
        QgsPointXY(51.14,28.38),
        QgsPointXY(51.9,28.65),
        QgsPointXY(51.57,29.09),
        QgsPointXY(51.77,29.72),
        QgsPointXY(51.64,30.17),
        QgsPointXY(51.38,30.72),
        QgsPointXY(50.45,31.7),
        QgsPointXY(49.71,32.33),
        QgsPointXY(48.9,32.85),
        QgsPointXY(47.72,33.74),
        QgsPointXY(46.56,34.06),
        QgsPointXY(45.78,34.67),
        QgsPointXY(45.32,35.33),
        QgsPointXY(44.34,35.73),
        QgsPointXY(43.47,36.18),
        QgsPointXY(43.14,36.67),
        QgsPointXY(41.86,37.53),
        QgsPointXY(40.93,37.97),
        QgsPointXY(39.29,38.01),
        QgsPointXY(37.13,37.83),
        QgsPointXY(36.22,37.65),
        QgsPointXY(35.37,37.33),
        QgsPointXY(34.75,37),
        QgsPointXY(35.07,36.67),
        QgsPointXY(35.36,36.65),
        QgsPointXY(35.65,36.65),
        QgsPointXY(35.88,36.84),
        QgsPointXY(36.02,36.92),
        QgsPointXY(36.23,36.77),
        QgsPointXY(36.24,36.79),
        QgsPointXY(36.21,36.59),
        QgsPointXY(36.03,36.51),
        QgsPointXY(35.77,36.3),
        QgsPointXY(36,35.98),
        QgsPointXY(35.9,35.94),
        QgsPointXY(35.83,35.84),
        QgsPointXY(35.87,35.74),
        QgsPointXY(35.8,35.63),
        QgsPointXY(35.75,35.54),
        QgsPointXY(35.84,35.48),
        QgsPointXY(35.91,35.41),
        QgsPointXY(35.92,35.3),
        QgsPointXY(35.91,35.1),
        QgsPointXY(35.89,34.97),
        QgsPointXY(35.89,34.97),
        QgsPointXY(36,34.57),
        QgsPointXY(35.79,34.41),
        QgsPointXY(35.63,33.99),
        QgsPointXY(35.55,33.9),
        QgsPointXY(35.46,33.89),
        QgsPointXY(35.49,33.81),
        QgsPointXY(35.31,33.45),
        QgsPointXY(35.03,32.77),
        QgsPointXY(34.96,32.83),
        QgsPointXY(34.83,32.33),
        QgsPointXY(34.69,31.9),
        QgsPointXY(34.57,31.69),
        QgsPointXY(34.42,31.51),
        QgsPointXY(34.21,31.28),
        QgsPointXY(33.8,31.16),
        QgsPointXY(33.72,31.12),
        QgsPointXY(33.52,31.1),
        QgsPointXY(33.42,31.17),
        QgsPointXY(33.36,31.14),
        QgsPointXY(33.11,31.04),
        QgsPointXY(33.04,31.14),
        QgsPointXY(32.97,31.06),
        QgsPointXY(32.8,31.06),
        QgsPointXY(32.68,31.05),
        QgsPointXY(32.4,31.16),
        QgsPointXY(31.92,31.47),
        QgsPointXY(31.78,31.44),
        QgsPointXY(31.55,31.43),
        QgsPointXY(31.2,31.52),
        QgsPointXY(31,31.51),
        QgsPointXY(30.89,31.39),
        QgsPointXY(30.76,31.52),
        QgsPointXY(30.37,31.45),
        QgsPointXY(30.36,31.34),
        QgsPointXY(29.96,31.21),
        QgsPointXY(29.59,30.98),
        QgsPointXY(29.53,30.54),
        QgsPointXY(29.54,30.45),
        QgsPointXY(29.48,29.01),
        QgsPointXY(29.6,28),
        QgsPointXY(29.93,26.84),
        QgsPointXY(30.37,25.88),
        QgsPointXY(31.04,25.09),
        QgsPointXY(31.65,24.51),
        QgsPointXY(32.23,24.18),
        QgsPointXY(32.62,24.11),
        QgsPointXY(32.88,24.3),
        QgsPointXY(33.25,24.52),
        QgsPointXY(33.34,24.66),
        QgsPointXY(33.34,24.96),
        QgsPointXY(33.31,25.27),
        QgsPointXY(33.14,25.57),
        QgsPointXY(32.84,26.1),
        QgsPointXY(32.74,26.49),
        QgsPointXY(32.53,26.75),
        QgsPointXY(32.12,27.22),
        QgsPointXY(32.1,27.55),
        QgsPointXY(31.96,27.75),
        QgsPointXY(31.91,28.05),
        QgsPointXY(31.87,28.43),
        QgsPointXY(31.88,28.9),
        QgsPointXY(32.1,29.21),
        QgsPointXY(32.63,29.55),
        QgsPointXY(33.12,29.87),
        QgsPointXY(33.76,30.38),
        QgsPointXY(34.61,30.85),
        QgsPointXY(35.37,31.28),
        QgsPointXY(35.75,31.75),
        QgsPointXY(36.41,32.19),
        QgsPointXY(37.01,32.71),
        QgsPointXY(37.36,32.97),
        QgsPointXY(38.03,33.23),
]

#print(geom)
poly = QgsGeometry.fromPolygonXY([Geom])

ftr = QgsFeature()
ftr.setGeometry(poly)
print(ftr.geometry()) #from my experience it’s should be Polygon form

Prj = QgsProject.instance()
Prj.addMapLayer(Layer)

prv = Layer.dataProvider()

prv.addFeatures([ftr])

Layer.updateExtents()

#3. create a fill Symbol
renderer = QgsSingleSymbolRenderer(QgsFillSymbol.createSimple({'outline_width':'0.6' , 
                                    'color' : 'transparent',
                                    'outline_color' : '51,160,44,255'}))
Layer.setRenderer(renderer)

Layer.triggerRepaint()

#4.Layouting Map
from qgis.PyQt import QtGui


layers = QgsProject.instance().mapLayersByName('Fertile Crescent')
layer = layers[0]

project = QgsProject.instance()
manager = project.layoutManager()
layoutName = 'Fertile Cersent'
layout_list = manager.printLayouts()
#romve any dupplicate layout
for layout in layout_list :
    if layout.name() == layoutName:
        manager.removeLayout(layout)
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

#remove map item in layout
map = QgsLayoutItemMap(layout)
map.setRect(20,20,20,20)

#set the map extent
ms = QgsMapSettings()
ms.setLayers([layer])
rect = QgsRectangle(22.699,20.611,56.105,43.468)
canvas = iface.mapCanvas()
map.setExtent(rect)
layout.addLayoutItem(map)


map.attemptMove(QgsLayoutPoint(6,8.3,QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(285,195, QgsUnitTypes.LayoutMillimeters))

#5. Add legend
legend = QgsLayoutItemLegend(layout)
legend.setTitle ("Legend")
layerTree = QgsLayerTree ()
layerTree.addLayer(layer)
legend.model().setRootGroup(layerTree)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(230 , 15, QgsUnitTypes.LayoutMillimeters))

#6. add scale bar
scalebar = QgsLayoutItemScaleBar(layout)
scalebar.setStyle('Single Box')
scalebar.setUnits(QgsUnitTypes.DistanceMiles)
scalebar.setNumberOfSegments(3)
scalebar.setNumberOfSegmentsLeft(0)
scalebar.setUnitsPerSegment(100)
scalebar.setLinkedMap(map)
scalebar.setUnitLabel('miles')
scalebar.update()
layout.addLayoutItem(scalebar)
scalebar.attemptMove(QgsLayoutPoint(180, 190, QgsUnitTypes.LayoutMillimeters))


#7. add title

title = QgsLayoutItemLabel(layout)
title.setText("Fertile Cersent")
title.setFont(QFont('Araboto-Black',25))
title.adjustSizeToText()

title.attemptResize(QgsLayoutSize(70,title.boundingRect().height()))
layout.addLayoutItem(title)
title.attemptMove(QgsLayoutPoint(10, 13, QgsUnitTypes.LayoutMillimeters))

#9. export Map

exporter = QgsLayoutExporter(layout)
fn = 'E:/Fertile Crescent.pdf' #put anywhere you want
exporter.exportToPdf(fn, QgsLayoutExporter.PdfExportSettings())

#Sources Learning : 
#gis.stackexchange.com
#youtube channel : geospatial school
#meta AI
