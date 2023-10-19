import os

sessions = [
    "The Simple Concepts",
    "Path Element",
    "Styling",
    "Viewport",
    "Document",
    "Painting",
    "Paint Servers",
    "Animations",
    "Bonus Section",
]

for i in range(len(sessions)):
    name = sessions[i]
    folder_name = name.replace(" - ", "_").replace(": ", "_")
    folder_name = folder_name.replace(" ", "_").lower()
    i += 1
    if i < 10:
        i = f"0{i}"
    folder_path = os.path.join(os.getcwd(), f"scripts/{i}_{folder_name}")
    file_path = os.path.join(folder_path, "README.md")
    os.mkdir(folder_path)
    with open(file_path, "w") as file_:
        file_.write(f"## Section {i}: {name}\n")
        file_.write("\n")
        file_.write("#### Table of Contents\n")
    file_.close()

print("done")
