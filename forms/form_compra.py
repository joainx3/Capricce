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

        
        self.ventana.mainloop()
