import os
import sqlite3
pathdb = os.path.join(os.path.dirname(__file__), "database.db")


def init_db():
    connection = sqlite3.connect(pathdb)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   streak INTEGER);''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS habit_logs(habit_id INTEGER,
                   log_date TEXT,
                   FOREIGN KEY(habit_id) REFERENCES habits(id) ON DELETE CASCADE);''')

def clear():
    os.system("cls" if os.name == "nt" else "clear")


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


def has_habits(habits):
    return len(habits) <= 0


def is_valid(habits, index_us):
    return 0 < index_us <= len(habits)


def input_tr(a):
    while True:
        try:
            b = int(input(a))
            return b
        except ValueError:
            print(translate("input_int"))


def mark_done(id):
    with sqlite3.connect(pathdb) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM habit_logs WHERE habit_id = ? AND log_date = date('now');", (id,))
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO habit_logs (habit_id, log_date) VALUES (?, date('now'))", (id,))
            cursor.execute("UPDATE habits SET streak = streak + 1 WHERE id = ?", (id,))
        else:
            print(translate('done'))
    


def add_habit():
    clear()
    name = input(translate("add_habit"))
    with sqlite3.connect(pathdb) as connection:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO habits (name,streak)
                       VALUES (?,0)''', (name,))


def del_habit(id):
    with sqlite3.connect(pathdb) as connection:
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute("DELETE FROM habits WHERE id = ?", (id,))


def lst_habits():
    clear()
    with sqlite3.connect(pathdb) as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT habits.id, habits.name, habits.streak, habit_logs.log_date 
                        FROM habits 
                        LEFT JOIN habit_logs ON habits.id = habit_logs.habit_id AND habit_logs.log_date = date('now');''')
        habits = cursor.fetchall()
    if has_habits(habits):
        print(translate('list_clean'))
        return habits
    for num, habit in enumerate(habits,start=1):
        print(f"{num}. {habit[1]} | {translate('streak')} {habit[2]} | {'✅' if habit[3] != None else '❌'}")
    return habits


def get_done():
    clear()
    habits = lst_habits()
    if has_habits(habits):
        return
    try:
        index_us = int(input(translate('input_num')))
        if is_valid(habits, index_us):
            index = index_us - 1
            mark_done(habits[index][0])
        else:
            print(translate('inp_correct'))
    except ValueError:
        print(translate('input_int'))

def get_delete():
    clear()
    habits = lst_habits()
    if has_habits(habits):
        return
    try:
        index_us = int(input(translate('input_num')))
        if is_valid(habits, index_us):
            index = index_us - 1
            del_habit(habits[index][0])
        else:
            print(translate('inp_correct'))
    except ValueError:
        print(translate('inp_correct'))


def menu():
    print(translate("menu"))


def clear_db():
    clear()
    habits = lst_habits()
    if len(habits) > 0:
        with sqlite3.connect(pathdb) as connection:
            cursor = connection.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')
            cursor.execute('DELETE FROM habits')
            print(translate('clear'))


init_db()


print(translate("prin"))
while True:
    menu()
    sel = input_tr(translate("sel_menu"))
    if sel == 1:
        add_habit()
    elif sel == 2:
        get_delete()
    elif sel == 3:
        lst_habits()
    elif sel == 4:
        get_done()
    elif sel == 5:
        clear_db()
    elif sel == 6:
        clear()
        print(translate("bye"))
        break
