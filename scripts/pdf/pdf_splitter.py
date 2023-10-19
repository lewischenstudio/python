import os
from PyPDF2 import PdfReader, PdfWriter


class PDFSplitter:
    def __init__(
        self,
        folder_path: str,
        pdf_file: int,
        output_folder: str,
        output_pattern: str,
        first_index: int,
    ) -> None:
        self.folder_path = folder_path
        self.pdf_file = pdf_file
        self.output_folder = output_folder
        self.output_pattern = output_pattern
        self.first_index = first_index

    def split(self):
        file_path = os.path.join(self.folder_path, self.pdf_file)
        pdf = PdfReader(file_path)

        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        for page in range(len(pdf.pages)):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf.pages[page])

            output_filename = os.path.join(
                self.output_folder,
                "{}{}.pdf".format(
                    self.output_pattern,
                    page + 1,
                ),
            )

            with open(output_filename, "wb") as out:
                pdf_writer.write(out)

        print("Successfully splitted PDF")


if __name__ == "__main__":
    PDFSplitter(
        folder_path=os.path.join(
            os.getcwd(),
            "my_folder",
        ),
        pdf_file="my_file.pdf",
        output_folder=os.path.join(
            os.getcwd(),
            "my_folder",
        ),
        output_pattern="new_pdf_",
        first_index=1,
    )
