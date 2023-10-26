import os
from pypdf import PdfMerger


class PDFMerger:
    def __init__(
        self,
        folder_path: str,
        files_num: int,
        files_pattern: str,
        first_index: int,
        output_folder: str,
        save_name: str,
        reverse_order: bool = False,
    ) -> None:
        self.folder_path = folder_path
        self.files_num = files_num
        self.files_pattern = files_pattern
        self.first_index = first_index
        self.output_folder = output_folder
        self.save_name = save_name
        self.reverse_order = reverse_order

    def merge(self):
        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        pdfs = [
            f"{self.files_pattern}{(i + self.first_index)}.pdf"
            for i in range(self.files_num)
        ]
        if self.reverse_order:
            pdfs.sort(reverse=True)
        print("pdfs: ", pdfs)
        files = [os.path.join(self.folder_path, pdf) for pdf in pdfs]

        merger = PdfMerger()

        for pdf in files:
            merger.append(pdf)

        merger.write(os.path.join(self.output_folder, f"{self.save_name}"))
        merger.close()

        print("Successfully merged PDFs")


if __name__ == "__main__":
    PDFMerger(
        folder_path=os.path.join(
            os.getcwd(),
            "pdfs",
        ),
        files_num=2,
        files_pattern="pdf_page_",
        first_index=1,
        output_folder=os.path.join(
            os.getcwd(),
        ),
        save_name="my_file.pdf",
    ).merge()
