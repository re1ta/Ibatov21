import table
import statistic


n = 0
name = "Эрнест"
name2 = "Ибатов"
def start():
    a = input("Требуемый формат данных: ")
    if a == "Вакансии": table.get_table()
    elif a == "Статистика": statistic.get_statistic()
    else: print("Неккоректный ввод")

start()