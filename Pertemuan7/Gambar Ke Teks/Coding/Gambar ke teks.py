import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pytesseract import pytesseract

class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Mengekstrak Gambar ke Teks")

        # Jalur Tesseract
        self.path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Jalur ke foto
        self.path_to_image = None

        # untuk mengarahkan tesseract_cmd ke tesseract
        pytesseract.tesseract_cmd = self.path_to_tesseract

        # Membuat UI element
        self.create_widgets()

    def create_widgets(self):
        # Judul
        judul_label = tk.Label(self.root, text="Aplikasi Menjadikan Gambar Ke Teks")
        judul_label.grid(row=0, column=0, padx=10, pady=10)

        # membuat button memilih file
        memilih_file_button = tk.Button(self.root, text="Pilih Gambar", command=self.choose_image)
        memilih_file_button.grid(row=1, column=0, padx=10, pady=10)

        try:
            if self.path_to_image:
                # memmbuka image dengan PIL
                img = Image.open(self.path_to_image)

                # Ekstrak foto ke teks
                text = pytesseract.image_to_string(img)

                # menampilkan gambar
                img.thumbnail((300, 300))
                img_tk = ImageTk.PhotoImage(img)
                image_label = tk.Label(self.root, image=img_tk)
                image_label.image = img_tk
                image_label.grid(row=2, column=0, padx=10, pady=10)

                # menampilkan teks yang telah di ekstrak
                text_label = tk.Label(self.root, text=f"Extracted Text:\n{text}")
                text_label.grid(row=3, column=0, padx=10, pady=10)

        except FileNotFoundError:
            error_label = tk.Label(self.root, text=f"File not found: {self.path_to_image}")
            error_label.grid(row=2, column=0, padx=10, pady=10)
        except Exception as e:
            error_label = tk.Label(self.root, text=f"Error: {str(e)}")
            error_label.grid(row=2, column=0, padx=10, pady=10)

    def choose_image(self):
        self.path_to_image = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
