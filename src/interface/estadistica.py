import customtkinter as ctk

def open_estadistica():
    estadistica_app = ctk.CTk()
    estadistica_app.title('Modulo Estadistica')
    estadistica_app.resizable(width=False, height=False)
    estadistica_app.wm_attributes('-fullscreen', True)
    # ... Agrega contenido a la nueva ventana ...

    estadistica_app.mainloop()