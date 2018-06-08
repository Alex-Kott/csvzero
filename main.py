import csv
import os
from pathlib import Path


def transform_csv_file(file_name):
    with open(file_name) as read_file:
        csvreader = csv.reader(read_file, delimiter=',')
        with open(f"{file_name.stem}_tmp.csv", "w") as write_file:
            csvwriter = csv.writer(write_file, delimiter=",")
            for row in csvreader:
                csvwriter.writerow([row[0], "000000", *row[1:]])

    os.remove(file_name)
    os.rename(f"{file_name.stem}_tmp.csv", file_name)


if __name__ == "__main__":
    from tkinter import filedialog, Tk

    root = Tk()
    dir_name = Path(filedialog.askdirectory())

    csv_files = [entry for entry in dir_name.iterdir() if entry.suffix == ".csv"]
    for csv_file in csv_files:
        transform_csv_file(csv_file)