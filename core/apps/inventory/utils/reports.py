from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from openpyxl import Workbook
from openpyxl.styles import Font


def generate_pdf_report(items):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Items Report", styles['Title']))
    
    data = [['ID', 'Name', 'Quantity', 'Price', 'Created At']]
    for item in items:
        data.append([
            str(item.id),
            item.name,
            str(item.quantity),
            item.price,
            item.created_at.strftime('%Y-%m-%d')
        ])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    return buffer


def generate_excel_report(items):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Items Report"
    
    headers = ['ID', 'Name', 'Quantity', 'Price', 'Created At']
    sheet.append(headers)
    
    for cell in sheet[1]:
        cell.font = Font(bold=True)
    
    for item in items:
        sheet.append([
            item.id,
            item.name,
            item.quantity,
            float(item.price),
            item.created_at.strftime('%Y-%m-%d')
        ])
    
    buffer = BytesIO()
    workbook.save(buffer)
    buffer.seek(0)
    return buffer