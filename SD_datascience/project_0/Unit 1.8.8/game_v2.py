"""Игра "Угадай число".
Компьютер сам загадывает и сам угадывает число.
Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
Алгоритм справляется с угадыванием меньше чем за 20 попыток.
"""


import numbers
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число. Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Local variables:
        rand_start (int): Настройка начала списка поиска загаданного значения. Defaults to 1.
        rand_end (int): Настройка конца списка поиска загаданного значения. Defaults to 101.

    Returns:
        int: Число попыток
    """
   
    count = 0
    
    rand_start = 1 # начало списка угадываемых чисел
    rand_end = 101 # конец списка угадываемых чисел
    
    while True:
        count += 1
        
        predict_number = np.random.randint(rand_start, rand_end) # предполагаемое число (уточнение кода относительно базовой версии для увеличения производительности)
        
        # Настройка алгоритма угадывания загаданного числа
        if number < predict_number:
            rand_end = predict_number
        if number > predict_number:
            rand_start = predict_number

        if number == predict_number:
            break  # выход из цикла если угадали

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array[1:101]:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)