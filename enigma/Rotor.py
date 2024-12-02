from CharUtil import CharUtil
class Rotor:

    offset = int()

    def __init__(self, input_map, notch):
        self.connections = input_map
        self.notch = notch
        self.reversed_connections = self.reverse_connections(self.connections)

    @staticmethod
    def reverse_connections(my_map):
        reversed_map = {v: k for k, v in my_map.items()}
        return reversed_map

    def encode_forward(self, in_char):
        """
        Прямое шифрование символа
        :param in_char: char
        :return: char
        """
        encoded = self.connections.get(in_char)
        return CharUtil.int_to_char( (CharUtil.char_to_int(in_character=encoded) + self.offset) % 26 )

    def encode_backward(self, in_char):
        """
        Обратное шифрование символа
        :return: char
        """
        char_num = CharUtil.char_to_int(in_char) - (self.offset % 26)

        if char_num < 0:
            char_num = CharUtil.char_to_int(in_char) - (self.offset % 26) + 26

        result = self.reversed_connections.get(CharUtil.int_to_char(char_num))
        return result

    def is_notched_offset(self):
        """
        Проверяет, находится ли ротор в положении засечки.
        :return: bool
        """
        return self.offset % 26 == self.notch

    def rotate(self):
        """
        Поворачивает ротор на 1 шаг
        :return: void
        """
        self.offset = self.offset + 1

    def set_offset(self, offset):
        """
        Устанавливает значение оффсета
        :param offset: long
        :return: void
        """
        self.offset = offset

    def to_screen(self):
        print(self.connections)


