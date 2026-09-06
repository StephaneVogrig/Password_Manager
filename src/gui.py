
import tkinter as tk
from tkinter import ttk

class TextVar:
    """Permet d'utiliser un tk.Text comme une StringVar (get/set)."""

    def __init__(self, text_widget: tk.Text):
        self.widget = text_widget

    def get(self) -> str:
        return self.widget.get("1.0", "end-1c")

    def set(self, value: str) -> None:
        self.widget.delete("1.0", "end")
        self.widget.insert("1.0", value)

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de mot de passe")
        self.geometry("700x400")
        self.minsize(560, 320)
        self.build_ui()

    def build_ui(self) -> None:
        frame_global = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        frame_global.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        frame_left = ttk.Frame(frame_global, width=220)
        frame_global.add(frame_left, weight=1)

        frame_right = ttk.Frame(frame_global)
        frame_global.add(frame_right, weight=2)

        self.build_frame_left(frame_left)
        self.build_frame_right(frame_right)

    def build_frame_left(self, parent: ttk.Frame) -> None:
        label = ttk.Label(parent, text="Sites enregistrés", font=("", 10 , "bold"))
        label.pack(anchor="w", pady=(0,4))

        list_container = ttk.Frame(parent)
        list_container.pack(fill=tk.BOTH, expand=True)

    def build_frame_right(self, parent: ttk.Frame) -> None:
        # Pour étirer la colonne des Entry
        parent.columnconfigure(1, weight=1)

        label = ttk.Label(parent, text="Détails", font=("", 10 , "bold"))
        label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,10))

        # Champs sur une seule ligne : (nom_de_variable, texte_a_afficher, etat)
        champs = [
            ("name"       , "Nom du site :"   , "normal"  ),
            ("url"        , "URL :"           , "normal"  ),
            ("identifiant", "Identifiant :"   , "normal"  ),
            ("password"   , "Mot de passe :"  , "normal"  ),
            ("email"      , "Email :"         , "normal"  ),
            ("other_data" , "Autres données :", "normal"  ),
            ("created_at" , "Créé le :"       , "readonly"),
            ("updated_at" , "Mis à jour le :" , "readonly"),
        ]

        self.vars = {}

        for row, (var_name, label_text, state_entry) in enumerate(champs, start=1):
            # Création dynamique des variables
            var = tk.StringVar()
            self.vars[var_name] = var

            # Création et placement des noms des champs
            label_name = ttk.Label(parent, text=label_text)
            label_name.grid(row=row, column=0, sticky="w", pady=4)

            # Création et placement des champs
            entry = ttk.Entry(parent, textvariable=var, state=state_entry)
            entry.grid(row=row, column=1, sticky="ew", pady=4)

        row = len(champs) + 1

        # Champ "notes" : multi-ligne, géré à part (pas de StringVar possible avec Text)
        label_notes = ttk.Label(parent, text="Notes :")
        label_notes.grid(row=row, column=0, sticky="nw", pady=4)

        self.notes_text = tk.Text(parent, height=5, wrap="word")
        self.notes_text.grid(row=row, column=1, sticky="nsew", pady=4)

        # Pour que la zone de texte s'étire verticalement si la fenêtre s'agrandit
        parent.rowconfigure(row, weight=1)

        # Ajout au dictionnaire pour utilisation comme les autres variables
        self.vars["notes"] = TextVar(self.notes_text)
