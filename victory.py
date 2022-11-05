authors_list = ('Пушкина', 'Гоголя', 'Есенина', 'Достоевского', 'Маяковского')   # Список авторов
birthday_list = (1799, 1809, 1809, 1821, 1893)               # Список годов рождения авторов

print('Привет! Ответь на 5 вопросов!')                      # Приглашение поучаствовать

question = 'Напиши год рождения'                             # Повторяющаяся переменная
count_correct = 0                      # Счетчик верных ответов
count_mistake = 0                      # Счетчик неверных ответов
answer = 1                            # Определение переменной для ответов

while answer == 1:
    for author, birthday in zip(authors_list, birthday_list): # Проходим циклом по спискам authors_list и birthday_list
        answer = int(input('Напиши год рождения ' + author + ' '))   # Формируем вопрос и записываем ответ в answer
        if answer == birthday:          # Если ответ верный
            count_correct +=1           # Добавяем 1 в верные
            print("Верно!")             # И сообщаем игроку
        else:
            count_mistake +=1            # Иначе прибавляем 1 к неверные
            print("Ошибка!")

    print('Колличесто правильных ответов - ', count_correct)                               # Выводим статистику
    print('Колличесто неправильных ответов - ', count_mistake)
    print('Процент правильных ответов - ', count_correct * 100 / len(authors_list))
    print('Процент неправильных ответов - ', count_mistake * 100 / len(authors_list))
    answer = int(input('Сыграем еще? Да - 1, Нет - 0  '))                                  # Предложение сыграть еще

print('End')








