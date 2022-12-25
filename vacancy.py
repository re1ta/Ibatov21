class Vacancy:
    def __init__(self, item: dict):
        self.__name = item["name"]
        self.__salary_from = float(item["salary_from"])
        self.__salary_to = float(item["salary_to"])
        self.__salary_currency = item["salary_currency"]
        self.__area_name = item["area_name"]
        self.__published_at = int(item["published_at"][:4])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary_from(self):
        return self.__salary_from

    @salary_from.setter
    def salary_from(self, salary_from):
        self.__salary_from = salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @salary_to.setter
    def salary_to(self, salary_to):
        self.__salary_to = salary_to

    @property
    def salary_currency(self):
        return self.__salary_currency

    @salary_currency.setter
    def salary_currency(self, salary_currency):
        self.__salary_currency = salary_currency

    @property
    def area_name(self):
        return self.__area_name

    @area_name.setter
    def area_name(self, area_name):
        self.__area_name = area_name

    @property
    def published_at(self):
        return self.__published_at

    @published_at.setter
    def published_at(self, published_at):
        self.__published_at = published_at
