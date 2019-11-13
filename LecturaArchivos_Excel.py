# List of constants
WORK_DIRECTORY = 'G:/COUNTRY/GIS/Workspace/191108_WC_MapasFBM/'
ORIGEN_FILE = 'src/01_ListadoMapasTrabajar.xls'
WORK_FILE = os.path.join(WORK_DIRECTORY, ORIGEN_FILE)

# Reading file of the origin of data
import xlrd
import xlwt
import xlutils
workbook = xlrd.open_workbook(WORK_FILE)

value = layer.getFeature(2).attribute(2)
expresion = '\"ApplicationNumber\" like \'7524\''
layer.selectByExpression(expresion, QgsVectorLayer.SetSelection)

print (attribute(1))