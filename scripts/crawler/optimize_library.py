import os
import shutil
from PIL import Image

def optimize_library(base_dir=r"data/cubari_library/dia-nguc-cua-kien-yeon-deop"):
    total_size_before = 0
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            total_size_before += os.path.getsize(os.path.join(root, f))

    chapters = sorted([
        d for d in os.listdir(base_dir) 
        if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith("temp_")
    ])

    for chap in chapters:
        chap_dir = os.path.join(base_dir, chap)
        temp_dir = os.path.join(base_dir, f"temp_{chap}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        os.makedirs(temp_dir, exist_ok=True)
        
        raw_files = sorted([
            f for f in os.listdir(chap_dir) 
            if os.path.splitext(f)[1].lower() in [".jpg", ".jpeg", ".png", ".webp", ".avif"]
        ])
        
        counter = 1
        for f in raw_files:
            fpath = os.path.join(chap_dir, f)
            try:
                im = Image.open(fpath)
                w, h = im.size
                if h > 3000:
                    top = 0
                    while top < h:
                        bottom = min(top + 3000, h)
                        slice_im = im.crop((0, top, w, bottom))
                        out_name = f"{counter:03d}.webp"
                        out_path = os.path.join(temp_dir, out_name)
                        slice_im.save(out_path, format="WEBP", quality=80, method=4)
                        counter += 1
                        top = bottom
                else:
                    out_name = f"{counter:03d}.webp"
                    out_path = os.path.join(temp_dir, out_name)
                    slice_im = im.convert("RGB") if im.mode not in ("RGB", "RGBA") else im
                    slice_im.save(out_path, format="WEBP", quality=80, method=4)
                    counter += 1
            except Exception as e:
                print(f"Error processing {fpath}: {e}")

        # Clean old files
        for f in os.listdir(chap_dir):
            fp = os.path.join(chap_dir, f)
            if os.path.isfile(fp):
                os.remove(fp)

        # Move optimized slices
        for f in os.listdir(temp_dir):
            shutil.move(os.path.join(temp_dir, f), os.path.join(chap_dir, f))
        
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Done {chap}: {counter - 1} slices")

    total_size_after = 0
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            total_size_after += os.path.getsize(os.path.join(root, f))

    print(f"Before: {total_size_before / (1024*1024):.2f} MB")
    print(f"After: {total_size_after / (1024*1024):.2f} MB")
    if total_size_before > 0:
        print(f"Reduced: {(1 - total_size_after/total_size_before)*100:.1f}%")

if __name__ == "__main__":
    optimize_library()
