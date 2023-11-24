import os
import math
from PIL import Image


class ResizeImage:
    def __init__(
        self,
        folder_path: str,
        files_num: int,
        files_pattern: str,
        files_ext: str,
        first_index: int,
        scale: float,
        output_folder: str,
        output_pattern: str,
    ) -> None:
        self.folder_path = folder_path
        self.files_num = files_num
        self.files_pattern = files_pattern
        self.files_ext = files_ext
        self.first_index = first_index
        self.scale = scale
        self.output_folder = output_folder
        self.output_pattern = output_pattern

    def resize(self):
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
            x, y = foo.size
            x2 = math.floor(x * self.scale / 10)
            y2 = math.floor(y * self.scale / 10)
            foo = foo.resize((x2, y2))
            foo.save(
                os.path.join(
                    self.output_folder,
                    "{}{}.{}".format(
                        self.output_pattern,
                        idx + 1,
                        self.files_ext,
                    ),
                ),
                quality=95,
            )

        print("Successfully resized images")


if __name__ == "__main__":
    ResizeImage(
        folder_path=os.path.join(
            os.getcwd(),
            "rotate",
        ),
        files_num=26,
        files_pattern="image_",
        files_ext="png",
        first_index=1,
        scale=6,
        output_folder=os.path.join(
            os.getcwd(),
            "resize",
        ),
        output_pattern="resize_image_",
    ).resize()
