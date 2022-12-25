from math import floor


class InputConect:
    def __init__(self, data: list, profession_name: str):
        self.__data = data
        self.__profession_name = profession_name
        self.__vacancies_by_city = {}
        self.__vacancies_amount = 0

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def profession_name(self):
        return self.__profession_name

    @profession_name.setter
    def profession_name(self, profession_name):
        self.__profession_name = profession_name

    def get_vacancies_by_city(self):
        vbc = {} #vacancies_by_city
        for i in self.__vacancies_by_city.keys():
            if self.__vacancies_by_city[i] >= floor(self.__vacancies_amount / 100):
                vbc[i] = round(self.__vacancies_by_city[i] / self.__vacancies_amount, 4)
        vbc = dict(sorted(vbc.items(), key=lambda item: item[1], reverse=True))
        return dict(zip(list(vbc.keys())[:10], list(vbc.values())[:10]))

    def get_vacancies_by_year_for_profession(self):
        sbyfp = {} #salary_by_year_for_profession
        for i in self.data:
            if self.profession_name in i.name:
                if i.published_at in sbyfp.keys(): sbyfp[i.published_at] += 1
                else: sbyfp[i.published_at] = 1
        if (sbyfp == {}): sbyfp = {2022: 0}
        return dict(sorted(sbyfp.items(), key=lambda item: item[0]))

    def get_vacancies_by_year(self):
        vby = {}  # vacancies_by_year
        for i in self.data:
            if i.published_at in vby.keys(): vby[i.published_at] += 1
            else: vby[i.published_at] = 1
            if i.area_name in self.__vacancies_by_city.keys(): self.__vacancies_by_city[i.area_name] += 1
            else: self.__vacancies_by_city[i.area_name] = 1
            self.__vacancies_amount += 1
        return dict(sorted(vby.items(), key=lambda item: item[0]))

    def get_salary_by_year(self):
        sby = {}
        sam = {}  # salary_by_year, salary_amount
        for i in self.data:
            if i.published_at in sby.keys():
                sby[i.published_at] += (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                sam[i.published_at] += 1
            else:
                sby[i.published_at] = (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                sam[i.published_at] = 1
        for i in sby.keys(): sby[i] = int(sby[i] / sam[i])
        return dict(sorted(sby.items(), key=lambda item: item[0]))

    def get_salary_by_year_for_profession(self):
        sbyfp = {} #salary_by_year_for_profession
        sa = {} #salary_amount
        for i in self.data:
            if self.profession_name in i.name:
                if (i.published_at not in sbyfp.keys()):
                    sbyfp[i.published_at] = (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                    sa[i.published_at] = 1
                else:
                    sbyfp[i.published_at] += (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                    sa[i.published_at] += 1
        for year in sbyfp.keys(): sbyfp[year] = int(sbyfp[year] / sa[year])
        if sbyfp == {}: sbyfp = {2022: 0}
        return dict(sorted(sbyfp.items(), key=lambda item: item[0]))

    def get_salary_by_city(self):
        sbc = {} #salary_by_city
        sa = {} #salary_amount
        for i in self.data:
            if self.__vacancies_by_city[i.area_name] >= floor(self.__vacancies_amount / 100):
                if i.area_name in sbc.keys():
                    sbc[i.area_name] += (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                    sa[i.area_name] += 1
                else:
                    sbc[i.area_name] = (i.salary_from + i.salary_to) / 2 * currency_to_rub[i.salary_currency]
                    sa[i.area_name] = 1
        for city in sbc.keys(): sbc[city] = int(sbc[city] / sa[city])
        sbc = dict(sorted(sbc.items(), key=lambda item: item[1], reverse=True))
        return dict(zip(list(sbc.keys())[:10], list(sbc.values())[:10]))


currency_to_rub = {
    "AZN": 35.68, "BYR": 23.91, "EUR": 59.90, "GEL": 21.74, "UZS": 0.0055,
    "KGS": 0.76, "KZT": 0.13, "RUR": 1, "UAH": 1.64, "USD": 60.66
}
