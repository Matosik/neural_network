import csv
import os

def create_annotation(subdir:str,label, folderpath) -> None:
    with open("annotation_train.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        for i in range(1020):
            absolute_way = os.path.abspath(f'{folderpath}/train/{subdir}/{i}.jpg')
            if (os.path.isfile(absolute_way)) == True:
                file_writer.writerow([absolute_way,label])


def main():
    folderpath='data_set_for_lerning'
    with open("annotation_train.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator='\n')
        file_writer.writerow(
            ["folder_path", "label"])
    subdir = "CatIT"
    create_annotation(subdir,'1',folderpath)
    subdir = "DogIT"
    create_annotation(subdir,'0',folderpath)


if __name__ == "__main__":
    main()