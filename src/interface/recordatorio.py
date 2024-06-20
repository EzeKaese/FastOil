import customtkinter
import customtkinter as ctk


def open_about():
    config_app = ctk.CTk()
    config_app.title('Configuracion')
    config_app.geometry('800x600')
    config_app.resizable(width=False, height=False)
    # ... Agrega contenido a la nueva ventana ...
    config_app.mainloop()
