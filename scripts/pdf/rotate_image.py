import os
from PIL import Image


class RotateImage:
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

    def rotate(self, angle: float):
        if not os.path.isdir(self.output_folder):
            os.mkdir(self.output_folder)

        for idx in range(self.files_num):
            fname = "{}{}.{}".format(
                self.files_pattern,
                idx + self.first_index,
                self.files_ext,
            )
            file_path = os.path.join(
                self.folder_path,
                fname,
            )
            foo = Image.open(file_path)
            if angle in [90, 180, 270]:
                if angle == 90:
                    foo = foo.transpose(Image.ROTATE_90)
                elif angle == 180:
                    foo = foo.transpose(Image.ROTATE_180)
                else:
                    foo = foo.transpose(Image.ROTATE_270)
            else:
                foo = foo.rotate(angle)
            foo.save(
                os.path.join(
                    self.output_folder,
                    "{}{}.{}".format(
                        self.output_pattern,
                        idx + self.first_index,
                        self.files_ext,
                    ),
                ),
                quality=95,
            )

        print("Successfully rotated images")


if __name__ == "__main__":
    RotateImage(
        folder_path=os.path.join(
            os.getcwd(),
            "conversion",
        ),
        files_num=26,
        files_pattern="pdf_page_",
        files_ext="png",
        first_index=1,
        output_folder=os.path.join(
            os.getcwd(),
            "rotate",
        ),
        output_pattern="image_",
    ).rotate(270)
