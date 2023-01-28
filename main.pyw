import tkinter as ttk


# CONSTANTS
DARK = "#0f0f0f"
LIGHT_DARK = "#1a1a1a"

# APP
root = ttk.Tk()


# CONFIGS APP
root.title("Disc-Libs")
root.resizable(False, False)
root.iconbitmap('discs.ico')
root.geometry("900x600")
root.config(
            bg=DARK
        )


# FRAME LIST
frameList = ttk.Frame(root)
frameList.pack(
        side="left",
        anchor="n", # (N=norte ; S=sur, E=este; O=oeste)
        padx="20",
        pady="20"
    )


# FRAME LIST CONFIGS
frameList.config(
        bg=LIGHT_DARK,
        width="860",
        height="400",
    )

# LABEL TITLE
labelTitle = ttk.Label(frameList, text="Disc List", fg="white", font=("Terminal", 18), bg=LIGHT_DARK)
labelTitle.place(x=400, y=0)

# LOOP
root.mainloop()