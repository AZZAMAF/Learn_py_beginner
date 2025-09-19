# GUI > Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
window = tk.Tk()

#Init
window.configure()
window.geometry("500x200")
window.resizable(False,False)
window.title('Halo aja')

#Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Frame input
input_frame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# Komponen
# 1.Label untuk Nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10, fill='x', expand=True)
# 2. entry Name

nama_depan_label = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_label.pack(padx=10,fill='x', expand=True)

# 3.Label untuk Nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang:")
nama_belakang_label.pack(padx=10, fill='x', expand=True)
# 4. entry Name
nama_belakang_label = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_label.pack(padx=10,fill='x', expand=True)

# 5. TOMBOL
def tombol_click():
    # di panggil tombol 
    pesan = f" Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Gangentggg"
    showinfo(title="wahtsup",message=pesan)

tombol_sapa = ttk.Button(input_frame,text="sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

#Main Loop Window
window.mainloop()
