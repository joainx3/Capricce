import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_compra import OrdenCompras


class Menu():      
      
      #Cierra sesión del usuario
      def CerrarSesion(self):
            self.ventana.destroy()
      
      #Acción para que vaya a la ventana ordenes de compra
      def OrdenCompra(self):
            self.ventana.destroy()
            OrdenCompras()

      def __init__(self):        
         #Configuración inicial
         self.ventana = tk.Tk()                             
         self.ventana.title('Capricce')
         self.ventana.geometry('800x500')
         self.ventana.config(bg='#fcfcfc')
         self.ventana.resizable(width=0, height=0)    
         utl.centrar_ventana(self.ventana,800,500)

         frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
         frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

 

         #Boton cerrar sesión
         btnCerrarS = tk.Button(frame_form,text="Cerrar Sesión",font=('Times', 15,BOLD), command=self.CerrarSesion)
         btnCerrarS.pack()
         btnCerrarS.place(x=0-1,y=0)

         #Boton compras
         btnCompras = tk.Button(frame_form,text="Ordenes de compra",font=('Times', 15,BOLD), command=self.OrdenCompra)
         btnCompras.pack()
         btnCompras.place(x=330,y=250)

         self.ventana.mainloop()