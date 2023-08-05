import tkinter as tk
import pygame

medida = (650, 650)
azul = (0, 0, 255)

var = False

def cerrar_ventana():
    ventana.destroy()

def abrir_vent_go():
    ventana.withdraw()
    global var
    var = True


pygame.init()

ven_go = pygame.display.set_mode(medida)
pygame.display.set_caption("juego")

ventana = tk.Tk()
ventana.title("menu")
ventana.geometry("650x650")
ventana.config(bg="black")


boton_salir = tk.Button(ventana, text="salir", command=cerrar_ventana)
boton_salir.pack()

boton_jugar = tk.Button(ventana, text="jugar", command=abrir_vent_go)
boton_jugar.pack()

ventana.mainloop()

while not var: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = True

pygame.quit()

ventana.destroy()
