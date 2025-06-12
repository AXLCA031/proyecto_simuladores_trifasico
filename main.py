import customtkinter as ctk
from simuladores.triangulo_potencias import TrianguloPotenciasSim
from simuladores.fasores import FasoresSim
from simuladores.curvas_trifasicas import CurvasTrifasicasSim
from simuladores.correccion_fp import CorreccionFPSim

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulador de Potencia Trifásica")
        self.geometry("1000x700")
        ctk.set_appearance_mode("light")

        # Layout general
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Panel lateral
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.label_sidebar = ctk.CTkLabel(
            self.sidebar, text="SIMULADORES",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.label_sidebar.pack(pady=(20, 20))

        # Botones
        self.btn_triangulo = ctk.CTkButton(
            self.sidebar, text="Triángulo de Potencias",
            command=self.mostrar_triangulo, height=60,
            font=ctk.CTkFont(size=16)
        )
        self.btn_triangulo.pack(pady=10, padx=20, fill="x")

        self.btn_fasores = ctk.CTkButton(
            self.sidebar, text="Fasores Animados",
            command=self.mostrar_fasores, height=60,
            font=ctk.CTkFont(size=16)
        )
        self.btn_fasores.pack(pady=10, padx=20, fill="x")

        self.btn_ondas = ctk.CTkButton(
            self.sidebar, text="Ondas Trifásicas",
            command=self.mostrar_ondas, height=60,
            font=ctk.CTkFont(size=16)
        )
        self.btn_ondas.pack(pady=10, padx=20, fill="x")

        self.btn_fp = ctk.CTkButton(
            self.sidebar, text="Corrección de FP",
            command=self.mostrar_fp, height=60,
            font=ctk.CTkFont(size=16)
        )
        self.btn_fp.pack(pady=10, padx=20, fill="x")

        # Área principal
        self.main_content = ctk.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.mostrar_triangulo()

    def limpiar_contenido(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

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

app = App()
app.mainloop()
