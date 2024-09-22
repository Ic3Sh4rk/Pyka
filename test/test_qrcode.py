# Ce code a été créé par Ic3Sh4rk | This code was created by Ic3Sh4rk

import qrcode
import tkinter as tk
from PIL import ImageTk, Image

"""
class QrCodeViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.qrcode = tk.PhotoImage(file="QRCode.bmp")
        self.pack()
"""
palette_color = ["#9A0E75", "#830E3B", "#0F0B21", "#3571D9", "#54AEED", "#69DBFC", "#FEFEFE"]

qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=5
)

qr.add_data("https://goo.gl/maps/67rarF4mbKLEB3d87")
qr.make(fit=True)
img = qr.make_image()
img.save('QRCode.bmp')
print("Le QR code vient d'être générer")


app = tk.Tk()
app.title("QrCode Viewer")
app.geometry("472x472")
app.minsize(354, 354)

qrcode = ImageTk.PhotoImage(Image.open("QRCode.bmp"))

frame = tk.Frame(app, bg=palette_color[2])
frame.pack(expand=False, fill="both")
size = [frame.winfo_width(), frame.winfo_height()]

canvas = tk.Canvas(frame, bg=palette_color[1], confine=False)
canvas.create_image(0, 0, anchor=tk.NW, image=qrcode)
# canvas.itemconfigure()
canvas.pack(fill='both', expand=True)


app.mainloop()
