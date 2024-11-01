from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.units import inch
import random
import os

# ----- Prepare data -----
def prepare_data():
    data = []

    for _ in range(2):
        count=0
        nums = []
        while count<25:
            new_num = random.randint(1, 100)
            if new_num not in nums:
                nums.append(new_num)
                count+=1
        data.append([nums[i:i+5] for i in range(0, 25, 5)])

    return data

# ----- vertical -----
def vertical_tables(data, filename):
    # Create a PDF file
    pdf = SimpleDocTemplate(filename, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30,bottomMargin=18)

    # Define the table size
    table_width = 4.5 * inch  # Half the page width for each table

    # Create two tables with the same data and style
    table1 = Table(data[0], colWidths=table_width / 5, rowHeights=table_width / 5)
    table2 = Table(data[1], colWidths=table_width / 5, rowHeights=table_width / 5)

    # Style the tables
    table_style = TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 24),  # Set font size to 14 for all cells
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align horizontally all cells
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center align vertically all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Add gridlines
    ])

    table1.setStyle(table_style)
    table2.setStyle(table_style)

    # Add tables and a spacer between them to the elements list
    elements = [table1, Spacer(1, 0.5 * inch), table2]

    # Build the PDF with the tables
    pdf.build(elements)


# ----- horizontal -----
def horizontal_tables(data, filename):
    # Create a PDF file
    pdf = SimpleDocTemplate(filename, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30,bottomMargin=18)
    pdf.pagesize = landscape(letter)

    # Define the table size
    table_width = 4.5 * inch  # Half the page width for each table
    spacer_width = 0.5 * inch

    # Create two tables with the same data and style
    table1 = Table(data[0], colWidths=table_width / 5, rowHeights=table_width / 5)
    table2 = Table(data[1], colWidths=table_width / 5, rowHeights=table_width / 5)

    # Style the tables
    table_style = TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 24),  # Set font size to 14 for all cells
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align horizontally all cells
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center align vertically all cells
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Add gridlines
    ])

    table1.setStyle(table_style)
    table2.setStyle(table_style)

    side_by_side_table = Table([[table1, "", table2]], colWidths=[table_width, spacer_width, table_width])

    # Build the PDF with the tables
    pdf.build([side_by_side_table])

folder = "bingo_file/"
if not os.path.exists(folder):
    os.makedirs(folder)  # This will create all intermediate directories if needed
for i in range(1, 4):
    filename = folder+"bingo_"+str(i)+".pdf"
    data = prepare_data()
    vertical_tables(data, filename)