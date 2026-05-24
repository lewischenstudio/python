import os
import shutil
from pdf_to_image import PDFToImage
from resize_image import ResizeImage
from image_to_pdf import ImageToPDF
from pdf_merger import PDFMerger
from variables import (
    image_ext,
    first_index,
    pdf_file_pattern,
    resize_file_pattern,
    new_file_pattern,
    temp_folder,
    images_folder,
    resize_folder,
    pdfs_folder,
)


class ResizePDF:
    def __init__(
        self,
        folder_path: str,
        pdf_file: str,
        scale: float,
        output_path: str,
    ) -> None:
        self.folder_path = folder_path
        self.pdf_file = pdf_file
        self.scale = scale
        self.output_path = output_path

    def resize(self):
        temp_folder_path = os.path.join(os.getcwd(), temp_folder)
        images_folder_path = os.path.join(temp_folder_path, images_folder)
        resize_folder_path = os.path.join(temp_folder_path, resize_folder)
        pdfs_folder_path = os.path.join(temp_folder_path, pdfs_folder)
        save_name = self.pdf_file.replace(".", "_(1).")

        if not os.path.isdir(temp_folder_path):
            os.mkdir(temp_folder_path)

        files_num = PDFToImage(
            folder_path=self.folder_path,
            pdf_file=self.pdf_file,
            output_folder=images_folder_path,
            output_pattern=pdf_file_pattern,
            output_ext=image_ext,
            first_index=first_index,
        ).convert()

        ResizeImage(
            folder_path=images_folder_path,
            files_num=files_num,
            files_pattern=pdf_file_pattern,
            files_ext=image_ext,
            first_index=first_index,
            scale=self.scale,
            output_folder=resize_folder_path,
            output_pattern=resize_file_pattern,
        ).resize()

        ImageToPDF(
            folder_path=resize_folder_path,
            files_num=files_num,
            files_pattern=resize_file_pattern,
            files_ext=image_ext,
            first_index=first_index,
            output_folder=pdfs_folder_path,
            output_pattern="new_pdf_page_",
        ).convert()

        PDFMerger(
            folder_path=pdfs_folder_path,
            files_num=files_num,
            files_pattern=new_file_pattern,
            first_index=first_index,
            output_folder=self.output_path,
            save_name=save_name,
        ).merge()

        shutil.rmtree(temp_folder_path)


if __name__ == "__main__":
    ResizePDF(
        folder_path="",
        pdf_file="",
        scale=4.5,
        output_path="",
    ).resize()
