import json
import os
data = {
    'habits': []
}
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_tr(a):
    try:
        b = int(input(a))
        return b
    except ValueError:
        print('Введите Число!')



def dump(data,filename = 'myp'):
    with open (filename, 'w',encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def load(filename = 'myp'):
    try:
        with open (filename,'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        data = {'habits':[]}
        dump(data,filename)
        return data



def clear_json(data,filename = 'myp'):
    clear()
    if len(data['habits'])>0:
        with open (filename,'w',encoding='utf-8') as f:
            data = {'habits':[]}
            json.dump(data,f)
        print('Список очищен')
    else:
        print('Список и так пуст!')
    return data


def add_habit():
    clear()
    name = input('Введите название привычки:')
    data['habits'].append({
        'name': name,
        'streak':0,
        'last_done':None
    })
    dump(data)


def del_habit():
    if len(data['habits'])>0:
            try:
                index = int(input('Введите номер: ')) - 1
                data['habits'].pop(index)
                dump(data)
            except (ValueError,TypeError):
                print('Введите число!')


def lst_habits():
    clear()
    if len(data['habits'])>0:
        for i,d in enumerate(data['habits'],start=1):
            print(f'{i}. {d['name']} | Streak: {d['streak']}')
    else:
        print('Список пуст')


def menu():
    print('\nМеню:\n1.Добавить привычку\n2.Удалить привычку\n3.Список привычек\n4.Отметить выполнение\n5.Очистить все привычки\n6.Выход')


print('Добро пожаловать в трекер привычек!')
data = load()
while True:
    menu()
    print(data)
    sel = input_tr('Выберите пункт меню:')
    if sel == 1:
        add_habit()
    elif sel == 2:
        lst_habits()
        del_habit()
    elif sel == 3:
        lst_habits()
    elif sel == 4:
        print('В разработке!')
    elif sel == 5:
        data = clear_json(data)
    elif sel == 6:
        print('До свидания!')
        break
