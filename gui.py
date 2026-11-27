import tkinter as tk
from tkinter import ttk, messagebox

from botwlibs.paths import UPDATE
from botwlibs.modbuilder import create_mod_folder
from botwlibs.weapons import Weapon
from botwlibs.weapon_fields import load_fields


def list_weapons():
    folder = UPDATE / "Actor" / "Pack"
    return sorted(p.stem for p in folder.glob("Weapon_*.sbactorpack"))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BOTW Mod Creator")
        self.geometry("900x520")

        self.all_weapons = list_weapons()
        self.fields = load_fields()
        self.weapon = None
        self.entries = {}

        self._build_left()
        self._build_right()
        self._build_bottom()


    def _build_left(self):
        left = ttk.Frame(self, padding=10)
        left.grid(row=0, column=0, sticky="ns")
        ttk.Label(left, text="Weapons").pack(anchor="w")

        self.search = tk.StringVar()
        self.search.trace_add("write", lambda *args: self._filter())
        ttk.Entry(left, textvariable=self.search).pack(fill="x")

        frame = ttk.Frame(left)
        frame.pack(fill="both", expand=True, pady=5)

        self.listbox = tk.Listbox(frame, 
                                  width=30, 
                                  height=20, 
                                  exportselection=False)
        
        scroll = ttk.Scrollbar(frame, command=self.listbox.yview)

        self.listbox.config(yscrollcommand=scroll.set)

        self.listbox.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.listbox.bind("<<ListboxSelect>>", self._on_select)
        self._filter()

    def _filter(self):
        text = self.search.get().lower()
        self.listbox.delete(0, "end")

        for name in self.all_weapons:
            if text in name.lower():
                self.listbox.insert("end", name)

    # --- right : wepons ---
    def _build_right(self):

        self.columnconfigure(1, weight= 1)
        
        right = ttk.Frame(self, padding= 10)
        right.grid(row= 0, column= 1, sticky="nsew")

        

        for i, f in enumerate(self.fields, start=1):
            ttk.Label(right, text=f["label"]).grid(row=2 * i - 1, column=0, sticky="w")
            if f["type"] == "bool":
                var = tk.StringVar(value="False")
                ttk.Combobox(right, textvariable=var, values=["True", "False"], state="readonly", width=10).grid(
                    row=2*i-1,
                    column=1,
                    sticky="w",
                    padx=8
                )
            else:
                var = tk.StringVar()
                ttk.Entry(right, textvariable = var, width = 12).grid(
                    row=2*i-1, 
                    column=1, 
                    sticky="w", 
                    padx=8
                )

            ttk.Label(right, text=f["description"], foreground="gray", wraplength=450
                ).grid(row = 2 * i, 
                    column = 0, 
                    columnspan = 2, 
                    sticky ="w", 
                    pady=(0, 6)
                )

            self.entries[f["id"]] = var

    # --- Bootom: name of mod + button ---
    def _build_bottom(self):
        bottom = ttk.Frame(self, padding=10)

        bottom.grid(row=1, 
                    column=0, 
                    columnspan=2, 
                    sticky="ew")

        ttk.Label(bottom, text="Name of the mod:").pack(side="left")

        self.mod_name = tk.StringVar(value="MyMod")

        ttk.Entry(bottom, textvariable=self.mod_name, width=24).pack(side="left", padx=6)

        ttk.Button(bottom, text="Genereted the mod", command=self.generate).pack(
            side="left", padx=6
        )
        self.status = ttk.Label(bottom, text="")
        self.status.pack(side="left", padx=10)

    # --- actions ---
    def _on_select(self, event):
        selection = self.listbox.curselection()

        if not selection:
            return
        
        name = self.listbox.get(selection[0])

        try:
            self.weapon = Weapon(name)
        except Exception as e:
            messagebox.showerror("Error", f"Impossiblity to open {name} :\n{e}")
            return

        self.title_label.config(text=name)

        for f in self.fields:
            try:
                value = self.weapon.get(f["id"])
            except Exception:
                value = ""  # don't exist for a weapon

            self.entries[f["id"]].set(str(value))

        self.status.config(text="")

    def generate(self):
        if self.weapon is None:
            messagebox.showinfo("Info", "Choose a weapon")
            return
        try:
            for f in self.fields:
                text = self.entries[f["id"]].get().strip()
                if text == "":
                    continue
                try:
                    current = str(self.weapon.get(f["id"]))
                except Exception:
                    continue
                if text == current:
                    continue  # don't touch what we have do


                if f["type"] == "int":
                    value = int(text)
                elif f["type"] == "bool":
                    bool(text)
                else:
                    float(text)
                    
                self.weapon.set(f["id"], value)

            name = self.mod_name.get().strip() or "MyMod"
            mod_dir = create_mod_folder(name, "Mod created with BOTW Mod Creator")
            out = self.weapon.save(mod_dir)

        except ValueError as e:
            messagebox.showerror("Forbbiden value", str(e))
            return
        
        self.status.config(text=f"Writed : {out}")


if __name__ == "__main__":
    App().mainloop()