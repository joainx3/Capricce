import pyodbc

server = 'DESKTOP-U0R51TM' 
bd = 'CAPRICCE'
usuario = 'sadmin'
contra = '123'


try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='
                             +bd+';UID='+usuario+';PWD='+ contra)
    print ('conexion exitosa')
except:
    print('Error al intentar conectarse')
    