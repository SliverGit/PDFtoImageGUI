PDFtoImageGUI.py

Requires "pdf2image" - pip3 install pdf2image

Tested with Version 1.17.0

pdf2image currently uses poppler-24.08.0 and when installing pdf2image that should download automatically too, when pdf2image is updated to the newer version of poppler line 66 is relevant to that version and would need to be updated, also maybe broken then.

poppler can be found at "https://poppler.freedesktop.org/" - line 66 is relevant to current poppler version for pdf2image and works with poppler-24.08.0, other versions have not been tested.

Requires "tkinter" - pip3 install tkinter

Additional "img2pdf" - pip3 install img2pdf

PDFtoImageGUI.py is a batch PDF to Image (PNG) Graphical User Interface based on the existing package pdf2image.

Simply put, navigate to PDF folder then navigate to desired output folder and click "Start Conversion" to extract.

![PDFtoImageGUI](https://github.com/user-attachments/assets/dc9440d6-04bd-47ef-9ae3-23b84925393b)

Furthermore, to convert to pdf from images with img2pdf "pip3 install img2pdf"
command: img2pdf image1.png image2.png image3.png -o images.pdf
