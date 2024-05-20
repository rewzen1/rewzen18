amount = 0
tickets = int(input("количество билетов:\n"))
for age in range(tickets):
    age = int(input("Возраст посетителя:\n"))
    if age <18:
        amount += 0
    elif age>=18 and age <= 25:
        amount += 990
    elif age >25:
        amount += 1390
    if amount == 0:
        print("добро пожаловать")
    else:
        print("количество билетов:",tickets,"шт:\n")
    if tickets >= 3:
        discont =amount / 100 * 10
        print("скидка составляет:","%.2f" %discont)
        print("Стоимость с учетом скидки:","%.2f"  )
    if tickets <=2:
        notdiscont =amount
        print("Стоимость:","%.2f" %notdiscont)