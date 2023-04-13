# Emre Kin
# <yemrekin4@gmail.com>
# with this project we do 3 process one make super file 1 make dummy and one for watermark
import PyPDF2
import sys
inputs = sys.argv[1:]  # with this we cant take file names in terminal


def pdf_combiner(pdf_list):  # with this we make a super pdf combined
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


with open('dummy.pdf', 'rb') as my_pdf:  # with this we make a new pdf like dummy
    reader = PyPDF2.PdfFileReader(my_pdf)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as pdf:
        writer.write(pdf)
pdf_combiner(inputs)

pdf = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf.getNumPages()):  # with this we materwark wanted pdf
    page = pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    pass

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
