import table
import statistic


def start():
    a = input("Требуемый формат данных: ")
    if a == "Вакансии": table.get_table()
    elif a == "Статистика": statistic.get_statistic()
    else: print("Неккоректный ввод")

start()