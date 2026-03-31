import json
import os
from datetime import datetime

data = {"habits": []}
index = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def input_tr(a):
    while True:
        try:
            b = int(input(a))
            return b
        except ValueError:
            print("Введите Число!")


def dump(data, filename="myp"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load(filename="myp"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        data = {"habits": []}
        dump(data, filename)
        return data


def clear_json(data, filename="myp"):
    clear()
    if len(data["habits"]) > 0:
        with open(filename, "w", encoding="utf-8") as f:
            data = {"habits": []}
            dump(data)
        print("Список очищен")
    else:
        print("Список и так пуст!")
    return data


def add_habit(data):
    clear()
    name = input("Введите название привычки:")
    data["habits"].append({"name": name, "streak": 0, "last_done": None})
    dump(data)
    return data


def del_habit(data):
    if len(data["habits"]) > 0:
        try:
            index = int(input("Введите номер: ")) - 1
            if 0 <= index < len(data["habits"]):
                data["habits"].pop(index)
                return data
            else:
                print("Введите верное число!")
        except (ValueError, TypeError):
            print("Введите число!")
    return data


def lst_habits(data):
    clear()
    now = datetime.now().strftime("%Y.%m.%d")
    if len(data["habits"]) > 0:
        for i, d in enumerate(data["habits"], start=1):
            print(
                f"{i}. {d['name']} | Серия: {d['streak']} | {'Выполнено' if d['last_done'] == now else 'Не выполнено'}"
            )
    else:
        print("Список пуст")
    return data


def update_streak(data, index):
    if data["habits"][index]["last_done"] is None:
        data["habits"][index]["streak"]+= 1
        return
    now = datetime.now().date()
    last = (
        datetime.strptime(data["habits"][index]["last_done"], "%Y.%m.%d").date()
    )
    diff = now - last
    if diff.days == 1:
        data["habits"][index]["streak"] += 1
    elif diff.days > 1:
        data["habits"][index]["streak"] = 1
    elif diff.days == 0:
        print("Уже выполнялось сегодня!")
    return data


def get_done(data):
    lst_habits(data)
    if len(data["habits"]) > 0:
        try:
            index = int(input("Введите номер выполненной привычки:")) - 1
            if 0 <= index < len(data["habits"]):
                now = datetime.now().strftime("%Y.%m.%d")
                if data["habits"][index]["last_done"] == now:
                    print("Уже выполнено!!")
                else:
                    update_streak(data, index)
                    data["habits"][index]["last_done"] = now
            else:
                print('Введите верное число!')
        except (ValueError, TypeError):
            print("Введите число!")
        dump(data)
    return data


def menu():
    print(
        "\nМеню:\n1.Добавить привычку\n2.Удалить привычку\n3.Список привычек\n4.Отметить выполнение\n5.Очистить все привычки\n6.Выход"
    )


print("Добро пожаловать в трекер привычек!")
data = load()
while True:
    menu()
    sel = input_tr("Выберите пункт меню:")
    if sel == 1:
        data = add_habit(data)
    elif sel == 2:
        lst_habits(data)
        data = del_habit(data)
    elif sel == 3:
        lst_habits(data)
    elif sel == 4:
        data, index = get_done(data)
    elif sel == 5:
        data = clear_json(data)
    elif sel == 6:
        print("До свидания!")
        break
