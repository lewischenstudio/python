import os
import re
import docx


class PythonDocument:
    def __init__(
        self,
        file_path: str = "",
        file_name: str = "",
        header: str = "",
        input: [] = [],
        delimiter: str = "|",
        file_first: bool = True,
        merge_tables: bool = True,
        output_file: str = "",
    ) -> None:
        self.file_path = file_path
        self.file_name = file_name
        self.header = header
        self.input = input
        self.delimiter = delimiter
        self.file_first = file_first
        self.merge_tables = merge_tables
        self.output_file = output_file

    def add_file(self, doc, table=None):
        if self.file_path != "":
            f = open(os.path.join(self.file_path, self.file_name), "r")
            data = f.readlines()
            first_data = re.split(
                f"[.*\s]({self.delimiter}.*)",
                data[0].replace("\n", ""),
            )
            rows = len(data)
            cols = len(first_data)
            if first_data[-1] == "":
                cols = cols - 1

            if self.file_first or (not self.merge_tables):
                table = doc.add_table(rows=1, cols=cols)

            for idx in range(rows):
                cell = table.add_row().cells

                col = re.split(
                    f"[.*\s]({self.delimiter}.*)", data[idx].replace("\n", "")
                )

                for i in range(cols):
                    cell[i].text = col[i]

        return table

    def add_input(self, doc, table=None):
        if len(self.input) > 0:
            rows = len(self.input)
            cols = len(self.input[0].split(","))

            if (not self.file_first) or (not self.merge_tables):
                table = doc.add_table(rows=1, cols=cols)

            for idx in range(rows):
                cell = table.add_row().cells

                col = self.input[idx].split(",")
                for i in range(cols):
                    cell[i].text = str(col[i])

        return table

    def create(self):
        # Create an instance of a word document
        doc = docx.Document()

        # Add a Title to the document
        doc.add_heading(self.header, 0)

        # Read lines from file
        if self.file_first:
            table = self.add_file(doc)
            self.add_input(doc, table)

            # Now save the document to a location
            return doc.save(os.path.join(self.file_path, self.output_file))

        table = self.add_input(doc, table)
        self.add_file(doc)
        return doc.save(os.path.join(os.getcwd(), self.output_file))


if __name__ == "__main__":
    PythonDocument(
        file_path=os.path.join(os.getcwd()),
        file_name="my_list.txt",
        header="Some Header",
        input=["Hello"],
        delimiter="PS",
        file_first=True,
        merge_tables=True,
        output_file="my_list.docx",
    ).create()
