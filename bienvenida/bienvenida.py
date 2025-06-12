import customtkinter as ctk
from PIL import Image
import os

class PantallaBienvenida(ctk.CTkFrame):
    def __init__(self, master, callback_triangulo, callback_fasores, callback_ondas, callback_fp, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Tarjeta 1 - Triángulo de Potencias
        self.card1 = self.crear_tarjeta(
            "Triángulo de Potencias",
            "Visualiza las relaciones entre potencia activa, reactiva y aparente.",
            "assets/trianguloPotencias.jpg", (200, 110),
            callback_triangulo
        )
        self.card1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Tarjeta 2 - Fasores Animados
        self.card2 = self.crear_tarjeta(
            "Fasores Animados",
            "Observa cómo los vectores de voltaje y corriente giran en el plano complejo.",
            "assets/fasoresAnimados.jpg", (160, 170),
            callback_fasores
        )
        self.card2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Tarjeta 3 - Ondas Trifásicas
        self.card3 = self.crear_tarjeta(
            "Ondas Trifásicas",
            "Simulación de señales sinusoidales desfasadas entre fases.",
            "assets/ondasTrifasicas.png", (200, 150),
            callback_ondas
        )
        self.card3.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Tarjeta 4 - Corrección de FP
        self.card4 = self.crear_tarjeta(
            "Corrección del FP",
            "Explora cómo el uso de capacitores mejora el factor de potencia.",
            "assets/correccionFactorPotencia.png", (180, 110),
            callback_fp
        )
        self.card4.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    def crear_tarjeta(self, titulo, descripcion, ruta_imagen, size, comando):
        frame = ctk.CTkFrame(self, corner_radius=15)

        if os.path.exists(ruta_imagen):
            imagen = ctk.CTkImage(light_image=Image.open(ruta_imagen), size=size)
            ctk.CTkLabel(frame, image=imagen, text="").pack(pady=(10, 5))

        ctk.CTkLabel(frame, text=titulo, font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 5))
        ctk.CTkLabel(frame, text=descripcion, wraplength=240, justify="center").pack(pady=(0, 10))
        ctk.CTkButton(frame, text="Abrir", command=comando).pack(pady=(0, 10))

        return frame
