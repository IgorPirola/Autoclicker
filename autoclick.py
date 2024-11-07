import pyautogui
import keyboard as kb
import time
import sys
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

#messagebox.showinfo("Box", "Programa iniciado\nF8 para clicar \nF7 para parar \nF9 para finalizar")
print("Programa iniciado") 
print("F8 para clicar") 
print("F7 para parar") 
print("F9 para finalizar")
print("")

def click():
    print("Começou a clicar")
    print("")
    while True:
        pyautogui.click()
        time.sleep(0.05)
        if kb.is_pressed('f7'):
            #messagebox.showinfo("Box", "Parou de clicar")
            break
        if kb.is_pressed('f9'):
            #messagebox.showinfo("Box", "Programa finalizado")
            sys.exit()

while True:
    if kb.is_pressed('f8'):
        click()
    else:
        time.sleep(0.05)
    if kb.is_pressed('f9'):
        #messagebox.showinfo("Box", "Programa finalizado")
        sys.exit()
