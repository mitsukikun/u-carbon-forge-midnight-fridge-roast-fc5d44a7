import os

LINE = "My smart fridge locks me out after midnight like the cheese inside is in witness protection."

try:
    os.makedirs("/output", exist_ok=True)
except Exception:
    pass

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
