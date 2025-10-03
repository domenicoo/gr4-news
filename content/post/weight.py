import os

def replace_weight(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(subdir, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content = content.replace("weight: 2", "weight: 10")
                if new_content != content:  # only overwrite if changes
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated: {filepath}")

if __name__ == "__main__":
    directory = input("Enter directory path: ").strip()
    replace_weight(directory)
