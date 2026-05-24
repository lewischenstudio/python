import io
import os
import math
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# 1. Create a new PDF with ReportLab containing the text

# Set font and size (e.g., Helvetica, 14 points)
# can.setFont("Helvetica", 14)
# can.drawString(1*inch, 10*inch, "Hello, World! (14pt)")

# # Set a different font and size (e.g., Times-Roman, 24 points)
# can.setFont("Times-Roman", 24)
# can.drawString(1*inch, 9*inch, "Larger Text (24pt)")

# # Set another font and size (e.g., Courier, 10 points)
# can.setFont("Courier", 10)
# can.drawString(1*inch, 8*inch, "Smaller Text (10pt)")

# Move to the beginning of the BytesIO buffer


sign_data = {
    "text": "Text",
    "left": 82.625,
    "top": 29.925003051757812,
    "width": 134,
    "height": 22,
    "leftRatio": 0.15531015037593984,
    "topRatio": 0.043495643970578216,
    "widthRatio": 0.2518796992481203,
    "heightRatio": 0.03197674418604651,
}

sign_list = [
    {
        "text": "Text",
        "left": 82.625,
        "top": 29.925003051757812,
        "width": 134,
        "height": 22,
        "leftRatio": 0.15531015037593984,
        "topRatio": 0.043495643970578216,
        "widthRatio": 0.2518796992481203,
        "heightRatio": 0.03197674418604651,
    },
    {
        "text": "Text",
        "left": 82.625,
        "top": 29.925003051757812,
        "width": 134,
        "height": 22,
        "leftRatio": 0.15531015037593984,
        "topRatio": 0.143495643970578216,
        "widthRatio": 0.2518796992481203,
        "heightRatio": 0.03197674418604651,
    },
]

file_path = os.path.join(os.getcwd(), "original.pdf")
existing_pdf = PdfReader(open(file_path, "rb"))
page = existing_pdf.pages[0]
page_width = page.mediabox.width
page_height = page.mediabox.height
print(f"Width: {page_width}, Height: {page_height}")

# text_width = page_width * sign_data.get("widthRatio")
signature = "Hello from Python Hello"

for item in sign_list:
    print("item: ", item)
    text_width = page_width * item.get("widthRatio")
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=[page_width, page_height])
    font_size = math.floor(11 - len(signature) * 11 / text_width)
    left = page_width * item.get("leftRatio")
    top = (
        page_height * (1 - item.get("topRatio")) - item.get("height") - (font_size / 2)
    )
    can.setFont("Helvetica", font_size)
    can.drawString(left, top, signature, charSpace=0)
    can.save()
    packet.seek(0)
    new_pdf_overlay = PdfReader(packet)
    page.merge_page(new_pdf_overlay.pages[0])
    output = PdfWriter()
    output.add_page(page)
# 4. Write the result to a new file
file_path = os.path.join(os.getcwd(), "new_original.pdf")
with open(file_path, "wb") as output_stream:
    output.write(output_stream)
