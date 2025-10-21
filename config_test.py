import subprocess
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(r"C:\Users\USER\Scripts\KOMUNIKON\NLP-Modules\config.ini")

bat_path = config.get("UNITEX", "path_n_cmd_name")
input_path = Path(config.get("UNITEX", "sent_txt_path")) / "test_input.txt"

subprocess.run([bat_path, str(input_path)], check=True)