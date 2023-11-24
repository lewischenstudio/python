import os

sessions = [
    "Introduction",
    "Watch before you start",
    "Crash Course on Unity",
    "Player's Finite State Machine",
    "Training Ground Setup",
    "Enemy's State Machine",
    "Battle System",
    "Skill System",
    "Clone Skill",
    "Sword Skill",
    "Ultimate Skill",
    "Magic Crystal Ability",
    "Stats and Elemental Ailments",
    "Items and Inventory",
    "UI",
    "Save and Load",
    "Scene Management and Souls (Currency)",
    "Game Polish - Mechanics",
    "Polish Stage - Visuals",
    "Build and Publish",
    "Additional Section - Enemies",
    "Additional Section - Bug Fixes",
]

for i in range(len(sessions)):
    name = sessions[i]
    folder_name = name.lower().replace(" - ", "_")
    folder_name = folder_name.replace(": ", "_")
    folder_name = folder_name.replace(" ", "_")
    folder_name = folder_name.replace("/", "")
    folder_name = folder_name.replace("&", "and")
    folder_name = folder_name.replace(",", "")
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
