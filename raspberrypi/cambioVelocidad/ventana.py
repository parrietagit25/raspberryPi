import tkinter
import tkinter.font as tkFont
from pynput import keyboard as kb

ventana = tkinter.Tk()
ventana.title("Cambios V-1")
ventana.geometry("500x500")
ventana.resizable(0,0)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
cabeza = tkinter.Label(ventana, text = "Xolito bruto", font=fontStyle).pack()

def pulsa(tecla):
	cabeza = tkinter.Label(ventana, text = print('Se ha pulsado la tecla ' + str(tecla)), font=fontStyle).pack()

with kb.Listener(pulsa) as escuchador:
	escuchador.join()

ventana.mainloop()
	

