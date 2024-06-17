import customtkinter
import customtkinter as ctk


def open_about():
    about_app = ctk.CTk()
    about_app.title('About')
    about_app.geometry('500x200')
    about_app.resizable(width=False, height=False)
    # ... Agrega contenido a la nueva ventana ...

    # Frame registro vehicular
    frame = customtkinter.CTkFrame(master=about_app, corner_radius=20, width=470, height=160)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    frame.place(x=15, y=15)

    texto = customtkinter.CTkLabel(about_app,
                                   text="# FastOil "
                                        "\n# Copyright (C) [2024] [Anthony Samplina]"
                                        "\n# Todos los derechos reservados."
                                        "\n# Este software y su documentación son propiedad de [Anthony Samplina]."
                                        "\n# El uso, copia, modificación o distribución de este software y su "
                                        "\ndocumentación por cualquier medio sin el permiso escrito de [Anthony "
                                        "\nSamplina] está estrictamente prohibido.",
                                   text_color="white",
                                   font=("Arial Bold", 12),
                                   justify="center",
                                   fg_color="transparent",
                                   )
    texto.pack(padx=10, pady=10)
    texto.place(x=40, y=40)

    about_app.mainloop()
