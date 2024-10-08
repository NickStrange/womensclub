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

    tmargin=5
    lmargin=10
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
    heights = [tmargin, height - 2 * tmargin, tmargin]

    para1Style = ParagraphStyle('para1d')
    para1Style.fontSize = 15
    para1Style.spaceAfter = 0
    para1Style.textColor = colors.HexColor('#003363')
    text = "This item is handmade and local. Proceeds go towards the programs of the Cary Woman's Club."
    para = Paragraph(text, para1Style)
    frontTable = Table(
        [['', '', ''],
         ['', para, ''],
         ['', '', '']],
       colWidths=widths,
       rowHeights=heights)

    frontTable.setStyle([
  #      ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    return frontTable

def front_page():
    width, height = A4
    linecount=10
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
        ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)

def back_page():
    width, height = A4
    linecount = 10
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
        #      ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])


    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)
    return mainTable

pdf = canvas.Canvas("../data/christmas.pdf", pagesize=A4)

front_page()
pdf.showPage()
back_page()
pdf.showPage()
pdf.save()