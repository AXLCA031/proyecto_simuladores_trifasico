import customtkinter as ctk
import os
from PIL import Image

from simuladores.triangulo_potencias import TrianguloPotenciasSim
from simuladores.fasores import FasoresSim
from simuladores.curvas_trifasicas import CurvasTrifasicasSim
from simuladores.correccion_fp import CorreccionFPSim
from bienvenida.bienvenida import PantallaBienvenida
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulador de Potencia Trifásica")
        self.geometry("1000x700")
        ctk.set_appearance_mode("light")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        ruta_logo = os.path.join("assets", "logotecsup.png")
        ancho = 200
        relacion_aspecto = 877 / 3331
        alto = int(ancho * relacion_aspecto)

        imagen_logo = ctk.CTkImage(light_image=Image.open(ruta_logo), size=(ancho, alto))
        logo_label = ctk.CTkLabel(self.sidebar, image=imagen_logo, text="")
        logo_label.pack(pady=(20, 5))

        label_simuladores = ctk.CTkLabel(
            self.sidebar,
            text="SIMULADORES",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        label_simuladores.pack(pady=(0, 20))

        btn_inicio = ctk.CTkButton(
            self.sidebar,
            text="Pantalla Principal",
            command=self.mostrar_bienvenida,
            height=50,
            font=ctk.CTkFont(size=16)
        )
        btn_inicio.pack(pady=10, padx=20, fill="x")

        def cambiar_tema():
            actual = ctk.get_appearance_mode()
            ctk.set_appearance_mode("dark" if actual == "Light" else "light")

        switch_tema = ctk.CTkSwitch(
            self.sidebar,
            text="Modo Oscuro",
            command=cambiar_tema
        )
        switch_tema.pack(pady=10)

        def mostrar_ayuda():
            ventana = ctk.CTkToplevel(self)
            ventana.title("Ayuda")
            ventana.geometry("400x300")
            ventana.attributes("-topmost", True)
            ventana.focus_force()

            ctk.CTkLabel(
                ventana,
                text="Selecciona un simulador desde la pantalla principal.\n\n"
                     "Cada uno ofrece una visualización diferente\n"
                     "de conceptos de potencia trifásica.",
                justify="center",
                font=ctk.CTkFont(size=14)
            ).pack(expand=True, pady=40, padx=20)

        btn_ayuda = ctk.CTkButton(self.sidebar, text="Ayuda", command=mostrar_ayuda)
        btn_ayuda.pack(pady=10, padx=20, fill="x")

        info_label = ctk.CTkLabel(
            self.sidebar,
            text="Proyecto Tecsup 2025\nPotencia Trifásica",
            justify="center",
            font=ctk.CTkFont(size=13),
            text_color="gray"
        )
        info_label.pack(side="bottom", pady=20)

        self.main_content = ctk.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.mostrar_bienvenida()

    def limpiar_contenido(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def mostrar_bienvenida(self):
        self.limpiar_contenido()
        bienvenida = PantallaBienvenida(
            self.main_content,
            self.mostrar_triangulo,
            self.mostrar_fasores,
            self.mostrar_ondas,
            self.mostrar_fp
        )
        bienvenida.pack(expand=True, fill="both")

    def mostrar_triangulo(self):
        self.limpiar_contenido()
        TrianguloPotenciasSim(self.main_content)

    def mostrar_fasores(self):
        self.limpiar_contenido()
        FasoresSim(self.main_content)

    def mostrar_ondas(self):
        self.limpiar_contenido()
        CurvasTrifasicasSim(self.main_content)

    def mostrar_fp(self):
        self.limpiar_contenido()
        CorreccionFPSim(self.main_content)

if __name__ == "__main__":
    app = App()
    app.mainloop()
