print("=== Анализ последовательности ДНК ===")

dna = input("Введите последовательность ДНК: ").upper()

count_A = dna.count("A")
count_t = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")

quantity = (count_A + count_t + count_G + count_C)

percent_A = int((count_A / quantity)*100)
percent_T = int((count_t / quantity)*100)
percent_G = int((count_G / quantity)*100)
percent_C = int((count_C / quantity)*100)

print("Подсчёт нуклеотидов:\n")
print(f"A: {count_A} ({percent_A}) % \n")
print(f"T: {count_t} ({percent_T}) % \n")
print(f"G: {count_G} ({percent_G}) % \n")
print(f"C: {count_C} ({percent_C}) % \n")
print("Общая длина: " f"{quantity} " "нуклеотидов")