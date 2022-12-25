import csv
from vacancy import Vacancy


class DataSet:
    def __init__(self, file: str):
        self.__file = file
        self.__data = self.universal_csv_parser()
        self.__vacancies_objects = [Vacancy(item) for item in self.data]

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.file = file

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def vacancies_objects(self):
        return self.__vacancies_objects

    @vacancies_objects.setter
    def vacancies_objects(self, vacancies_objects):
        self.__vacancies_objects = vacancies_objects

    def universal_csv_parser(self) -> list:
        with open(self.file, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            array1 = []
            array2 = []
            for i in reader:
                if array1 == []:
                    array1 = i
                    lineL = len(array1)
                else:
                    if ("" not in i and len(i) == lineL): array2.append(dict(zip(array1, i)))
        if array1 == []:
            print("Пустой файл")
            exit()
        return array2
