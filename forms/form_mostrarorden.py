import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from util.bdo import conexion

class MostrarOrdenes:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Mostrar Ordenes')
        self.ventana.geometry('1280x720')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 1280, 720)
        # Crear la tabla
        self.crear_tabla()

        # Botón de menú
        btnMenu = tk.Button(self.ventana, text="Menú", font=('Times', 15, BOLD), command=self.abrir_menu)
        btnMenu.pack(pady=10)

        # Botón para ver detalles
        btnDetalles = tk.Button(self.ventana, text="Ver Detalles", font=('Times', 15, BOLD), command=self.ver_detalles)
        btnDetalles.pack(pady=10)

        self.ventana.mainloop()

    def abrir_menu(self):
        from forms.form_menu import Menu
        self.ventana.destroy()
        Menu()

    def crear_tabla(self):
        frame_tabla = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_tabla.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # Configuración de la tabla
        columns = ["ID_ORDEN", "Nombre Cliente", "Dirección", "Producto", "Precio", "Fecha de Compra", "Estado Factura", "Estado Despacho"]
        self.tree = ttk.Treeview(frame_tabla, columns=columns, show="headings", selectmode="browse")

        # Configuración de las columnas
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Llena la tabla con los datos del procedimiento
        self.llenar_tabla()

        # Enlaza la selección de la tabla a la función de manejo de eventos
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        # Empaqueta la tabla en el frame
        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

    def llenar_tabla(self):
        try:
            # Utiliza la conexión ya disponible en util.bdo
            with conexion.cursor() as cursor:
                # Ejecuta tu procedimiento almacenado aquí
                cursor.execute("EXEC sp_MostrarOrdenesCompra")

                # Obtiene los resultados
                resultados = cursor.fetchall()

                # Llena la tabla con los resultados
                for row in resultados:
                    # Ajusta el orden de los valores según la secuencia de columnas esperada
                    self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")

    def seleccionar_fila(self, event):
        # Obtiene la fila seleccionada
        selected_item = self.tree.selection()[0]
        # Puedes acceder a los valores de la fila seleccionada usando item
        values = self.tree.item(selected_item, "values")
        print("Fila seleccionada:", values)

    def ver_detalles(self):
        # Implementa la lógica para abrir la nueva ventana con los detalles de la fila seleccionada
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Selecciona una fila antes de ver detalles.")
            return

        # Obtiene el ID_ORDEN de la fila seleccionada
        id_orden = self.tree.item(selected_item, "values")[0]

        # Llama al procedimiento almacenado para obtener los detalles
        detalles = self.obtener_detalles_orden(id_orden)

        if detalles:
            detalles_ventana = tk.Toplevel(self.ventana)
            detalles_ventana.title("Detalles de la Factura")

            etiquetas = ["ID_ORDEN:", "Nombre Cliente:", "Dirección:", "Producto:", "Precio:", "Fecha de Compra:", "Estado Factura:", "Estado Despacho:", "IVA:", "TOTAL CON IVA"]
            valores = [str(detalles["ID_ORDEN"]), detalles["Nombre Cliente"], detalles["Direccion"], detalles["Producto"],
                        f"${detalles['Precio']:.2f}", str(detalles["FechaCompra"]), detalles["EstadoFactura"], detalles["EstadoDespacho"],
                        f"${detalles['IVA']:.2f}", f"${detalles['Total con IVA']:.2f}" if 'Total con IVA' in detalles else "N/A"]


            for etiqueta, valor in zip(etiquetas, valores):
                tk.Label(detalles_ventana, text=etiqueta, font=('Times', 12, BOLD)).pack(anchor='w')
                tk.Label(detalles_ventana, text=valor, font=('Times', 12)).pack(anchor='w')

        # Agrega el botón para omitir la factura
        btnOmitirFactura = tk.Button(detalles_ventana, text="Emitir Factura", command=lambda: self.omitir_factura(id_orden, detalles, detalles_ventana))
        btnOmitirFactura.pack(pady=10)


       

    def obtener_detalles_orden(self, id_orden):
        try:
            # Utiliza la conexión ya disponible en util.bdo
            with conexion.cursor() as cursor:
                # Llama al procedimiento almacenado para obtener detalles
                cursor.execute("EXEC sp_MostrarOrdenesCompraDetalles @ID_ORDEN = ?", (id_orden,))
                
                # Obtén el primer conjunto de resultados
                detalles = cursor.fetchone()

                # Si hay al menos un conjunto de resultados
                if detalles:
                    # Devuelve un diccionario con los detalles
                    detalles_dict = {
                        "ID_ORDEN": detalles[0],
                        "Nombre Cliente": detalles[1],
                        "Direccion": detalles[2],
                        "Producto": detalles[3],
                        "Precio": detalles[4],
                        "FechaCompra": detalles[5],
                        "EstadoFactura": detalles[6],
                        "EstadoDespacho": detalles[7],
                        "IVA": detalles[8],
                        "Total con IVA": detalles[9] if len(detalles) > 9 else None
                    }
                    return detalles_dict
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron detalles para la orden seleccionada.")
                    return None

        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")
            return None

    def omitir_factura(self, id_orden, detalles, detalles_ventana):
        try:
            with conexion.cursor() as cursor:
                # Ejemplo de actualización, ajusta según tu esquema de base de datos
                cursor.execute("UPDATE dbo.ordenCompra SET factura = 'Facturado' WHERE ID_ORDEN = ?", (id_orden,))
                conexion.commit()

               
                # Inserta los detalles en la tabla
                self.insertar_en_tabla(detalles)

                messagebox.showinfo("Información", "La factura ha sido omitida y los detalles se han guardado en la base de datos.")

                # Cierra la ventana de detalles
                detalles_ventana.destroy()

                # Programa la recarga de la tabla después de un cierto tiempo (por ejemplo, 500 ms)
                self.ventana.after(500, self.recargar_tabla)
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar el estado de la factura: {e}")


    def insertar_en_tabla(self, detalles):
        try:
            with conexion.cursor() as cursor:
                # Llama al procedimiento almacenado para insertar detalles en la tabla
                cursor.execute("EXEC sp_InsertarDetallesFactura @ID_ORDEN = ?, @NombreCliente = ?, @Direccion = ?, @Producto = ?, @Precio = ?, @FechaCompra = ?, @EstadoFactura = ?, @EstadoDespacho = ?, @IVA = ?, @TotalConIVA = ?",
                            (detalles["ID_ORDEN"], detalles["Nombre Cliente"], detalles["Direccion"], detalles["Producto"],
                                detalles["Precio"], detalles["FechaCompra"], detalles["EstadoFactura"], detalles["EstadoDespacho"],
                                detalles["IVA"], detalles["Total con IVA"] if 'Total con IVA' in detalles else None))
            conexion.commit()
            messagebox.showinfo("Información", "Detalles insertados en la tabla correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al insertar detalles en la tabla: {e}")            

    def recargar_tabla(self):
        # Limpia la tabla actual
        for item in self.tree.get_children():
            self.tree.delete(item)


        # Vuelve a llenar la tabla con los datos actualizados
        self.llenar_tabla()

if __name__ == "__main__":
    app = MostrarOrdenes()
