import customtkinter as ctk

class FasoresSim:
    def __init__(self, parent):
        ctk.CTkLabel(
            parent,
            text="Simulador de Fasores Trifásicos",
            font=ctk.CTkFont(size=20)
        ).pack(pady=20)
