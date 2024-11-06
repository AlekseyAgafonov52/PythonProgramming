import time
from threading import Thread
from colorama import Fore, Back, Style
import chime

def input_num_of_timers():
    """
    Функция запрашивает у пользователя кол-во таймеров и возвращает это число.

    :return: int - кол-во таймеров
    """
    while True:
        try:
            numbers_t = int(input("Вы можете задать максимум 10 таймеров.\nСколько таймеров нужно?\n"))
            if 1 <= numbers_t <= 10:
                return numbers_t
            else:
                print("Некорректный ввод. Введите число от 1 до 10.")
        except ValueError:
            print("Ошибка: введите целое число.")


def input_timer_intervals(numbers_t):
    """
    Функция запрашивает у пользователя кол-во секунд для каждого таймера и возвращает список интервалов.

    :param numbers_t: int - кол-во таймеров
    :return: list[int] - массив интервалов для каждого таймера
    """
    arr_seconds = []
    for i in range(1, numbers_t + 1):
        while True:
            try:
                seconds = int(input(f"Введите время (в секундах) для таймера {i}:\n"))
                if seconds > 0:
                    arr_seconds.append(seconds)
                    break
                else:
                    print("Время должно быть больше 0.")
            except ValueError:
                print("Ошибка: введите целое число.")
    return arr_seconds


def timer(seconds, timer_id):
    """
    Функция запускает таймер на заданное количество секунд.

    :param seconds: int - количество секунд для таймера
    :param timer_id: int - идентификатор таймера
    """
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.BLUE + f"Таймер {timer_id} запущен на {seconds} секунд.")
    time.sleep(seconds)
    print(Fore.LIGHTRED_EX + Style.BRIGHT + Back.BLACK + f"Таймер {timer_id} сработал!")
    chime.theme('mario')
    chime.info(sync=True, raise_error=False)


def threads_t():
    '''
    Функция запускает несколько(от 1 до 10) таймеров одновременно
    '''
    threads = []
    for i in range(0, numbers_t):
        t = Thread(target=timer, args=(arr_seconds[i], i + 1))  # Передаем i+1 как идентификатор таймера
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Ожидаем завершения всех таймеров


if __name__ == "__main__":
    numbers_t = input_num_of_timers()
    arr_seconds = input_timer_intervals(numbers_t)
    print("Количество таймеров:", numbers_t)
    print("Интервалы для таймеров:", arr_seconds)
    threads_t()
