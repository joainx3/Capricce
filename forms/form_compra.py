import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from util.bdo import conexion


class OrdenCompras():
    def verificar(self):
        id_cliente = self.combobox1.get()
        id_producto = self.combobox2.get()
        with conexion.cursor() as cursor:
            # Ajusta el nombre del procedimiento almacenado y la cantidad de parámetros según tu caso
            consulta = 'EXEC sp_InsertarOrdenes ?, ?;'
            cursor.execute(consulta, (id_producto[1], id_cliente[1]))
            
            # La mayoría de los procedimientos almacenados no devuelven filas, 
            # pero puedes verificar si hay algún resultado utilizando 'OUT' parameters 
            # o revisando si hay filas afectadas en el cursor.
            filas_afectadas = cursor.rowcount

        if filas_afectadas > 0:
            messagebox.showinfo(message="Se ha creado la orden de compra correctamente", title="Correcto")
        else:
            messagebox.showerror(message="Error al crear la orden de compra", title="Fallo")

    def __init__(self):        
        #Configuración inicial
        self.ventana = tk.Tk()                             
        self.ventana.title('Ordenes de Compra')
        self.ventana.geometry('1280x720')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,1280,720)

        # Botón de menú
        btnMenu = tk.Button(self.ventana, text="Menú", font=('Times', 15, BOLD), command=self.abrir_menu)
        btnMenu.pack()
        btnMenu.place(x=0-1,y=0)
        
         #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de Ordenes de compras",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top
        
       

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        
        
        with conexion.cursor() as cursor:
            consulta =('select id_cliente,nom_cliente,apellido_p from cliente')
            cursor.execute(consulta)
            opcion = cursor.fetchall()
        id_cliente_label = tk.Label(frame_form_fill,text="Seleccion cliente")
        self.combobox1 = ttk.Combobox(frame_form_fill,values=opcion,height = 50,width=60)
        id_cliente_label.pack()
        self.combobox1.pack()


        with conexion.cursor() as cursor:
            consulta2 =('select id_producto,nom_producto,precio from producto')
            cursor.execute(consulta2)
            opcion2 = cursor.fetchall()
        id_producto_label = tk.Label(frame_form_fill,text="Seleccion Producto")
        self.combobox2 = ttk.Combobox(frame_form_fill,values=opcion2,height = 50,width=60)        
        id_producto_label.pack()
        self.combobox2.pack()
        
                 

        inicio = tk.Button(frame_form_fill,text="Registrar",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)   
        inicio.bind("<Return>", (lambda event: self.verificar()))


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


