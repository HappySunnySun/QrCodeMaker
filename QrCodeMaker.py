import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
import webbrowser

def generate_qr():
    url = url_entry.get()
    if url:
        qr_img = qrcode.make(url)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_img.save(file_path)
            result_label.config(text="QR code enregistré avec succès !", fg="green")
        else:
            result_label.config(text="Enregistrement annulé.", fg="red")
    else:
        result_label.config(text="Veuillez entrer une URL valide.", fg="red")

def open_github():
    github_url = "https://github.com/HappySunnySun/QrCodeMaker"
    webbrowser.open(github_url)

root = tk.Tk()
root.configure(bg="white")
root.title("QrCodeMaker")

url_label = tk.Label(root, text="Entrez l'URL:", bg="white", fg="black")
url_entry = tk.Entry(root, width=40, relief=tk.SUNKEN, bd=2, highlightthickness=1, highlightcolor="blue", highlightbackground="gray")

generate_button = tk.Button(root, text="Générer QR Code", command=generate_qr, bg="white", relief=tk.FLAT)
result_label = tk.Label(root, text="", fg="red", bg="white")

github_logo = Image.open(r"D:\Programation\QrCodeMaker\src\github-mark.png")
github_logo = github_logo.resize((30, 30), Image.Resampling.LANCZOS)
github_logo = ImageTk.PhotoImage(github_logo)
generate_button = tk.Button(root, text="Générer QR Code", command=generate_qr)
github_button = tk.Button(root, image=github_logo, command=open_github, relief=tk.FLAT, bd=0, highlightthickness=0, bg="white")
github_button.image = github_logo

url_label.pack(pady=10)
url_entry.pack(pady=10)
generate_button.pack(pady=10)
result_label.pack(pady=10)
github_button.pack(pady=20)

root.resizable(False, False)
root.mainloop()