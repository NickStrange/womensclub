from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def frontLabel(width, height):
    tmargin=5
    lmargin=10
    widths=[lmargin, width-2*lmargin, lmargin]
    heights = [tmargin, height - 2 * tmargin, tmargin]
    image_pathr = '../data/wc.jpeg'
    img = Image(image_pathr, heights[1], height=height, kind='proportional')

    frontTable = Table(
        [['', '', ''],
         ['', img, ''],
         ['', '', '']],
       colWidths=widths,
       rowHeights=heights)

    frontTable.setStyle([
        #    ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    return frontTable


def backLabel(width, height):
    tmargin=5
    lmargin=10
    widths=[lmargin, width-2*lmargin, lmargin]
    heights = [tmargin,
               (height - 2 * tmargin)*0.75,
               (height - 2 * tmargin)*0.25,
               tmargin]

    para1Style = ParagraphStyle('para1d', leading=20)
    para2Style = ParagraphStyle('para2d', leading=20)
    para1Style.fontSize = 18
    para2Style.fontSize = 12
    para1Style.spaceAfter = 0
    para1Style.textColor = colors.HexColor('#003363')
    text1 = "This item is handmade and local.<br /> Proceeds go towards the programs of the Cary Woman's Club."
    para1 = Paragraph(text1, para1Style)
    text2 = "www.carywomansclub.org<br />We thank you for your purchase."
    para2 = Paragraph(text2, para2Style)
    backTable = Table(
        [['', '', ''],
         ['', para1, ''],
         ['', para2, ''],
         ['', '', '']],
       colWidths=widths,
       rowHeights=heights)

    backTable.setStyle([
    #    ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    return backTable


def front_page():
    width, height = A4
    linecount=5
    matrix = []
    lwidth=width/2
    lheight=height/linecount
    for i in range(linecount):
        matrix+=([[frontLabel(lwidth, lheight),
                   frontLabel(lwidth, lheight)]])

    mainTable = Table(
        matrix
    , colWidths=lwidth,
       rowHeights=lheight)

    mainTable.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)


def back_page():
    width, height = A4
    linecount = 5
    matrix = []
    lwidth = width / 2
    lheight = height / linecount
    for i in range(linecount):
        matrix += ([[backLabel(lwidth, lheight),
                     backLabel(lwidth, lheight)]])

    mainTable = Table(
        matrix
        , colWidths=lwidth,
        rowHeights=lheight)

    mainTable.setStyle([
              ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])


    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)
    return mainTable

if __name__ == '__main__':
    pdf = canvas.Canvas("../data/christmas.pdf", pagesize=A4)

    front_page()
    pdf.showPage()
    back_page()
    pdf.showPage()
    pdf.save()