

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет
vozrast = int (input("Введите Ваш возраст - "))
if vozrast >= 18:
    print("Доступ разрешён")
else:
    print ("Извините,пользование данным ресурсом только с 18 лет")

