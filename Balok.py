import tkinter as tk

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Volume Balok")

def hitung():
    output_hasil_luas.delete(0, tk.END)
    output_hasil_volume.delete(0, tk.END)

    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())

    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    volume = panjang * lebar * tinggi

    output_hasil_luas.insert(0, f"Luas Permukaan: {round(luas_permukaan, 2)}")
    output_hasil_volume.insert(0, f"Volume: {round(volume, 2)}")

# Label Nama
label_nama = tk.Label(app, text="Mohammad Agus Salim (220511096)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Panjang
label_panjang = tk.Label(app, text="Panjang Balok : ")
label_panjang.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_panjang = tk.Entry(app)
entry_panjang.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Lebar
label_lebar = tk.Label(app, text="Lebar Balok : ")
label_lebar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
entry_lebar = tk.Entry(app)
entry_lebar.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Tinggi
label_tinggi = tk.Label(app, text="Tinggi Balok : ")
label_tinggi.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
entry_tinggi = tk.Entry(app)
entry_tinggi.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung_button = tk.Button(app, text="Hitung", command=hitung, pady=3, padx=3)
hitung_button.grid(row=6, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas = tk.Label(app, text="Hasil Luas Permukaan:", height=2)
label_hasil_luas.grid(row=7, column=0, padx=5, pady=5)
output_hasil_luas = tk.Entry(app)
output_hasil_luas.grid(row=7, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Hasil Volume:", height=1)
label_hasil_volume.grid(row=8, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=8, column=2, padx=5, pady=5)

app.mainloop()
