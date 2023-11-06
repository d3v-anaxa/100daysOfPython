from pypdf import PdfWriter
from os import listdir

merger = PdfWriter()

pdfs = [ f for f in listdir('.') if f.endswith('.pdf')]

for pdf in pdfs:
    merger.append(pdf)

merger.write("default.pdf")
merger.close()
