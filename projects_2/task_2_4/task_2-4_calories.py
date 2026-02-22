protein_gr = int(input("Масса белков (г):"))
fats_gr = int(input("Масса жиров (г):"))
carbohydrates_gr = int(input("Масса углеводов (г):"))

calories = int((protein_gr*4)+(fats_gr*9)+(carbohydrates_gr*4))

print(f"{calories}" "ккал")

