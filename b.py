from time import sleep
import pyautogui as gui



def benemerito():
       
        print('Comenzando con Benemerito')

        sleep(3)
        print('Click en el sitio')
        gui.moveTo(122,258)
        gui.doubleClick()


        print('Comenzando Benemerito 1')

        sleep(2)
        gui.moveTo(431, 330)
        gui.rightClick()

        print("click en el NCE")
        sleep(4)
        gui.moveTo(470, 201)
        gui.click()


        sleep(5)
        print('Entrando al NCE')

        ## Script para la busqueda y descarga de archivos
        print('Busqueda wdm')
        sleep(4)
        print('Escribiendo... wdm')
        gui.moveTo(131, 481)
        gui.doubleClick()
        gui.write('wdm')

        print('Click en wdm')
        sleep(2)
        gui.moveTo(120, 541)
        gui.doubleClick()

        print('Explorer')
        sleep(3)
        print('Scroll')
        gui.moveTo(1355, 640)
        gui.click()

        print('Guardar archivo')
        print('Click en save')
        sleep(3)
        gui.moveTo(1243, 595)
        gui.click()

        print('Save as...')
        gui.moveTo(1224, 640)
        sleep(3)
        gui.click()

        sleep(2)
        print('Click en ok')
        gui.moveTo(752, 495)
        gui.click()

        # Scrip General para cerrar todas las ventanas del sitio
        print('Cerrando Todo!!!!!')
        sleep(2)
        gui.moveTo(64, 145)
        gui.rightClick()

        gui.moveTo(108,244)
        gui.click()



def letter_B():
        benemerito()