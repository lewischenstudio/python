import os

sessions = [
    "Introduction",
    "A Quick Refresher - Basic Review",
    "Variables and Memory",
    "Numeric Types",
    "Function Parameters",
    "First-Class Functions",
    "Scopes, Closures and Decorators",
    "Tuples as Data Structures and Named Tuples",
    "Modules, Packages and Namespaces",
    "Python Updates",
    "Extras"
]

for i in range(len(sessions)):
    name = sessions[i]
    folder_name = name.replace(" ", "_").lower()
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
