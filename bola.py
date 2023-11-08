import tkinter as tk
import math

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Volume Bola")

def hitung():
    output_hasil_luas.delete(0, tk.END)
    output_hasil_volume.delete(0, tk.END)

    jari_jari = float(entry_jari_jari.get())

    luas_permukaan = 4 * math.pi * jari_jari**2
    volume = (4/3) * math.pi * jari_jari**3

    output_hasil_luas.insert(0, f"Luas Permukaan: {round(luas_permukaan, 2)}")
    output_hasil_volume.insert(0, f"Volume: {round(volume, 2)}")

# Label Nama
label_nama = tk.Label(app, text="Mohammad Agus Salim (220511096)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Jari-jari
label_jari_jari = tk.Label(app, text="Jari-Jari Bola : ")
label_jari_jari.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_jari_jari = tk.Entry(app)
entry_jari_jari.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung_button = tk.Button(app, text="Hitung", command=hitung, pady=3, padx=3)
hitung_button.grid(row=5, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas = tk.Label(app, text="Hasil Luas Permukaan:", height=2)
label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
output_hasil_luas = tk.Entry(app)
output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Hasil Volume:", height=1)
label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)

app.mainloop()
