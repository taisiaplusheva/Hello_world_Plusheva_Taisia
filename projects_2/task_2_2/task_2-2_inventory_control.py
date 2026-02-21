f = open("C:/спбпу 1 курс/2 сем/inventory.txt", "w", encoding="utf-8")

reagent_name = input("Название реагента: ")
сuantity_of_reagent = input("Количество реагентов: ")

print(f"Реактив {reagent_name} поступил на склад в количестве {сuantity_of_reagent} штук.", file=f)
f.close()
