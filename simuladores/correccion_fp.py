import customtkinter as ctk

class CorreccionFPSim:
    def __init__(self, parent):
        ctk.CTkLabel(
            parent,
            text="Simulador de Corrección del Factor de Potencia",
            font=ctk.CTkFont(size=20)
        ).pack(pady=20)
