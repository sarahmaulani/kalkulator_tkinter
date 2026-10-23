import tkinter as tk
from tkinter import ttk

# Fungsi untuk menjumlahkan angka
def hitung_penjumlahan():
    try:
        angka_pertama = float(entry_angka_pertama.get())
        angka_kedua = float(entry_angka_kedua.get())

        total = angka_pertama + angka_kedua
        
        if total.is_integer():
            total = int(total)
            
        label_hasil.config(text=f"Hasil: {total}")
    except ValueError:
        label_hasil.config(text="Harus berupa angka!")


root = tk.Tk()
root.title("Kalkulator")
root.geometry("300x250") 

entry_angka_pertama = ttk.Entry(root, justify="center")
entry_angka_pertama.pack(pady=10)

label_tambah = ttk.Label(root, text="+", font=("Arial", 12))
label_tambah.pack(pady=5)

entry_angka_kedua = ttk.Entry(root, justify="center")
entry_angka_kedua.pack(pady=10)

btn_hitung = ttk.Button(root, text="Hitung", command=hitung_penjumlahan)
btn_hitung.pack(pady=15)

label_hasil = tk.Label(root, text="Hasil: ", bg="#d4edda", fg="#155724", width=20, height=2)
label_hasil.pack(pady=10)

root.mainloop()
