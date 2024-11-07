import pyautogui
import keyboard as kb
import time
import sys

print("Programa iniciado") 
print("F8 para clicar") 
print("F7 para parar") 
print("f9 para finalizar")
print("")

def click():
    print("Começou a clicar")
    print("")
    while True:
        pyautogui.click()
        time.sleep(0.05)
        if kb.is_pressed('f7') or pyautogui.position() != (posicao):
            print("Parou de clicar")
            print("")
            break
        if kb.is_pressed('f9'):
            print("Programa finalizado")
            sys.exit()

while True:
    if kb.is_pressed('f8'):
        posicao = pyautogui.position()
        click()
    else:
        time.sleep(0.05)
    if kb.is_pressed('f9'):
        print("Programa finalizado")
        sys.exit()
