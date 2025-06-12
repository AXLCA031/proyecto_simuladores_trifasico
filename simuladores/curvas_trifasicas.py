import customtkinter as ctk

class CurvasTrifasicasSim:
    def __init__(self, parent):
        ctk.CTkLabel(
            parent,
            text="Simulador de Ondas Trifásicas",
            font=ctk.CTkFont(size=20)
        ).pack(pady=20)
