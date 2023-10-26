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

    def read_file(
        self,
        match_list: [],  # words that are included for the doc
        remove_list: [],  # words that are removed from inclusion
        inclusion_list: [] = [],  # the same as match_list by default
        exclusion_list: [] = [],  # different list matching words excluded
        same_file: bool = True,
        output_file: str = "",
    ):
        if self.file_path == "":
            return None

        if len(exclusion_list) > 0 and not same_file and output_file == "":
            raise Exception("The second output file cannot be empty.")

        f = open(os.path.join(self.file_path, self.file_name), "r")
        data = f.readlines()
        item_list = []
        this_item = ""
        for x in data:
            if x == "\n":
                for item in match_list:
                    if re.match(f".*({item})", this_item):
                        item_list.append(this_item[:-1])
                this_item = ""
            else:
                for item in match_list:
                    if re.match(f".*({item})", x):
                        this_item = this_item + x.replace("\n", "|")
                for item in remove_list:
                    if (
                        not re.match(f".*({item})", x)
                        and x.replace("\n", "") not in this_item
                    ):
                        this_item = this_item + x.replace("\n", "|")

        filter_1 = "|".join(inclusion_list)
        if len(inclusion_list) == 0:
            filter_1 = "|".join(match_list)

        list_1 = sorted(
            list(
                filter(
                    lambda x: re.match(f".*({filter_1}).*", x),
                    item_list,
                )
            )
        )

        filter_2 = ""
        list_2 = []
        if len(exclusion_list) > 0:
            filter_2 = "|".join(exclusion_list)

        if len(filter_2) > 0:
            list_2 = sorted(
                list(
                    filter(
                        lambda x: re.match(f"^((?!{filter_2}).)*$", x),
                        item_list,
                    )
                )
            )

        doc = docx.Document()
        doc.add_heading(self.header, 0)
        table = self.add_input(doc, list_1, self.delimiter, True)

        if len(exclusion_list) == 0:
            return doc.save(os.path.join(os.getcwd(), self.output_file))

        if same_file:
            cols_1 = len(max(list_1).split(self.delimiter))
            cols_2 = len(min(list_2).split(self.delimiter))
            if cols_2 < cols_1:
                diff = cols_1 - cols_2
                list_2 = [col + "| " * diff for col in list_2]
            self.add_input(doc, list_2, self.delimiter, False, table)
            return doc.save(os.path.join(os.getcwd(), self.output_file))

        else:
            doc.save(os.path.join(os.getcwd(), self.output_file))

            doc = docx.Document()
            doc.add_heading(self.header, 0)
            self.add_input(doc, list_2, self.delimiter, True, None)
            return doc.save(os.path.join(os.getcwd(), output_file))

    def add_input(
        self,
        doc,
        input: [],
        delimiter: str,
        create_table: bool = False,
        table=None,
    ):
        if len(input) < 0:
            raise Exception("Input array cannot be empty.")

        rows = len(input)
        cols = len(max(input).split(delimiter))

        if table is None or create_table:
            table = doc.add_table(rows=1, cols=cols)

        for idx in range(rows):
            cell = table.add_row().cells
            diff = cols - len(input[idx].split(delimiter))
            row = input[idx] + "| " * diff
            col = row.split(delimiter)

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
            create_table = not (self.file_first and self.merge_tables)
            self.add_input(
                doc,
                self.input,
                self.delimiter,
                create_table,
                table,
            )

            # Now save the document to a location
            return doc.save(os.path.join(self.file_path, self.output_file))

        create_table = not (self.file_first and self.merge_tables)
        table = self.add_input(doc, self.input, self.delimiter, create_table)
        self.add_file(doc)
        return doc.save(os.path.join(os.getcwd(), self.output_file))


if __name__ == "__main__":
    PythonDocument(
        file_path=os.path.join(os.getcwd(), "scripts", "docx"),
        file_name="my_games.txt",
        header="My Games List",
        input=["Hello"],
        delimiter="|",
        file_first=True,
        merge_tables=True,
        output_file="my_list.docx",
    ).read_file(
        ["PS PLUS", "EA PLAY", "PS4", "PS5"],
        ["Download"],
        ["PS PLUS", "EA PLAY"],
        ["PS PLUS"],
        False,
        "my_list_2.docx",
    )
