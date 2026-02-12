#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, additional_info):
    """Creates a PDF report with the provided info"""
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    
    report_title = Paragraph(title, styles['h1'])
    # info_list is the variable you'll send from your other script
    report_info = Paragraph(additional_info, styles['BodyText'])
    
    report.build([report_title, report_info])