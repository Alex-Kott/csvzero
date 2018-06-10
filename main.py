import csv
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import json

settings_file_path = Path("./.settings.json")


def load_settings():
    if settings_file_path.exists():
        with open(settings_file_path) as file:
            settings = json.loads(file.read())
            # print(settings)

        for k, v in settings.items():
            # print(k ,v)
            settings[k] = Path(v)
    else:
        settings = {
            "source_dir": Path.cwd(),
            "dest_dir": Path.cwd()
        }
    return settings


def save_settings():
    settings = {
        'source_dir': e1.get(),
        'dest_dir': e2.get()
    }
    with open(settings_file_path, "w") as outfile:
        json.dump(settings, outfile)


def transform_csv_file():
    source_dir = Path(e1.get())
    dest_dir = Path(e2.get())

    for file_path in source_dir.iterdir():
        if file_path.suffix != ".csv":
            continue
        with open(file_path) as read_file:
            csvreader = csv.reader(read_file, delimiter=',')
            with open(dest_dir / (f"{file_path.stem}.txt"), "w", newline='') as write_file:
                csvwriter = csv.writer(write_file, delimiter=",")

                for row in csvreader:
                    csvwriter.writerow([row[0], "000000", *row[1:]])
    root.quit()


def select_dir(title, element):
    dir_path = Path(filedialog.askdirectory(title=title))
    element.delete(0, END)
    element.insert(0, dir_path)
    save_settings()


if __name__ == "__main__":
    global settings

    root = Tk()
    settings = load_settings()

    Label(root, text="Source folder").grid(row=0)
    Label(root, text="Dest folder").grid(row=1)

    e1 = Entry(root, width=60)
    e2 = Entry(root, width=60)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    e1.insert(0, settings['source_dir'])
    e2.insert(0, settings['dest_dir'])

    b1 = Button(text="Select folder", command=lambda: select_dir(title="Откуда брать файлы?",
                                                                 element=e1))
    b2 = Button(text="Select folder", command=lambda: select_dir(title="Куда положить файлы?",
                                                                 element=e2))
    b3 = Button(text="OK", command=transform_csv_file)
    b1.grid(row=0, column=2)
    b2.grid(row=1, column=2)
    b3.grid(row=2, column=1)

    mainloop()
