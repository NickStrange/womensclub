from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, Paragraph

from src.avery_label import AveryLabel


def sticky_label(canvas, width, height):
        para1Style = ParagraphStyle('para1d')
        para2Style = ParagraphStyle('para2d')
        para1Style.fontSize = 10
        para2Style.fontSize = 10
      #  para1Style.spaceAfter = 0
        para1Style.textColor = colors.HexColor('#003363')
        text1 = "Proceeds go towards the programs of the Cary Woman's Club."
        para1 = Paragraph(text1, para1Style)
        text2 = "www.carywomansclub.org<br />We thank you for your purchase."
        para2 = Paragraph(text2, para2Style)
        table = Table(
            [
             [para1],
             [para2]],
            colWidths=width,
            rowHeights=[2*height/3, 1*height/3])
        table.wrapOn(canvas,0,0)
        table.drawOn(canvas, 0, 0)

if __name__ == '__main__':
   label = AveryLabel(5160)
   label.open( "../data/womensclub_purchase.pdf" )
   label.render( sticky_label, 30)
   label.close()