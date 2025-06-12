import customtkinter as ctk

class TrianguloPotenciasSim:
    def __init__(self, parent):
        ctk.CTkLabel(
            parent, 
            text="Simulador de Triángulo de Potencias",
            font=ctk.CTkFont(size=20)
        ).pack(pady=20)
        
        # Aquí agregarás sliders, inputs, gráficos, etc.
