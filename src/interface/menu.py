import customtkinter
import customtkinter as ctk
import os
from PIL import Image
from customtkinter import CTkFont
from registro import open_registro
from about import open_about
from productos import open_productos
from estadistica import open_estadistica

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


# Initialize the main window, main menu
def create_main_window():
    app = ctk.CTk()
    app.title('FastOil Car Service Registration')
    app.geometry('800x600')
    app.resizable(width=False, height=False)

    # image menu logo fastoilMenu
    image_path = os.path.join(os.path.dirname(__file__), 'img/logo.png')
    image = customtkinter.CTkImage(dark_image=Image.open(image_path), size=(780, 125))
    image_label = customtkinter.CTkLabel(app, image=image, text='')
    image_label.place(x=10, y=25)

    # add other images
    image2_path = os.path.join(os.path.dirname(__file__))
    imgregistro = customtkinter.CTkImage(Image.open(image2_path +
                                                    "/img/registro.png"), size=(200, 170))
    imgproducto = customtkinter.CTkImage(Image.open(image2_path +
                                                    "/img/producto.png"), size=(200, 170))
    imgestadistica = customtkinter.CTkImage(Image.open(image2_path +
                                                       "/img/estadistica.png"), size=(180, 200))

    # Frame registro vehicular
    frame = customtkinter.CTkFrame(master=app, corner_radius=20, width=765, height=430)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    frame.place(x=15, y=160)

    # Clases de Fonts
    # Font for First title widgets
    font_wp: CTkFont = customtkinter.CTkFont(family="AriaL",
                                             size=24,
                                             weight="bold",
                                             )
    # Botones para el frame
    btn_registro = customtkinter.CTkButton(command=open_registro,
                                           master=frame,
                                           text="REGISTRO\nVEHICULAR",
                                           corner_radius=20,
                                           width=230,
                                           height=246,
                                           font=font_wp,
                                           border_spacing=5,
                                           anchor="n",
                                           image=imgregistro,
                                           compound="bottom",
                                           )
    btn_registro.pack(padx=20, pady=20)
    btn_registro.place(x=10, y=15)

    btn_productos = customtkinter.CTkButton(command=open_productos,
                                            master=frame,
                                            text="AÑADIR\nPRODUCTOS",
                                            corner_radius=20,
                                            width=230,
                                            height=246,
                                            font=font_wp,
                                            border_spacing=5,
                                            anchor="n",
                                            image=imgproducto,
                                            compound="bottom",
                                            )

    btn_productos.pack(padx=20, pady=20)
    btn_productos.place(x=265, y=15)

    btn_estadistica = customtkinter.CTkButton(command=open_estadistica,
                                              master=frame,
                                              text="ESTADISTICAS",
                                              corner_radius=20,
                                              width=230,
                                              height=246,
                                              font=font_wp,
                                              border_spacing=5,
                                              anchor="n",
                                              image=imgestadistica,
                                              compound="bottom",
                                              )

    btn_estadistica.pack(padx=20, pady=20)
    btn_estadistica.place(x=520, y=15)

    btn_recordatorio = customtkinter.CTkButton(master=frame,
                                               text="RECORDATORIO\nCLIENTES",
                                               corner_radius=20,
                                               width=230,
                                               height=80,
                                               font=font_wp,
                                               border_spacing=5,
                                               anchor="center",
                                               )

    btn_recordatorio.pack(padx=20, pady=20)
    btn_recordatorio.place(x=10, y=300)

    btn_config = customtkinter.CTkButton(master=frame,
                                         text="CONFIGURACION",
                                         corner_radius=20,
                                         width=230,
                                         height=80,
                                         font=font_wp,
                                         border_spacing=5,
                                         anchor="center",
                                         )

    btn_config.pack(padx=20, pady=20)
    btn_config.place(x=265, y=300)

    btn_tutorial = customtkinter.CTkButton(master=frame,
                                           text="TUTORIAL",
                                           corner_radius=20,
                                           width=115,
                                           height=50,
                                           font=font_wp,
                                           border_spacing=5,
                                           anchor="center",
                                           )

    btn_tutorial.pack(padx=20, pady=20)
    btn_tutorial.place(x=560, y=280)

    btn_catalogo = customtkinter.CTkButton(master=frame,
                                           text="CATALOGO",
                                           corner_radius=20,
                                           width=115,
                                           height=50,
                                           font=font_wp,
                                           border_spacing=5,
                                           anchor="center",
                                           )

    btn_catalogo.pack(padx=20, pady=20)
    btn_catalogo.place(x=552.5, y=340)

    btn_info = customtkinter.CTkButton(command=open_about,
                                       master=frame,
                                       text="i",
                                       corner_radius=50,
                                       width=20,
                                       height=20,
                                       font=("NSimSun", 20),
                                       border_spacing=5,
                                       anchor="center",
                                       )

    btn_info.pack(padx=20, pady=20)
    btn_info.place(x=725, y=390)

    # Run the application

    app.mainloop()
