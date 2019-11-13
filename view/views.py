from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsProject

message_welcome = 'Bienvenido a la ejecución de los \nprimeros mensajes en QGIS 3.8.0 Zanzibar'
message_projectname = QgsProject.baseName
QMessageBox.information(iface.mainWindow(), 'Mensaje Bienvenida', message_welcome)
QMessageBox.information(iface.mainWindow(), 'Mensaje Bienvenida', message_projectname)

