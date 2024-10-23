import yaml

def load_questions(filename):
    """
    Функция загружает вопросы из YAML файла.
    :param filename: имя файла с вопросами.
    :return: список вопросов.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def ask_question(question_dict):
    """
    Задаёт вопрос пользователю и проверяет его ответ.
    :param question_dict: словарь с данными о вопросе (вопрос, варианты, правильный ответ).
    :return: возвращает True, если ответ правильный, иначе False.
    """
    print(question_dict["question"])
    for index, ans in enumerate(question_dict["answers"]):
        index = index + 1
        print(str(index) + ") " + str(ans))

    # получаем выбор пользователя
    while True:
        try:
            user_answer = int(input("Введите номер варианта: "))
            user_answer = user_answer - 1               # -1 т.к. в yaml нумерация с 0
            if 0 <= user_answer < len(question_dict["answers"]):
                break
            else:
                print("Пожалуйста, введите допустимый номер варианта.")
        except ValueError:
            print("Ошибка: введите целое число.")

    # проверяем правильный ли ответ
    return user_answer == question_dict["correct_answer"]

def run_quiz():
    """
    Основная функция для запуска викторины.
    """
    questions = load_questions("questions.yaml")
    correct_count = 0
    incorrect_count = 0

    for question_dict in questions:
        if ask_question(question_dict):
            print("Правильно!\n")
            correct_count += 1
        else:
            print("Неправильно. Правильный ответ: " + question_dict['answers'][question_dict['correct_answer']] + "\n")
            incorrect_count += 1

    # выводим результат
    print("Тест завершен.\nПравильных ответов:" + str(correct_count) + "\nНеправильных ответов:" + str(incorrect_count))

def main():
    run_quiz()

main()
