# -*- coding: utf-8 -*- # Se debe identificar la codificación del archivo para ejecutarlo en QGIS

def crear_mapa_plantilla(nombre_del_mapa, ruta_plantilla, datos_plantilla={}):
    """
    Documentación función crear_mapa_plantilla()
    
    Objetivo de la función:
        - Crear un mapa utilizando las capas cargadas en
            QGIS 2.18.x y utilizando una plantilla previamente
            diseñada

    Parámetros:
        nombre_del_mapa = Cadena de caracteres con el
            nombre final del mapa
        ruta_plantilla = Ruta donde se aloja la plantilla que
            se utilizará como base para presentar las salidas
            gráficas correspondientes
    
    Retorno:
        1. Mapa en la sección de composición con los datos
            de interés.
        2. Aviso informativo informando de la finalización
            de la actividad en la barra de mensajes.
    
    Fecha: Octubre 10 de 2019
    Autor: David Alonso Rueda Rodríguez
    Otro: Desarrollado para QGIS 2.18
    
    Listado de versiones:
    
    000. Se crea una función para creación del mapa en 
        la ventana de composición.    
    01. Se crea archivo que crea mapa desde plantilla,
        solicita al usuario el nombre y directorio de la
        plantilla de referencia.
    """
    #Cargar librerías
    from qgis.utils import iface
    from PyQt4.QtGui import QInputDialog, QFileDialog
    from qgis.PyQt.QtXml import QDomDocument
    import os, sys

    #Creación de nuevo documento basado en una plantilla existente
    # Tomada desde https://gis.stackexchange.com/questions/157807/programmatically-import-new-composer-from-template-to-project-using-pyqgis
    myTemplateFile = file(ruta_plantilla, 'rt')
    myTemplateContent = myTemplateFile.read()
    myTemplateFile.close()
    myDocument = QDomDocument()
    myDocument.setContent(myTemplateContent, False)
    newcomp = iface.createNewComposer(str(nombre_del_mapa))
    newcomp.composition().loadFromTemplate(myDocument)