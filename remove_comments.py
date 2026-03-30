import os
import re

folder = "."

for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.lower().endswith(".json"):
            filepath = os.path.join(root, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Remove /* ... */ comment blocks
            cleaned = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)

            # Remove extra blank lines
            cleaned = re.sub(r"\n\s*\n\s*\n+", "\n\n", cleaned)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned)

            print(f"Cleaned: {filepath}")