print("Совместимость группы крови")

recipient_type = input("Введите группу крови рецепиента (I, II, III, IV): ").strip().upper()
donor_type = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()

if recipient_type == "I" and donor_type == "I" or recipient_type =="II"and donor_type == "I" or recipient_type =="III"and donor_type == "I" or recipient_type =="IV" and donor_type == "I":

    print("Переливание допустимо")

elif recipient_type == "II" and donor_type == "II":

    print("Переливание допустимо")

elif recipient_type == "III" and donor_type == "III":

    print("Переливание допустимо")

elif recipient_type == "IV" and donor_type == "IV":

    print("Переливание допустимо")

else:

    print("Переливание запрещено")