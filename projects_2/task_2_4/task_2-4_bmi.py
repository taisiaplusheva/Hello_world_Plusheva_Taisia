height = float(input("Введите рост (м): "))
weight = float(input("Введите вес (кг): "))

bmi = float(weight / ((height/100)** 2))

print("Отчет о состоянии здоровья")
print("Рост: \t"f"{height}" "см \nВес: \t" f"{weight}" "кг")
print("Индекс массы тела:"f"{bmi:.2f}")