
std = ['andey', 'maxim', 'ignat'] 

init = 1
while init:
    print(f'Выберите действие: 1 - Отчислисть 2 - Вывести список студентов ')

    init = int(input('Введите цифру: '))
    if init == 1:
        cum = input('Имя студента: ')
        std.remove(cum.lower())
    else:
        start = 0
        end = len(std)
        for i in range(start, end,1):
            print(f'Студент [{i}] = ', std[i].capitalize())