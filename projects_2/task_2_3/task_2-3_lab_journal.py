print("Электронный лабораторный журнал")
researcher_name = input("ФИО исследователя")
date = input("Дата")
experiment_name = input("Эксперимент")
conclusion = input("Вывод")

with open("C:/спбпу 1 курс/2 сем/journal.txt", "w", encoding="utf-8") as journal:
    journal.write("+--------------------------------------------------+\n")
    journal.write("|               Лабораторный журнал                |\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write("|ФИО исследователя:"f"{researcher_name.ljust(32)}|\n")
    journal.write("|Дата:"f"{date.ljust(45)}|\n")
    journal.write("|Эксперимент:"f"{experiment_name.ljust(38)}|\n")
    journal.write("+--------------------------------------------------+\n")
    journal.write("| Вывод:                                           |\n")
    journal.write(""f"|{conclusion.ljust(50)}|\n")
    journal.write("+--------------------------------------------------+\n")
   

