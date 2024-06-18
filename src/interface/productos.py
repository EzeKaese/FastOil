import customtkinter as ctk

def open_productos():
    productos_app = ctk.CTk()
    productos_app.title('Modulo Productos')
    productos_app.wm_attributes('-fullscreen', True)
    productos_app.resizable(width=False, height=False)
    # ... Agrega contenido a la nueva ventana ...

    productos_app.mainloop()