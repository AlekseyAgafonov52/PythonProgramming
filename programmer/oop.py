class Programmer:

    def __init__(self, name, position):
        '''
        Инициализирует программиста с именем и должностью
        :param name: str
        :param position: str
        '''
        self.name = name
        self.position = position
        self.work_time = 0
        self._salary_per_hour = self.calc_salary()
        self._nakop = 0
        self.actions = [f"Утверждён на должность {self.position}"]

    def calc_salary(self):
        '''
        Возвращает зп в час в зависимости от должности
        :return: int
        '''
        if self.position == "Junior":
            return 10
        elif self.position == "Middle":
            return 15
        elif self.position == "Senior":
            return 20
        else:
            print("некорректная должность")
            return 0

    def work(self, time):
        '''
        Добавление к рабочему времени и к накопу, запись в статистику
        :return void
        '''
        self.work_time += time
        self._nakop += self._salary_per_hour * time
        self.actions.append(f"Работал {time} часов")

    def bonus(self, amount):
        '''
        Добавление к накопу, запись в статистику
        :return void
        '''
        if amount <= 0:
            print("Премия должна быть положительной")
        self._nakop += amount
        self.actions.append(f"Получена премия в размере {amount}")

    def rise(self):
        '''
        Повышение в должности и увеличение зп в час, запись в статистику
        :return void
        '''
        if self.position == "Junior":
            self.position = "Middle"
            self._salary_per_hour = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self._salary_per_hour = 20
        elif self.position == "Senior":
            self._salary_per_hour += 1
        self.actions.append(f"Повышен в должности до {self.position}, теперь зп в час {self._salary_per_hour}")

    def salary(self):
        '''
        Выдаёт накоп и обнуляет его и рабочие часы
        :return int
        '''
        if self._nakop < 0:
            print("Нечего выдавать")
        money = self._nakop
        self.actions.append(f"Получена накопленная зп в размере {money} тгр")
        self._nakop = 0
        self.work_time = 0
        return money

    def info(self):
        '''
        Информация для бухгалтерии
        :return void
        '''
        return f"{self.name} {self.work_time} ч. {self._salary_per_hour} тгр."

    def stat(self):
        '''
        Выводит Имя, Должность и отчёт о карьере
        :return void
        '''
        print(f"{self.name} {self.position}")
        for i in range(0, len(self.actions)):
            print(f"{i+1}) " + self.actions[i])


programmer = Programmer("Вася Пупкин", "Junior")
programmer.work(10)
print(programmer.info())
programmer.salary()
programmer.rise()
programmer.work(20)
print(programmer.info())
programmer.salary()
programmer.rise()
programmer.work(30)
print(programmer.info())
programmer.salary()

programmer.stat()
