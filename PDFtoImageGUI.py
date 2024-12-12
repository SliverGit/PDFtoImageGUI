import os
from pdf2image import convert_from_path
from tkinter import Tk, filedialog, messagebox, Button, Label, Entry, Frame, StringVar
from tkinter import ttk

class PDFConverter:
    def __init__(self, root):
        self.root = root
        self.pdf_dir = ""
        self.png_dir = ""
        self.input_var = StringVar()
        self.output_var = StringVar()

        # Create input directory frame
        self.input_frame = Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        Label(self.input_frame, text="Select Input Directory").pack(pady=5)
        Entry(self.input_frame, textvariable=self.input_var, width=50).pack(pady=5)
        Button(self.input_frame, text="Browse", command=self.browse_input_dir).pack(pady=5)

        # Create output directory frame
        self.output_frame = Frame(self.root)
        self.output_frame.pack(padx=10, pady=10)

        Label(self.output_frame, text="Select Output Directory").pack(pady=5)
        Entry(self.output_frame, textvariable=self.output_var, width=50).pack(pady=5)
        Button(self.output_frame, text="Browse", command=self.browse_output_dir).pack(pady=5)

        # Create start button
        self.start_button = Button(self.root, text="Start Conversion", command=self.start_conversion)
        self.start_button.pack(pady=10)

    def browse_input_dir(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.input_var.set(dir_path)

    def browse_output_dir(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.output_var.set(dir_path)

    def start_conversion(self):
        try:
            self.pdf_dir = self.input_var.get()
            self.png_dir = self.output_var.get()

            if not os.path.exists(self.pdf_dir) or not os.path.exists(self.png_dir):
                messagebox.showerror("Error", "Both input and output directories must exist")
                return

            for filename in os.listdir(self.pdf_dir):
                if filename.endswith(".pdf"):
                    pdf_file_path = os.path.join(self.pdf_dir, filename)
                    print(f'Converting {pdf_file_path} to PNG...')
                    self.extract_images_from_pdf(pdf_file_path, self.png_dir)

            print("Conversion Complete.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract_images_from_pdf(self, pdf_file_path, png_dir):
        try:
            images = convert_from_path(pdf_file_path, poppler_path=r'C:\Program Files\poppler-24.08.0\Library\bin')

            for i, img in enumerate(images):
                filename = os.path.splitext(os.path.basename(pdf_file_path))[0]
                img.save(f'{png_dir}/{filename}+{i}.png')
        except Exception as e:
            print(f"Error converting {pdf_file_path}: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = PDFConverter(root)
    root.title("PDF to PNG Converter")
    root.geometry("400x300")
    root.mainloop()
