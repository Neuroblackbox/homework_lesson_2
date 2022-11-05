day_of_birth = 6
year_of_birth = 1799


input_year = (int(input('Напиши год рождения А. С Пушкина: ')))
if input_year == year_of_birth:
    input_day = (int(input('Напиши день рождения А. С Пушкина: ')))
    if input_day ==day_of_birth:
        print('Верно!')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год!')