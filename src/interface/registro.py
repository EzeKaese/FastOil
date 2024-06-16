import customtkinter as ctk

def open_registro():
    registro_app = ctk.CTk()
    registro_app.title('Registro Cambio de Aceite')
    registro_app.geometry('800x600')
    registro_app.resizable(width=False, height=False)
    # ... Agrega contenido a la nueva ventana ...

    registro_app.mainloop()