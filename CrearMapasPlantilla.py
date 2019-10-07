######## INICIO SCRIPT CREAR MAPA EN COMPOSER ########
# -*- coding: utf-8 -*- # Se debe identificar la codificación del archivo para ejecutarlo en QGIS
##
##
##
# Objetivo de la rutina:
## - Crear una mapa utilizando una plantilla existente, y cargar una capa para mostrar las
##    entidades de interés.
#Fecha:
##- Octubre 10 de 2019
#Desarrollado por:
## David Alonso Rueda Rodríguez - daruedar@correo.udistrital.edu.co
# Listado de versiones:
## 000. Se crea archivo que crea mapa desde plantilla, solicita al usuario el nombre y directorio
##         de la plantilla de referencia.
## 

#Cargar librerías
from qgis.utils import iface
from PyQt4.QtGui import QInputDialog, QFileDialog
from qgis.PyQt.QtXml import QDomDocument
import os, sys

# Ingresar el nombre del mapa
nombre_del_mapa = str(QInputDialog.getText(None, "Nombre Mapa", "Ingrese el Nombre del Mapa: ")[0])
print("El nombre del mapa ingresado fue: {}" .format(nombre_del_mapa))

# Selección de rutas de plantilla
ruta_plantilla = QFileDialog.getOpenFileName(QFileDialog(), 'Seleccionar Plantilla del Mapa', 'C:\\', "qpt(*.qpt)")
print("El nombre del mapa ingresado fue: {}" .format(fname ))

#Creación de nuevo documento basado en una plantilla existente
# Tomada desde https://gis.stackexchange.com/questions/157807/programmatically-import-new-composer-from-template-to-project-using-pyqgis
myTemplateFile = file(ruta_plantilla, 'rt')
myTemplateContent = myTemplateFile.read()
myTemplateFile.close()
myDocument = QDomDocument()
myDocument.setContent(myTemplateContent, False)
newcomp = iface.createNewComposer(str(nombre_del_mapa))
newcomp.composition().loadFromTemplate(myDocument)