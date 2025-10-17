import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup

def scarica_notizie():
    url = "https://www.ansa.it/sito/notizie/topnews/topnews.shtml"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titoli = soup.find_all('h3', class_='news-title')

            output_area.delete('1.0', tk.END)  

            if titoli:
                for i, titolo in enumerate(titoli[:100], start=1):
                    output_area.insert(tk.END, f"{i}. {titolo.get_text(strip=True)}\n\n")
            else:
                output_area.insert(tk.END, "Nessun titolo trovato.")
        else:
            messagebox.showerror("Errore", f"Errore HTTP: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore:\n{str(e)}")

# Interfaccia Grafica
finestra = tk.Tk()
finestra.title("Notizie ANSA")
finestra.geometry("600x500")
finestra.resizable(False, False)

titolo = tk.Label(finestra, text="Ultime Notizie ANSA", font=("Helvetica", 16, "bold"), fg="#4CAF50")
titolo.pack(pady=10)

btn = tk.Button(finestra, text="Visualizza Notizie", command=scarica_notizie, bg="#4CAF50", fg="white", font=("Helvetica", 12))
btn.pack(pady=10)

output_area = scrolledtext.ScrolledText(finestra, wrap=tk.WORD, width=70, height=20, font=("Helvetica", 10))
output_area.pack(padx=10, pady=10)

finestra.mainloop()
