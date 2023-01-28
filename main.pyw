import tkinter as ttk


# CONSTANTS
FONT = "Terminal"
DARK = "#0f0f0f"
LIGHT_DARK = "#1a1a1a"


# APP
root = ttk.Tk()
root.title("Disc-Libs")
root.resizable(False, False)
root.iconbitmap('discs.ico')
root.geometry("900x600")
root.config(
    bg=DARK
)


# FRAME SEARCH
frameSearch = ttk.Frame(
    root
)
frameSearch.place(x=20, y=20)
frameSearch.config(
    bg=LIGHT_DARK,
    width=860,
    height=80
)


# FRAME LIST
frameList = ttk.Frame(
    root
)
frameList.place(x=20, y=120)
frameList.config(
    bg=LIGHT_DARK,
    width=860,
    height=380,
)


# FRAME BOTTOM
frameBottom = ttk.Frame(
    root
)
frameBottom.place(x=20, y=520)
frameBottom.config(
    bg=LIGHT_DARK,
    width=860,
    height=60,
)


## SEARCH SPACE
# Label Title
labelTitle = ttk.Label(
    frameSearch,
    text="Disc List",
    fg="white",
    font=(FONT, 18),
    bg=LIGHT_DARK,
    pady=8
)
labelTitle.place(x=400, y=0)


# Entry Search
entrySearch = ttk.Entry(
    frameSearch,
    fg="white",
    font=(FONT, 14),
    bg=DARK,
    width=50
)
entrySearch.place(x=140, y=48)


# Button Search
buttonSearch = ttk.Button(
    frameSearch,
    fg="white",
    font=(FONT, 12),
    bg=DARK,
    width=10,
    text="Search"
)
buttonSearch.place(x=650, y=46)


# LOOP
root.mainloop()