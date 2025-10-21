import os
import glob
import pandas as pd

# Path to the folder containing the CSV files
FOLDER = r"C:\Users\USER\dwhelper"
# r"c:\path\to\folder"   # change this to your folder path

# Find all .csv files in the folder
csv_files = glob.glob(os.path.join(FOLDER, "*.csv"))

if not csv_files:
    print("No CSV files found in the folder.")
else:
    dfs = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            # Keep only required columns if they exist
            cols = [c for c in ["source", "before", "after", "distance"] if c in df.columns]
            if cols:
                dfs.append(df[cols])
            else:
                print(f"Warning: {file} has none of the required columns.")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if dfs:
        merged = pd.concat(dfs, ignore_index=True)
        out_file = os.path.join(FOLDER, "merged_reports.tsv")
        merged.to_csv(out_file, sep="\t", index=False, encoding="utf-8")
        print(f"Merged {len(csv_files)} files into: {out_file}")
    else:
        print("No valid data to merge.")
