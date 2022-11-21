from ast import If
import threading
from tkinter import * 
from pynput import keyboard
 
def on_press(key):
    try:
        #print(str(key))
        if str(key) == 'Key.up':
            print("Se suvio de velocidad")
        elif str(key) == 'Key.down':
            print("se bajo de velocidad")    
    except AttributeError:
        print('2- pressed' + str(key))
        
def on_release(key):
    #print('3- released' + str(key))
    if key == keyboard.Key.esc:
        return False
 
def escuchar():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
 
def ventana():
    master = Tk()
    master.geometry("500x500")
    w = Label(master, text="Hello, world!")
    w = Label(master, text="casco")
    w.pack()
    mainloop()
 
hilo1 = threading.Thread(target = ventana)
hilo2 = threading.Thread(target = escuchar)
 
hilo1.start()
hilo2.start()
