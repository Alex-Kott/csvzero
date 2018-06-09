import csv
import sys
from pathlib import Path
from tkinter import filedialog, Tk
import json
import win32con, win32api



def load_settings():
    if sys.platform == 'linux':
        with open("./.settings") as file:
            settings_text = json.loads(file.read())
    else:
        with


def transform_csv_file(file_name, dest_dir):
    with open(file_name) as read_file:
        csvreader = csv.reader(read_file, delimiter=',')
        with open(dest_dir / file_name.name, "w") as write_file:
            csvwriter = csv.writer(write_file, delimiter=",")
            for row in csvreader:
                print(row)
                csvwriter.writerow([row[0], "000000", *row[1:]])


if __name__ == "__main__":
    root = Tk()
    settings = load_settings()

    source_dir = Path(filedialog.askdirectory(title="Откуда взять файлы?"))
    dest_dir = Path(filedialog.askdirectory(title="Куда сложить файлы?"))

    with open(".settings", "w") as outfile:
        settings = {
            'source_dir': source_dir,
            'dest_dir': dest_dir
        }
        json.dump(settings, outfile)

    if sys.platform != 'linux':
        win32api.SetFileAttributes(".settings", win32con.FILE_ATTRIBUTE_HIDDEN)


    csv_files = [entry for entry in source_dir.iterdir() if entry.suffix == ".csv"]
    for csv_file in csv_files:
        transform_csv_file(csv_file, dest_dir)