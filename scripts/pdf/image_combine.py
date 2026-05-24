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


class ImageCombine:
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

    def combine(self):
        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        for idx in range(self.files_num):
            if idx == self.files_num - 1:
                break
            if idx == 0:
                fname_1 = "{}{}.{}".format(
                    self.files_pattern,
                    self.first_index + idx,
                    self.files_ext.lower(),
                )
                file_index = f"a_{idx + 1}"
            else:
                fname_1 = "{}{}.{}".format(
                    self.files_pattern,
                    file_index,
                    self.files_ext.lower(),
                )
                file_index = f"a_{idx + 1}"
            image_1 = Image.open(os.path.join(self.folder_path, fname_1))

            fname_2 = "{}{}.{}".format(
                self.files_pattern,
                self.first_index + idx + 1,
                self.files_ext.lower(),
            )
            image_2 = Image.open(os.path.join(self.folder_path, fname_2))

            max_width = max(image_1.width, image_2.width)
            combined_height = image_1.height + image_2.height

            # Create a new blank image
            combined_image = Image.new("RGB", (max_width, combined_height))

            # Paste the images onto the new canvas
            combined_image.paste(image_1, (0, 0))
            combined_image.paste(image_2, (0, image_1.height))
            combined_image.save(
                os.path.join(
                    self.output_folder,
                    "{}{}.png".format(
                        self.output_pattern,
                        file_index,
                    ),
                )
            )

    print("Successfully combined images into a single file.")


if __name__ == "__main__":
    ImageCombine(
        folder_path=os.path.join(
            os.getcwd(),
            "combine",
        ),
        first_index=first_index,
        files_pattern="pdf_page_",
        files_num=5,
        files_ext=image_ext,
        output_folder=os.path.join(
            os.getcwd(),
            "combine",
        ),
        output_pattern="pdf_page_",
    ).combine()
