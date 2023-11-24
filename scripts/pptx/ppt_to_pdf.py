import os
import re
from spire.presentation import FileFormat, Presentation


class PPTXToPDF:
    def __init__(self, folder_path) -> None:
        self.folder_path = folder_path

    def convert(self):
        for path in os.listdir(self.folder_path):
            if os.path.isfile(
                os.path.join(
                    self.folder_path,
                    path,
                )
            ) and re.search("\\.pptx$", path):
                pptx_file = self.folder_path + "/" + path

                # Create a Presentation object
                presentation = Presentation()

                # # Load a PowerPoint presentation in PPTX format
                presentation.LoadFromFile(pptx_file)

                # # Convert the presentation to PDF format
                pdf_file = pptx_file.replace(".pptx", ".pdf")
                presentation.SaveToFile(pdf_file, FileFormat.PDF)
                presentation.Dispose()


if __name__ == "__main__":
    PPTXToPDF("C:\\Users\\lcyc2\\dev\\python\\scripts\\pptx").convert()
