#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, data):
    """Creates a PDF report with a styled table in blue and white"""
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    # Report Title with spacing
    report_title = Paragraph(title, styles['h1'])
    elements.append(report_title)
    elements.append(Spacer(1, 12)) # 12pt space below title

    # Create Table object
    # data should be a list of lists: [['Header1', 'Header2'], ['Val1', 'Val2']]
    table = Table(data, hAlign='LEFT')

    # Professional Style (Blue & White)
    style = TableStyle([
        # Header: Dark Blue background, White text
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E5A88')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        
        # Body: White background, Black text
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        
        # Grid lines (Subtle light grey)
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    
    table.setStyle(style)
    elements.append(table)
    
    # Build PDF file
    report.build(elements)