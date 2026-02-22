capsules_quantity = int(input("Введите количество произведенных капсул (шт):"))
packing_capacity = int(input("Введите количество капсул в одной упаковке (шт):"))

packs = (capsules_quantity // packing_capacity)
surplus = (capsules_quantity % packing_capacity)

print("Отчет фасовочного цеха")
print("Полных упаковок:" f"\t{packs}")
print("Остаток купсул:" f"\t\t{surplus}")