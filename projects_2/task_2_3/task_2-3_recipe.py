name_medium = input("Название среды:")
agar_concentration = input("Концентрация агара (%):")
sterilization = input("Температура стерилизации:")

with open("C:/спбпу 1 курс/2 сем/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name_medium}\n")
    recipe.write(f"{agar_concentration}\n")
    recipe.write(f"{sterilization}\n")

    print(f"\nФайл 'recipe.txt' успешно сформирован!")
