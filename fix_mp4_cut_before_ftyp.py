import os

def fix_mp4_cut_before_ftyp(folder_path, extension=".mp4", dry_run=True, scan_bytes=65536):
    """
    Search for 'ftyp' marker near the start and remove all bytes before the MP4 header.
    Writes a '.fixed.mp4' copy next to each source.
    """
    if not extension.startswith("."):
        extension = "." + extension

    repaired = 0
    for fname in os.listdir(folder_path):
        if not fname.lower().endswith(extension.lower()):
            continue
        src = os.path.join(folder_path, fname)
        if not os.path.isfile(src):
            continue

        with open(src, "rb") as f:
            head = f.read(scan_bytes)
        i = head.find(b"ftyp")
        if i < 0:
            print(f"Skip {fname}: 'ftyp' not found within first {scan_bytes} bytes.")
            continue

        # MP4 box starts 4 bytes before 'ftyp' (size field)
        start = i - 4
        if start <= 0:
            print(f"OK {fname}: no extra prefix detected.")
            continue

        out = os.path.join(folder_path, os.path.splitext(fname)[0] + ".fixed" + extension)
        if dry_run:
            print(f"Would fix {fname}: remove {start} leading bytes -> {os.path.basename(out)}")
            continue

        # Stream copy from 'start' to end
        with open(src, "rb") as fin, open(out, "wb") as fout:
            fin.seek(start)
            while True:
                chunk = fin.read(1024 * 1024)
                if not chunk:
                    break
                fout.write(chunk)
        print(f"Fixed {fname} -> {os.path.basename(out)}")
        repaired += 1

    if not dry_run:
        print(f"\nDone. Wrote {repaired} repaired file(s).")


# Example usage:
fix_mp4_cut_before_ftyp("C:/Users/USER/dwhelper", dry_run=False)