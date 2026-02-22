operator_name = input("Введите имя оператора:")
pressure_value = input("Введите текущее значение датчика давления (Па): ")

with open("C:/спбпу 1 курс/2 сем/sensor_log.txt", "w", encoding="utf-8") as report:

    report.write("ОПЕРАТОР"f"\t{operator_name}\n")
    report.write("ЗНАЧЕНИЕ"f"\t{pressure_value}")

    print("\n Данные успешно сохранены в sensor_log.txt. ")
    

