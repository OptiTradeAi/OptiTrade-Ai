
import tkinter as tk
from tkinter import ttk

class PainelVisual:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("OptiTrade AI - Painel Visual")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e2f")
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#1e1e2f")
        style.configure("TLabel", background="#1e1e2f", foreground="#ffffff", font=("Segoe UI", 10))
        style.configure("TButton", background="#292940", foreground="#ffffff", font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#37375a")])
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.setup_strategy_panel()

    def setup_strategy_panel(self):
        self.strategy_label = ttk.Label(self.main_frame, text="Estratégias Ativas", font=("Segoe UI", 12, "bold"))
        self.strategy_label.pack(anchor="w", pady=(0, 10))

        self.strategy_frame = ttk.Frame(self.main_frame)
        self.strategy_frame.pack(fill="x", pady=10)

        self.super_label = ttk.Label(self.strategy_frame, text="Super Estratégias (>88% Acerto)", font=("Segoe UI", 10, "bold"), foreground="#00ff99")
        self.super_label.grid(row=0, column=0, sticky="w", pady=5)

        self.super_var = tk.BooleanVar(value=True)
        self.super_check = ttk.Checkbutton(self.strategy_frame, variable=self.super_var)
        self.super_check.grid(row=0, column=1, sticky="e")

        self.normal_label = ttk.Label(self.strategy_frame, text="Demais Estratégias", font=("Segoe UI", 10, "bold"))
        self.normal_label.grid(row=1, column=0, sticky="w", pady=5)

        self.normal_var = tk.BooleanVar(value=True)
        self.normal_check = ttk.Checkbutton(self.strategy_frame, variable=self.normal_var)
        self.normal_check.grid(row=1, column=1, sticky="e")

        self.timeframe_label = ttk.Label(self.main_frame, text="Seleção de Timeframe", font=("Segoe UI", 12, "bold"))
        self.timeframe_label.pack(anchor="w", pady=(20, 10))

        self.timeframe_frame = ttk.Frame(self.main_frame)
        self.timeframe_frame.pack(fill="x")

        self.m1_var = tk.BooleanVar(value=True)
        self.m5_var = tk.BooleanVar(value=True)

        self.m1_check = ttk.Checkbutton(self.timeframe_frame, text="M1", variable=self.m1_var)
        self.m1_check.grid(row=0, column=0, padx=5, sticky="w")

        self.m5_check = ttk.Checkbutton(self.timeframe_frame, text="M5", variable=self.m5_var)
        self.m5_check.grid(row=0, column=1, padx=5, sticky="w")
