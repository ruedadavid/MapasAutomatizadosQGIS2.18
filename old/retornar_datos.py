# -*- coding: utf-8 -*- # Se debe identificar la codificación del archivo para ejecutarlo en QGIS
def retornar_datos(dato_buscado, campo, lista_campos=[]):
    """
    Documentación función retornar_datos()
    
    Objetivo de la función:
        - Seleccionar elemento de la capa activa (capa seleccionada en la tabla 
        de contenido) haciendo una consulta por atributo, esta función
        se ha desarrollado para QGIS 3.x, retorna un diccionario con los datos
        requeridos
        
    Parámetros:
        campo = Cadena de caracteres con el nombre del campo sobre el cual se
            hace la consulta
        dato_buscado = Cade de caracteres con el valor buscado
        lista_campos = Lista con el nombre de los campos requeridos para ser
            retornados
    
    Retorno:
        1. Diccionario con los datos requeridos y su valor asociado
    
    Listado de versiones:
    
    000. Versión se ajusta para retornar un diccionario con los datos requeridos
    01. Primera versión retornaba una sóla cadena de caracteres por cada consulta
    """
    layer = iface.activeLayer()
    if layer:
        if len(lista_campos)==0:
            lista_campos.append (campo)
        exp = '\"{}\" like \'{}\''.format(campo, dato_buscado)
        layer.selectByExpression(exp)
        sel = layer.selectedFeatures()
        if sel:
            datos_requeridos = {str(i):sel[0][i] for i in lista_campos}
            canvas = qgis.utils.iface.mapCanvas()
            canvas.zoomToSelected()
            lista_campos = []
            return datos_requeridos
        else:
            lista_campos = []
            return ('Dato no encontrado')
    else:
        print("No hay capas activas en el entorno de trabajo")