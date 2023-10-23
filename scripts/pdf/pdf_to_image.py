import os
from pdf2image import convert_from_path


class PDFToImage:
    def __init__(
        self,
        folder_path: str,
        pdf_file: int,
        output_folder: str,
        output_pattern: str,
        output_ext: str,
        first_index: int,
    ) -> None:
        self.folder_path = folder_path
        self.pdf_file = pdf_file
        self.output_folder = output_folder
        self.output_pattern = output_pattern
        self.output_ext = output_ext
        self.first_index = first_index

    def convert(self):
        file_path = os.path.join(self.folder_path, self.pdf_file)
        pdf_images = convert_from_path(file_path)

        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        for idx in range(len(pdf_images)):
            fname = "{}{}.{}".format(
                self.output_pattern,
                idx + self.first_index,
                self.output_ext.lower(),
            )
            pdf_images[idx].save(
                os.path.join(self.output_folder, fname),
                self.output_ext.upper(),
            )

        print("Successfully converted PDF to images")
        return len(pdf_images)


if __name__ == "__main__":
    for i in range(26):
        PDFToImage(
            folder_path=os.path.join(os.getcwd(), "new"),
            pdf_file=f"{i}.pdf",
            output_folder=os.path.join(
                os.getcwd(),
                "conversion",
            ),
            output_pattern="pdf_page_",
            output_ext="png",
            first_index=i + 1,
        ).convert()
