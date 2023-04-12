import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of filepaths
filepaths = glob.glob('Text_Files/*.txt')
# Create one PDF file
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Go through each text file
for filepath in filepaths:
    # df = pd.read_csv(filepath)

    # Add page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    filename = Path(filepath).stem

    # Add the name to the PDF
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'{filename.title()}', ln=1)

    # Get the context of each text file
    with open(filepath, 'r') as file:
        info = file.read()

    # Add the text file content to the pdf
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=info)


# Produce the PDF document
pdf.output("output.pdf")
