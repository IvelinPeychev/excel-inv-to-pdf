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
    pdf.cell(w=50, h=8, txt=f'{filename.title()}')
    # with open(filepath, 'r') as file:
    #     info = file.readlines()
    #     pdf.page()

# Produce the PDF document
pdf.output('Text_Files/Test.pdf')
