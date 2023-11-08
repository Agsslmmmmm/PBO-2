import tkinter as tk

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Volume Limas Segitiga")

def hitung():
    output_hasil_luas.delete(0, tk.END)
    output_hasil_volume.delete(0, tk.END)

    alas = float(entry_alas.get())
    tinggi_alas = float(entry_tinggi_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    luas_alas = 0.5 * alas * tinggi_alas
    volume = (1/3) * luas_alas * tinggi_limas

    output_hasil_luas.insert(0, f"Luas Alas: {round(luas_alas, 2)}")
    output_hasil_volume.insert(0, f"Volume: {round(volume, 2)}")

# Label Nama
label_nama = tk.Label(app, text="Mohammad Agus Salim (220511096)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Alas Segitiga
label_alas = tk.Label(app, text="Panjang Alas Segitiga : ")
label_alas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_alas = tk.Entry(app)
entry_alas.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Tinggi Alas Segitiga
label_tinggi_alas = tk.Label(app, text="Tinggi Alas Segitiga : ")
label_tinggi_alas.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
entry_tinggi_alas = tk.Entry(app)
entry_tinggi_alas.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Tinggi Limas
label_tinggi_limas = tk.Label(app, text="Tinggi Limas Segitiga : ")
label_tinggi_limas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
entry_tinggi_limas = tk.Entry(app)
entry_tinggi_limas.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung_button = tk.Button(app, text="Hitung", command=hitung, pady=3, padx=3)
hitung_button.grid(row=6, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas = tk.Label(app, text="Hasil Luas Alas:", height=2)
label_hasil_luas.grid(row=7, column=0, padx=5, pady=5)
output_hasil_luas = tk.Entry(app)
output_hasil_luas.grid(row=7, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Hasil Volume:", height=1)
label_hasil_volume.grid(row=8, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=8, column=2, padx=5, pady=5)

app.mainloop()
