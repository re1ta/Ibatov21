from dataSet import DataSet
from input_conect import InputConect
from report import Report

file_name = input("Введите название файла: ")
profession_name = input("Введите название профессии: ")
data = DataSet(file_name).vacancies_objects
if not data:
    print("Нет данных")
else:
    result = InputConect(data, profession_name)

    print(f"Динамика уровня зарплат по годам: {result.get_salary_by_year()}")
    print(f"Динамика количества вакансий по годам: {result.get_vacancies_by_year()}")
    print(f"Динамика уровня зарплат по годам для выбранной профессии: {result.get_salary_by_year_for_profession()}")
    print(
        f"Динамика количества вакансий по годам для выбранной профессии: {result.get_vacancies_by_year_for_profession()}")
    print(f"Уровень зарплат по городам (в порядке убывания): {result.get_salary_by_city()}")
    print(f"Доля вакансий по городам (в порядке убывания): {result.get_vacancies_by_city()}")

    report = Report(result.get_salary_by_year(),
                    result.get_vacancies_by_year(),
                    result.get_salary_by_year_for_profession(),
                    result.get_vacancies_by_year_for_profession(),
                    result.get_salary_by_city(),
                    result.get_vacancies_by_city(),
                    profession_name)

    report.generate_excel()
    report.generate_image()
    report.generate_pdf()
