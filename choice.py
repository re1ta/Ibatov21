import table
import statistic


n = 0
n += 2
def start():
    a = input("Требуемый формат данных: ")
    if a == "Вакансии": table.get_table()
    elif a == "Статистика": statistic.get_statistic()
    else: print("Неккоректный ввод")

start()