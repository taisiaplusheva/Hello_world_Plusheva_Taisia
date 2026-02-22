solution_volume = float(input("Введите объем раствора (мл): "))

mass_of_NaCl = (solution_volume * 0.0009)
water_volume = solution_volume

with open("C:/спбпу 1 курс/2 сем/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ: \n")
    recipe.write( "-" * 23)
    recipe.write("\nОбщий объем: "f"\t{solution_volume}"  "\tмл\n")
    recipe.write("Масса соли: "f"\t{mass_of_NaCl:.2f}" "\tг\n")
    recipe.write("Объем воды: "f"\t{water_volume}" "\tмл\n")
