import os

for root, dirs, files in os.walk(r"d:\Nhung\trans-tool"):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith((".py", ".json", ".md", ".txt")) and f != "raw_full.md":
            p = os.path.join(root, f)
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as fl:
                    cnt = fl.read()
                    if "9749021" in cnt:
                        print("Found 9749021 in:", p)
            except:
                pass
