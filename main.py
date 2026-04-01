import json
import os
from datetime import datetime


def clear():
    os.system("cls" if os.name == "nt" else "clear")


data = {"habits": []}
sel_language = "en"


language = {
    "ru": {
        "prin": "Добро пожаловать в трекер привычек!",
        "input_int": "Введите число!",
        "clear": "Список очищен",
        "cleaned": "Список и так пуст!",
        "done": "Уже выполнено!",
        "add_habit": "Введите название привычки:",
        "input_num": "Введите номер: ",
        "inp_correct": "Введите верное число!",
        "streak": "Серия:",
        "list_clean": "Список пуст",
        "done_yet": "Уже выполнялось сегодня!",
        "inp_num_habbit": "Введите номер выполненной привычки:",
        "menu": "\nМеню:\n1.Добавить привычку\n2.Удалить привычку\n3.Список привычек\n4.Отметить выполнение\n5.Очистить все привычки\n6.Выход",
        "sel_menu": "Выберите пункт меню:",
        "bye": "До свидания!",
    },
    "en": {
        "prin": "Welcome to the habit tracker!",
        "input_int": "Enter a number!",
        "clear": "List cleared",
        "cleaned": "The list is already empty!",
        "done": "Already done!",
        "add_habit": "Enter the habit name:",
        "input_num": "Enter the number: ",
        "inp_correct": "Enter a valid number!",
        "streak": "Streak:",
        "list_clean": "List is empty",
        "done_yet": "Already completed today!",
        "inp_num_habbit": "Enter the number of the completed habit:",
        "menu": "\nMenu:\n1. Add habit\n2. Delete habit\n3. Habit list\n4. Mark as completed\n5. Clear all habits\n6. Exit",
        "sel_menu": "Select a menu item:",
        "bye": "Goodbye!",
    },
}


def translate(key):
    return language[sel_language][key]


def sel_lang(sel_language):
    print("Select language(Выберите язык):\n1:Russian(Русский)\n2:English(Английский)")
    d = int(input(translate("input_num")))
    sel_language = "ru" if d == 1 else "en" if d == 2 else "en"
    clear()
    return sel_language


sel_language = sel_lang(sel_language)


def has_habits(data):
    return len(data["habits"]) > 0


def is_valid(data, index):
    return 0 <= index < len(data["habits"])


def input_tr(a):
    while True:
        try:
            b = int(input(a))
            return b
        except ValueError:
            print(translate("input_int"))


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
    if has_habits(data):
        with open(filename, "w", encoding="utf-8") as f:
            data = {"habits": []}
            dump(data)
        print(translate("clear"))
    else:
        print(translate("cleaned"))
    return data


def mark_done(data, index):
    now = datetime.now().strftime("%Y.%m.%d")
    if data["habits"][index]["last_done"] == now:
        print(translate("done"))
    else:
        update_streak(data, index)
        data["habits"][index]["last_done"] = now


def add_habit(data):
    clear()
    name = input(translate("add_habit"))
    data["habits"].append({"name": name, "streak": 0, "last_done": None})
    dump(data)
    return data


def del_habit(data):
    if has_habits(data):
        try:
            index = int(input(translate("input_num"))) - 1
            if is_valid(data, index):
                data["habits"].pop(index)
                return data
            else:
                print(translate("inp_correct"))
        except (ValueError, TypeError):
            print(translate("input_int"))
    return data


def lst_habits(data):
    clear()
    now = datetime.now().strftime("%Y.%m.%d")
    if has_habits(data):
        for i, d in enumerate(data["habits"], start=1):
            print(
                f"{i}. {d['name']} | {translate("streak")} {d['streak']} | {'✅' if d['last_done'] == now else '❌'}"
            )
    else:
        print(translate("list_clean"))
    return data


def update_streak(data, index):
    if data["habits"][index]["last_done"] is None:
        data["habits"][index]["streak"] += 1
        return
    now = datetime.now().date()
    last = datetime.strptime(data["habits"][index]["last_done"], "%Y.%m.%d").date()
    diff = now - last
    if diff.days == 1:
        data["habits"][index]["streak"] += 1
    elif diff.days > 1:
        data["habits"][index]["streak"] = 1
    elif diff.days == 0:
        print(translate("done_yet"))
    return data


def get_done(data):
    clear()
    lst_habits(data)
    if has_habits(data):
        try:
            index = int(input(translate("inp_num_habbit"))) - 1
            if is_valid(data, index):
                mark_done(data, index)
            else:
                print(translate("inp_correct"))
        except (ValueError, TypeError):
            print(translate("input_int"))
        dump(data)
    return data


def menu():
    print(translate("menu"))


print(translate("prin"))
data = load()
while True:
    menu()
    sel = input_tr(translate("sel_menu"))
    if sel == 1:
        data = add_habit(data)
    elif sel == 2:
        lst_habits(data)
        data = del_habit(data)
    elif sel == 3:
        lst_habits(data)
    elif sel == 4:
        data = get_done(data)
    elif sel == 5:
        data = clear_json(data)
    elif sel == 6:
        clear()
        print(translate("bye"))
        break
