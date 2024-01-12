print("Добро пожаловать в викторину 'Угадай год рождения знаменитости'!")
print ("Вам будет задано 5 вопросов, постарайтесь ответить правильно на все!")

answer = None
while answer!= "stop_while":
    answer = ""
    score = 0
    # 1870
    year = int(input(" Введите год рождения В.И.Ленина "))
    if year == 1870:
        score +=1
    # 1929
    year = int(input(" Введите год рождения В.М.Шукшина "))
    if year == 1929:
        score += 1
    # 1938
    year = int(input(" Введите год рождения В.С.Высоцкого "))
    if year == 1938:
        score += 1
    # 1870
    year = int(input(" Введите год рождения А.И.Куприна "))
    if year == 1870:
        score += 1
    # 1672
    year = int(input(" Введите год рождения Петра Великого "))
    if year == 1672:
        score += 1

    print("")
    print("Игра окончена! Число правильных ответов:", score)
    print("Число неправильных ответов:", 5 - score)
    percent = score * 20
    print("Процент правильных ответов:", percent)
    print("Процент неправильных ответов:", 100 - percent)

    print("")
    answer2 = None
    while  answer2 != "stop_while2":
        povtor = input("Хотите повторить игру? (д/н) (y/n) ")
        if  povtor=="н" or povtor=="Н" or povtor=="n" or povtor=="N":
            answer  = "stop_while"
            answer2 = "stop_while2"
        elif  povtor=="д" or povtor=="Д" or povtor=="y" or povtor=="Y":
            answer2 = "stop_while2"
        else:
            print("")
            print("Введите корректное значение ещё раз!")

print("Спасибо за участие!")
