import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import qrcode
from PIL import Image, ImageTk

class GeradorQRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QR Code")

        self.label = tk.Label(root, text="Digite o texto ou URL:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.label_modos = tk.Label(root, text="Selecione o modo de codificação:")
        self.label_modos.pack()

        self.modo_codificacao = tk.StringVar()
        self.modo_codificacao.set("Byte")
        self.combobox_modos = ttk.Combobox(root, textvariable=self.modo_codificacao, values=["Byte", "Numeric", "Alphanumeric", "Kanji"])
        self.combobox_modos.pack()

        self.label_tamanho = tk.Label(root, text="Tamanho do QR Code (em pixels):")
        self.label_tamanho.pack()

        self.tamanho_entry = tk.Entry(root)
        self.tamanho_entry.insert(tk.END, "300")
        self.tamanho_entry.pack()

        self.label_borda = tk.Label(root, text="Borda do QR Code (em módulos):")
        self.label_borda.pack()

        self.borda_entry = tk.Entry(root)
        self.borda_entry.insert(tk.END, "4")
        self.borda_entry.pack()

        self.label_qualidade = tk.Label(root, text="Qualidade da imagem (de 1 a 10):")
        self.label_qualidade.pack()

        self.qualidade_entry = tk.Entry(root)
        self.qualidade_entry.insert(tk.END, "8")
        self.qualidade_entry.pack()

        self.button_gerar_previa = tk.Button(root, text="Visualizar Prévia", command=self.visualizar_previa)
        self.button_gerar_previa.pack()

        self.canvas_previa = tk.Canvas(root, width=300, height=300)
        self.canvas_previa.pack()

        self.canvas_previa.create_text(150, 150, text="Prévia do QR Code aparecerá aqui.", fill="gray")

        self.button_gerar = tk.Button(root, text="Gerar QR Code", command=self.gerar_qr_code)
        self.button_gerar.pack()

        self.button_limpar = tk.Button(root, text="Limpar", command=self.limpar_campos)
        self.button_limpar.pack()

        self.button_salvar = tk.Button(root, text="Salvar QR Code", command=self.salvar_qr_code)
        self.button_salvar.pack()

        self.qr_image = None

    def visualizar_previa(self):
        data = self.entry.get()
        if data:
            try:
                tamanho = int(self.tamanho_entry.get())
                borda = int(self.borda_entry.get())
                qualidade = int(self.qualidade_entry.get())

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                img = img.resize((tamanho, tamanho))
                self.qr_image = ImageTk.PhotoImage(img)

                self.canvas_previa.delete("all")
                self.canvas_previa.create_image(150, 150, image=self.qr_image)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao gerar a prévia do QR Code: {e}")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira algum texto ou URL.")

    def gerar_qr_code(self):
        data = self.entry.get()
        if data:
            try:
                tamanho = int(self.tamanho_entry.get())
                borda = int(self.borda_entry.get())
                qualidade = int(self.qualidade_entry.get())
                modo_codificacao = self.modo_codificacao.get()

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)

                if modo_codificacao == "Numeric":
                    mode = 'numeric'
                elif modo_codificacao == "Alphanumeric":
                    mode = 'alphanumeric'
                elif modo_codificacao == "Kanji":
                    mode = 'kanji'
                else:
                    mode = 'byte'

                img = qr.make_image(fill_color="black", back_color="white", mode=mode)

                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
                if file_path:
                    img = img.resize((tamanho, tamanho))
                    img.save(file_path, quality=qualidade)

                    messagebox.showinfo("Salvar", "QR Code salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o QR Code: {e}")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira algum texto ou URL.")

    def limpar_campos(self):
        self.entry.delete(0, tk.END)
        self.canvas_previa.delete("all")
        self.qr_image = None

    def salvar_qr_code(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorQRApp(root)
    root.mainloop()
