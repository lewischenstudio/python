# PDF Reducer

Occassionally we may want to reduce the size of a PDF file for meeting certain
requirements. Although the image or file quality will be lowered, it should be
acceptable by users as long as it is within the readable limit. This directory
consists of a series of methods to reduce the size of a large PDF file.

- [PDFToImage](/scripts/pdf/pdf_to_image.py)
- [ResizeImage](/scripts/pdf/resize_image.py)
- [ImageToPDF](/scripts/pdf/image_to_pdf.py)
- [PDFMerger](/scripts/pdf/pdf_merger.py)
- [RotateImage](/scripts/pdf/rotate_image.py) (optional)
- [PDFSplitter](/scripts/pdf/pdf_splitter.py) (optional)

The main method is [ResizePDF](/scripts/pdf/resize_pdf.py), which accepts a PDF
file and the value for scaling down and returns a PDF file of smaller size.
