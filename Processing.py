''' Se ha creado una class llamada Game con funciones
- def __init__() para iniciar el constructor de la class Game
_ def run(self) funcion para iniciar
- def__process(self) para el proceso'''

# Importamos las librerias de mayor a menor gerarquia
import os
import cv2
import keyboard
from fun_get_shapes import get_shapes

# Definimos la class
class Game:


    def __init__(self):
        # Es el constructor
        pass
    def run(self):
        print("Precaución Iniciando Operaciones")
        self.__process()

    def __process(self):
        # leer el path donde estan las imagenes
        _path = "resources"
        print(f'veamos: { _path}')
        #Lista con los nombres de las imagenes
        files_names = os.listdir(_path)

        _running = True

        # Bucle infinito mientras running este en True
        while _running:
            # Recorriendo la lista donde esta las imagenes
            for file_name in files_names:
                image = cv2.imread(_path + "/" + file_name)

                # Para dibujar los contornos pero mantener la imagen original hacemos una copia de la misma
                image_contour = image.copy()

                # Cambio de espacio de color de BGR a escala de grises
                _image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Desenfoque gaussiano
                _image_blur = cv2.GaussianBlur(_image_gray, (3, 3), 0)

                #   Detector de bordes Canny
                image_canny = cv2.Canny(_image_blur, 50, 50)

                # Instancia de la funcion get_shapes
                # Como parámetro para la función, pasaremos la imagen resultante del detector de bordes
                get_shapes(image_canny, image_contour)
                # Podemos ver como el detector de bordes muestra los contornos
                cv2.imshow("Result", image_contour)

                cv2.waitKey(500)

                # Code para salir del bucle While pulsando la tecla q
                if keyboard.is_pressed("q"):
                    _running = False
                    break



