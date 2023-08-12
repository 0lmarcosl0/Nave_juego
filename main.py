import tkinter as tk
import game

def cerrar_ventana():
	ventana.quit()
	
def iniciar_juego():
	ventana.destroy()
	game.Game()
ventana = tk.Tk()
ventana.title("menu")
ventana.geometry("650x420")
ventana.config(bg = "black")

boton_jugar = tk.Button(ventana,text = "jugar",command=iniciar_juego,height = 1,width = 6,font=("ariel",20))
boton_jugar.place(x = 290, y = 110)

boton_salir= tk.Button(ventana,text = "salir",command=cerrar_ventana,height = 1,width = 6,font=("ariel",20))
boton_salir.place(x = 290, y = 210)

ventana.mainloop()