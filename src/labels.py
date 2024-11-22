from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def label(width, height, line1, line2, line3, line4, line5, line6):
    tmargin=25
    margin=75
    lmargin= 30
    widths=[lmargin,margin, width-2*(lmargin + margin), margin]
    heights = [height*0.0, height*0.2, height*0.075, height*0.075, height*0.075, height*0.075, height*0.1]
    image_path = '../data/wc-1.jpeg'
    img = Image(image_path, width=heights[1], height=heights[1], kind='proportional')

    frontTable = Table(
        [['','','',''],
         ['',img, line1, ''],
         ['','', line2, ''],
         ['','', line3, ''],
         ['', '', line4, ''],
         ['', '', line5, ''],
         ['', '', line6, '']],
       colWidths=widths,
       rowHeights=heights)

    frontTable.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'blue'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 1), (-1, 1), 'red'),
        ('FONTSIZE', (0, 1), (-1, 1), 30),
        ('TEXTCOLOR', (0, 2), (-1, -1), 'green'),
        ('FONTSIZE', (0, 2), (-1, -1), 20),
    ])
    return frontTable


def front_page(line1, line2, line3, line4=None, line5=None, line6=None):
    width, height = A4
    linecount=1
    heights = [height*0.4, height*0.6]
    lwidth=width
    lheight=height

    mainTable = Table(
        [[label(lwidth, heights[1], line1, line2, line3, line4, line5, line6)],
         ['']]
    , colWidths=lwidth,
       rowHeights=heights)

    mainTable.setStyle([
     #   ('GRID', (0, 0), (-1, -1), 1, 'red'),
    ])
    mainTable.wrapOn(pdf,0,0)
    mainTable.drawOn(pdf, 0, 0)




if __name__ == '__main__':
    pdf = canvas.Canvas("../data/fair.pdf", pagesize=A4)

    front_page(line1="Unique Carolina\n\n\nPhotographic cards",
                      line2="$5 per Card",
                      line3='')
    pdf.showPage()
   # pdf.save()

    front_page(line1="Hand Painted\n\n\nCards",
                      line2="$1 per card",
                      line3='')
    pdf.showPage()

    front_page(line1="Rock Painting\n\n\nKits",
                      line2="$15 Each",
                      line3='')
    pdf.showPage()

    front_page(line1="Ornaments",
               line2="Shell Santa $3",
               line3='Copper North Carolina $3',
               line4='Crystal Snowflakes, Small $11, Medium $12, Large $13',
               line5='',
               line6='')
    pdf.showPage()

    front_page(line1="Body\n\n\nProducts",
                      line2="Soaps $8",
                      line3='Body Butter $9')
    pdf.showPage()
    pdf.save()
