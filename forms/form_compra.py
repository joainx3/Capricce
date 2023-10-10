import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl


class OrdenCompras():
    def __init__(self):        
        #Configuración inicial
        self.ventana = tk.Tk()                             
        self.ventana.title('Ordenes de Compra')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)

        # Botón de menú
        btnMenu = tk.Button(self.ventana, text="Menú", font=('Times', 15, BOLD), command=self.abrir_menu)
        btnMenu.pack()
        btnMenu.place(x=0-1,y=0)
        
        self.ventana.mainloop()

    def abrir_menu(self):
        from forms.form_menu import Menu
        self.ventana.destroy()
        Menu()

if __name__ == "__main__":
    app = OrdenCompras()
