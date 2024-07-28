import tkinter as tk
from PIL import ImageTk, Image

def show_imge(path):
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()
    
show_imge('Screenshot 2024-07-28 152536.png')