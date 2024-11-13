import re
from colorama import Fore, Style

def haiku(file_name, output_file_name):
    '''
    Функция принимает на вход файл, который содержит хайку(предполагается). Каждая строка трёхстишия разделена /.
    Считает число слогов в каждой строке и складывает эти числа в другой массив,
    после чего относительно него выносит решение хайку или нет.
    :param file_name: str - имя файла
    :return: void
    '''
    with open(file_name) as file, open(output_file_name, "w") as output_file:
        text_lines = file.readlines()
        pattern = r'[уеёыаоэяиюУЕЁЫАОЭЯИЮ]'

        for l in text_lines:
            haiku_strings = l.strip().split('/')
            count = []
            #считаем кол-во слогов в каждом трёхстишье
            for s in haiku_strings:
                matches = re.findall(pattern, s)
                count.append(len(matches))

            if len(count) != 3:
                output_file.write(l + "Не хайку, должно быть 3 строки.\n\n")
                print(Style.RESET_ALL + f"{haiku_strings}" + Fore.LIGHTRED_EX + "\nНе хайку, должно быть 3 строки.\n")
                continue

            if count == [5, 7, 5]:
                output_file.write(l + "Хайку!\n\n")
                print(Style.RESET_ALL + f"{haiku_strings}" + Style.RESET_ALL + Fore.GREEN + "\nХайку!\n")
            else:
                if count[0] != 5:
                    output_file.write(l + f"Не хайку. Должно быть 5 слогов в 1-ой строке, а в ней {count[0]}.\n\n")
                    print(Style.RESET_ALL + Fore.BLACK + f"{haiku_strings}\n" + Fore.LIGHTRED_EX + f"Не хайку. Должно быть 5 слогов в 1-ой строке, а в ней {count[0]}.\n")
                elif count[1] != 7:
                    output_file.write(l + f"Не хайку. Должно быть 7 слогов в 2-ой строке, а в ней {count[1]}.\n\n")
                    print(Style.RESET_ALL + Fore.BLACK + f"{haiku_strings}\n" + Fore.LIGHTRED_EX + f"Не хайку. Должно быть 7 слогов в 2-ой строке, а в ней {count[1]}.\n")
                elif count[2] != 5:
                    output_file.write(l + f"Не хайку. Должно быть 5 слогов в 3-ей строке, а в ней {count[2]}.\n\n")
                    print(Style.RESET_ALL + Fore.BLACK + f"{haiku_strings}\n" + Fore.LIGHTRED_EX + f"Не хайку. Должно быть 5 слогов в 3-ой строке, а в ней {count[2]}.\n")

haiku("haiku.txt", "test_haiku.txt")







