import os
import shutil

folder = "."

rules = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".txt"],
    "Code": [".py", ".html", ".css", ".js"]
}

for file in os.listdir(folder):
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)

        for category, extensions in rules.items():
            if ext.lower() in extensions:
                os.makedirs(category, exist_ok=True)
                shutil.move(file, os.path.join(category, file))
                print(f"Moved {file} → {category}")
                break

print("Agent finished.")