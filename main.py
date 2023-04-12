import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem

    # one way
    # invoice_nr = filename.split('-')[0]
    # date = filename.split('-')[1]

    # as we have a two items in filename, Python assigned it directly
    invoice_nr, date = filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{invoice_nr}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    # ln is giving a new line for the cell
    pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    # data frame
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # Extracting the columns titles from the Excel file

    # Add a header

    # without list comprehension

    # columns = list(df.columns)
    # pdf.set_font(family='Times', size=10)
    # pdf.set_text_color(80, 80, 80)
    # pdf.cell(w=30, h=8, txt=columns[0].replace("_", " "), border=1)
    # pdf.cell(w=70, h=8, txt=columns[1].replace("_", " "), border=1)
    # pdf.cell(w=30, h=8, txt=columns[2].replace("_", " "), border=1)
    # pdf.cell(w=30, h=8, txt=columns[3].replace("_", " "), border=1)
    # # we give new line to the last cell "ln=1" so the table be displayed correctly
    # pdf.cell(w=30, h=8, txt=columns[4].replace("_", " "), border=1, ln=1)


    # with list comprehension

    columns = [item.replace("_", " ").capitalize() for item in list(df.columns)]
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    # we give new line to the last cell "ln=1" so the table be displayed correctly
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        # we give new line to the last cell "ln=1" so the table be displayed correctly
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    total_sum = df['total_price'].sum()
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=70, h=8, txt='', border=1)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    # we give new line to the last cell "ln=1" so the table be displayed correctly
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add a total sum sentence
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=30, h=8, txt=f'The total price is {total_sum}', ln=1)


    # Add a company name and logo
    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=25, h=8, txt='Pythonhow')
    pdf.image('pythonhow.png', w=10)




    pdf.output(f'PDFs/{filename}.pdf')

