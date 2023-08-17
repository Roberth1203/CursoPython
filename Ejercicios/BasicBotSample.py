import pyautogui as pg
import time

#Ejemplo sencillo de un bot para enviar el contenido de un archivo .txt

flag = pg.confirm(text='¿Desea iniciar el envío de datos?', title='Confirmación', buttons=['OK', 'Cancel'])

def enviarDatos():
    time.sleep(10)
    msg = "saben is a"
    txt = open('./assets/animals.txt','r')
    
    for i in txt:
        pg.write(msg + ' ' + i)
        pg.press('Enter')

if (flag == 'OK'):
    enviarDatos()
else:
    pg.alert(text='Se ha cancelado el envío de datos.', title='Python dice', button='Ok')