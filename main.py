import time

import pyautogui
# Procura instalar las librerias de pillow y pyscreeze

"""
pyautogui.moveTo(100,100,duration=1) # Mover el ratón
pyautogui.click()# Clic en la posición actual
pyautogui.typewrite("Hola, PyAutoGUI!") # Escribir texto
"""

"""
Captura de pantalla
screenshot = pyautogui.screenshot()
screenshot.save("imagen.png")
"""


#pyautogui.hotkey('ctrl','d') Simular teclas

#pyautogui.moveTo(100, 200, duration=1) pyautogui.move(x, y, duration=1): Mueve el ratón relativo a su posición actual.
#print(pyautogui.position()) Devuelve la posición actual del cursor. Point(x=100, y=200)

#time.sleep(7)
# Clic en la posición actual
#pyautogui.click()

# Clic derecho
#pyautogui.rightClick()

# Doble clic
#pyautogui.doubleClick()

# Arrastrar y soltar
#pyautogui.dragTo(300, 300, duration=2)
#print(pyautogui.position())

#time.sleep(4)
#pyautogui.typewrite("Hola",interval=0.5) Simula la escritura

#time.sleep(4)
#pyautogui.hotkey('ctrl','d')
#pyautogui.press('enter')

#Lista de teclas validas
#print(pyautogui.KEYBOARD_KEYS)

"""
time.sleep(6)
pyautogui.hotkey('win','d') #Ir a escritorio
time.sleep(6)
image_location = pyautogui.locateOnScreen('uipath.png') #Box(left=128, top=3, width=81, height=79)
time.sleep(6)
if image_location:
    print("Elemento encontrado:", image_location)
    pyautogui.doubleClick(image_location)
else:
    print("No se encontro el elemento")
    
Ajusta la precision 
image_location = pyautogui.locateOnScreen('uipath.png', confidence=0.8)
"""
#time.sleep(5)

"""
Da 5 veces doble click en las coordenadas x:500, y:500
for _ in range(5):
    pyautogui.doubleClick(500,500)
    time.sleep(2)
"""

time.sleep(5)
pyautogui.moveTo(300,300,duration=1)
pyautogui.dragTo(400,300,duration=1)
pyautogui.dragTo(400,400,duration=1)
pyautogui.dragTo(300,400,duration=1)
pyautogui.dragTo(300,300,duration=1)



