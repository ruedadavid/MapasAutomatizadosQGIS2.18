def select_data(vlayer, field ='', data = '', zoom = False):
    if vlayer==None:
        vlayer = iface.activeLayer()
    if field =='':
        field_found = vlayer.setSubsetString("")
    else:
        # Previamente se debe validar el tipo de dato
        # para asignar el operador correspondiente
        field_found = vlayer.setSubsetString("\"{}\" = '{}'" .format(field, data))
    return field_found

def select_feature(vlayer, field ='', data = '', zoom = False):
    exp = "\"{}\" like {}" .format(field, data)
    vlayer.selectByExpression(exp)
    return 