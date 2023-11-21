import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_compra import OrdenCompras
from forms.form_mostrarorden import MostrarOrdenes
from forms.form_facturas import MostrarFacturas
class Menu():
    def CerrarSesion(self):
        from forms.form_login import App
        self.ventana.destroy()
        App()

    def OrdenCompra(self):
        self.ventana.destroy()
        OrdenCompras()

    def MostrarOrdenes(self):
        self.ventana.destroy()
        MostrarOrdenes()

    def MostrarFactura(self):
        self.ventana.destroy()
      # Llamar al método necesario en la instancia
        MostrarFacturas()
         
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Capricce')
        self.ventana.geometry('1280x720')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 1280, 720)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="CAPRICCE", font=('Times', 70), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        btnCerrarS = tk.Button(frame_form, text="Cerrar Sesión", font=('Times', 15, BOLD), command=self.CerrarSesion)
        btnCerrarS.place(x=0-1, y=0)

        btnCompras = tk.Button(frame_form, text="Ordenes de compra", font=('Times', 15, BOLD), command=self.OrdenCompra)
        btnCompras.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        btnOrdenes = tk.Button(frame_form, text="Mostrar Ordenes", font=('Times', 15, BOLD), command=self.MostrarOrdenes)
        btnOrdenes.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        btnOrdenes = tk.Button(frame_form, text="Facturas", font=('Times', 15, BOLD), command=self.MostrarFactura)
        btnOrdenes.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.ventana.mainloop()

if __name__ == "__main__":
    app = Menu()
