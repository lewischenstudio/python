import os
from PIL import Image
from variables import (
    first_index,
    image_ext,
    pdf_file_pattern,
    pdfs_folder,
    resize_file_pattern,
    resize_folder,
)


class ImageToPDF:
    def __init__(
        self,
        folder_path: str,
        files_num: int,
        files_pattern: str,
        files_ext: str,
        first_index: int,
        output_folder: str,
        output_pattern: str,
    ) -> None:
        self.folder_path = folder_path
        self.files_num = files_num
        self.files_pattern = files_pattern
        self.files_ext = files_ext
        self.first_index = first_index
        self.output_folder = output_folder
        self.output_pattern = output_pattern

    def convert(self):
        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        for idx in range(self.files_num):
            fname = "{}{}.{}".format(
                self.files_pattern,
                self.first_index + idx,
                self.files_ext.lower(),
            )
            image_1 = Image.open(os.path.join(self.folder_path, fname))
            im_1 = image_1.convert("RGB")
            im_1.save(
                os.path.join(
                    self.output_folder,
                    "{}{}.pdf".format(
                        self.output_pattern,
                        self.first_index + idx,
                    ),
                )
            )

    print("Successfully converted images to PDFs")


if __name__ == "__main__":
    ImageToPDF(
        folder_path=os.path.join(
            os.getcwd(),
            resize_folder,
        ),
        first_index=first_index,
        files_pattern=resize_file_pattern,
        files_num=26,
        files_ext=image_ext,
        output_folder=os.path.join(
            os.getcwd(),
            pdfs_folder,
        ),
        output_pattern=pdf_file_pattern,
    ).convert()
