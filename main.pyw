import tkinter as ttk


# APP
root = ttk.Tk()


# CONFIGS APP
root.title("Disc-Libs")
root.resizable(False, False)
root.iconbitmap('discs.ico')
root.geometry("900x600")
root.config(
            bg="#0f0f0f"
        )


# FRAME LIST
frameList = ttk.Frame()
frameList.pack(
        side="left",
        anchor="n", # (N=norte ; S=sur, E=este; O=oeste)
        padx="20",
        pady="20"
    )


# FRAME LIST CONFIGS
frameList.config(
        bg="#1a1a1a",
        width="860",
        height="400",
    )


# LOOP
root.mainloop()