import datetime

weekdays = {
    0:"Понедельник",
    1:"Вторник",
    2:"Среда",
    3:"Четверг",
    4:"Пятница",
    5:"Суббота",
    6:"Воскресенье"
}

start_date = datetime.datetime.strptime(input("Введите дату в формате день.месяц.год: "), '%d.%m.%Y')

def count_days(start_date):
    count = 0
    study_days = [day for day in range(1, 31) if day % 3 == 0]
    for day in study_days:
        new_date = start_date + datetime.timedelta(days=day)
        if new_date.weekday() == 6 or new_date.weekday() == 5:
            new_date = new_date + datetime.timedelta(days=1)
        else:
            count += 1
            print(new_date.strftime(str(count) + '.' + ' ' + "%d.%m.%Y" + ' ' + str(weekdays[new_date.weekday()])))


count_days(start_date)



