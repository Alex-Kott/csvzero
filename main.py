import csv
from pathlib import Path
from tkinter import filedialog, Tk


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
    source_dir = Path(filedialog.askdirectory(title="Откуда взять файлы?"))
    dest_dir = Path(filedialog.askdirectory(title="Куда сложить файлы?"))

    csv_files = [entry for entry in source_dir.iterdir() if entry.suffix == ".csv"]
    for csv_file in csv_files:
        transform_csv_file(csv_file, dest_dir)