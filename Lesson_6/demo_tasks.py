"""
Створіть словник з інформацією про пошукові системи,
в якому ключі – назви пошукових систем, а значення –
частка їхнього використання у світі на даний момент (дійсне число).
Надрукуйте елементи словника як у вихідних даних.
Елементи у словнику невпорядковані.
"""


def task_1():
    search_systems = {
        'Yahoo!': 2.09,
        'Google': 90.15,
        'Bing': 3.23,
        'Baidu': 2.2
    }
    print(search_systems)


"""
Припустимо, що у нас є словник, в якому ключі є ідентифікаторами,
а значення – іменами користувачів. Напишіть програму, 
яка виводить вітальне повідомлення користувачу на основі його ідентифікатора.
Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.
"""


def task_2():
    users = {
        1: "Mariia",
        2: "Ihor",
        3: "Petro"
    }
    input_message = input("Enter user id: ")

    if users.get(int(input_message)):
        print(f"Hi {users[int(input_message)]}")
    else:
        print("Hi all")


"""
Ви створюєте пригодницьку гру і використовуєте для зберігання предметів гравця словник, 
у якому ключі - це назви предметів, значення - кількість одиниць кожної із речей. 
Виведіть повідомлення про усі речі гравця як у вихідних даних.
"""


def task_3():
    equipment = {
        'key':  3,
        'mace': 1,
        'gold': 24,
        'lantern': 1,
        'stone': 10
    }
    print(f"Total number of things: {sum(equipment.values())}")


"""
Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. 
Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». 
Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.
"""


def task_4():
    movies = {
        'Avengers: Endgame': 2019,
        'Thor': 2011,
        'Guardians of the Galaxy': 2014,
        'Iron Man': 2008
    }
    # by key
    sorted_films = dict(sorted(movies.items()))
    print(sorted_films)
    # by value
    print(dict(sorted(movies.items(), key=lambda item: item[1])))


"""
Напишіть програму для сортування за спаданням (порядок, зворотний алфавітному) словника за ключами. 
Словник зберігає пари ключ-значення у вигляді «країна: столиця». 
Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами країн.
"""


def task_5():
    countries = {
        'Ukraine': 'Kyiv',
        'France': 'Paris',
        'Canada': 'Ottawa',
        'Denmark': 'Copenhagen',
        'China': 'Beijing',
    }
    print(sorted(countries.items(), reverse=True))


"""
Надрукуйте елементи словника, де ключі - це числа від 1 до n (обидва числа включно),
а значення - квадрати ключів. n – ціле число, яке вводить користувач.
"""


def task_6(n: int):
    generated_dict = {x: x*x for x in range(1, n+1)}
    print(generated_dict)


"""
Напишіть програму, яка приймає рядок символів, і обчислює кількість великих та малих літер.
"""


def task_7(text: str):
    results = {}
    results["upper case"] = sum(1 for char in text if char.isupper())
    results["lower case"] = sum(1 for char in text if char.islower())
    print(results)


"""
Напишіть програму для видалення дублікатів зі списку цілих чисел.
"""


def task_8(numbers):
    print(list(set(numbers)))


"""
Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.
"""

def task_9(list_1, list_2):
    list_1_to_set = set(list_1)
    list_2_to_set = set(list_2)
    unique = list_1_to_set.symmetric_difference(list_2_to_set)
    print(unique)
    return len(unique)


def char_count(input_text: str) -> dict():
    results = {}
    results['upper case'] = sum(1 for x in input_text if x.isupper())
    results['lower case'] = sum(1 for x in input_text if x.islower())
    return  results