from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

def table_table(width:float, height:float):
    linecount = 11
    widths=[width*0.1, width*0.3, width*0.3, width*0.25]
    times=['8-10', '8-10', '10-12', '10-12', '12-2', '12-2', '2-4', '2-4']
    matrix = [['Time', 'Name', 'email', 'phone']]
    for i in range(len(times)):
        matrix += ([[times[i], '', '', '',]
                    ])

    times=['08-10', '08-10', '10-12', '10-12', '12-02', '12-02', '02-04', '02-04']

    table_body = Table(
        matrix
    , colWidths=widths, rowHeights=height/linecount)

    table_body.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'black'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTSIZE', (0, 0), (-1, -1), 18),
    ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold'),

    ('BACKGROUND', (0, 0), (3, 0), colors.blue),
    ('TEXTCOLOR', (0, 0), (3, 0), colors.white),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.antiquewhite, colors.beige])
    ])

    return table_body

def title(width:float, height: float, fair_date:str, location:str):
    heights=[height*0.0, height*0.3, height*0.3, height*0.3, height*0.1]

    text1 = "VOLUNTEERS NEEDED TO RUN THE FAIR"

    title_table = Table([
        [''],
        [text1],
        [fair_date],
        [location],
        ['']
    ], colWidths=width, rowHeights=heights)

    title_table.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 28),
        ('FONT', (0, 0), (-1, -1),  'Helvetica-Bold')
    ])

    return title_table


def page(fair_date:str, location:str):
    width, height = A4
    heights=[height*0.2, height*0.8]

    main_table = Table([
        [title(width, heights[0], fair_date, location)],
        [table_table(width, heights[1])]
    ], colWidths=width, rowHeights=heights)

    main_table.setStyle([
      #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
         ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)


if __name__ == '__main__':
    pdf = canvas.Canvas("../data/christmas_signup.pdf", pagesize=A4)

    page('NOVEMBER 2ND', 'ST ANDREWS CARY')
    pdf.showPage()
    page('NOVEMBER 23RD', 'GLENAIRE')
    pdf.showPage()
    pdf.save()
