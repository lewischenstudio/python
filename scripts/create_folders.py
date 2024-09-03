import os

sessions = []

under_score_list = [" - ", ": ", " "]
empty_string_list = ["/", ",", "?"]
for i in range(len(sessions)):
    name = sessions[i]
    folder_name = name.lower()
    for item in under_score_list:
        folder_name = folder_name.replace(item, "_")
    for item in empty_string_list:
        folder_name = folder_name.replace(item, "")
    folder_name = folder_name.replace("&", "and")
    i += 1
    if i < 10:
        i = f"0{i}"
    folder_path = os.path.join(os.getcwd(), f"scripts/{i}_{folder_name}")
    file_path = os.path.join(folder_path, "README.md")
    os.mkdir(folder_path)
    with open(file_path, "w") as file_w:
        file_w.write(f"## Section {i}: {name}\n")
        file_w.write("\n")
        file_w.write("#### Table of Contents")
        file_w.write("\n")
    file_w.close()

    # Convert Windows files to Linux/Unix/MacOS files (CRLF --> LF)
    with open(file_path, "rb") as file_rb:
        content = file_rb.read()
    content = content.replace(b"\r\n", b"\n")  # (CRLF --> LF)
    # content = content.replace(b"\n", b"\r\n")  # (LF --> CRLF)
    with open(file_path, "wb") as file_w:
        file_w.write(content)
    file_w.close()

print("done")
