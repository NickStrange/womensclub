from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

def table_table(width:float, height:float):
    linecount = 30
    widths=[width*0.3, width*0.4, width*0.25]
    matrix = [['Name', 'email', 'phone']]
    for i in range(linecount-2):
        matrix += ([['', '', '',]
                    ])
    table_body = Table(
        matrix
    , colWidths=widths, rowHeights=height/linecount)

    table_body.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'black'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
  #  ('FONTSIZE', (0, 0), (0, -1), 18),
    ('FONTSIZE', (0, 0), (1, -1), 12),
    ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold'),

    ('BACKGROUND', (0, 0), (3, 0), colors.blue),
    ('TEXTCOLOR', (0, 0), (3, 0), colors.white),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.antiquewhite, colors.beige])
    ])

    return table_body


def page():
    width, height = A4
    heights=[height*0.05, height*0.05, height*0.9]

    main_table = Table([
            ['CLUB HISTORY BUFF?'],
            ['Help organize, digitize and save our history.'],
            [table_table(width, heights[2])]
    ], colWidths=width, rowHeights=heights)

    main_table.setStyle([
     #    ('GRID', (0, 0), (-1, -1), 1, 'red'),
     #    ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
    #     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

    ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
    ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),
    ('VALIGN', (1, 0), (-1, -1), 'MIDDLE'),
    ('FONTSIZE', (0, 0), (-1, -1), 27),
    ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ])

    main_table.wrapOn(pdf, 0, 0)
    main_table.drawOn(pdf, 0, 0)


if __name__ == '__main__':
    pdf = canvas.Canvas("../data/volunteer_signup.pdf", pagesize=A4)

    page()
    pdf.showPage()
    pdf.save()