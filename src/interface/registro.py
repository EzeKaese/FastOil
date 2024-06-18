import customtkinter as ctk

def open_registro():
    registro_app = ctk.CTk()
    registro_app.title('Modulo Estadistica')
    registro_app.wm_attributes('-fullscreen', True)
    registro_app.resizable(width=False, height=False)
    # ... Agrega contenido a la nueva ventana ...

    registro_app.mainloop()