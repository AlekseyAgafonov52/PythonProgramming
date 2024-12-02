from enigma.Rotor import Rotor
from enigma.RotorFactory import RotorFactory
from enigma.Reflector import Reflector


class RotaryBlock:
    def __init__(self):
        """
        Инициализирует роторы и рефлектор
        :param rotor_1: Rotor
        :param rotor_2: Rotor
        :param rotor_3: Rotor
        :param reflector: Reflector
        """
        self.rotor1 = RotorFactory.rotor_a()
        self.rotor2 = RotorFactory.rotor_b()
        self.rotor3 = RotorFactory.rotor_c()
        self.reflector = Reflector()

    def set_offset(self, offset_a, offset_b, offset_c):
        """
        Устанавливает оффсеты
        :param offset_a: int
        :param offset_b: int
        :param offset_c: int
        :return:
        """
        self.rotor1.set_offset(offset_a)
        self.rotor2.set_offset(offset_b)
        self.rotor3.set_offset(offset_c)

    def encode(self, input_char):
        """
        Реализует сам механизм шифрования при проходе через все три ротора и обратно через рефлектор.
        :param in_char: char
        :return: char
        """
        encoded_1_fwd = self.rotor1.encode_forward(input_char)
        encoded_2_fwd = self.rotor2.encode_forward(encoded_1_fwd)
        encoded_3_fwd = self.rotor3.encode_forward(encoded_2_fwd)
        encoded_reflector = self.reflector.encode(encoded_3_fwd)
        encoded_3_backward = self.rotor3.encode_backward(encoded_reflector)
        encoded_2_backward = self.rotor2.encode_backward(encoded_3_backward)
        encoded_1_backward = self.rotor1.encode_backward(encoded_2_backward)

        self.rotate()

        return encoded_1_backward

    def rotate(self):
        """
        Прокручивает 1-ый ротор. Потом проверяет если уже находится на нотче первый, то прокручиваем второй ротор.
        Тоже самое происходит с третьим ротором.
        :return: void
        """
        self.rotor1.rotate()
        if self.rotor1.is_notched_offset():
            self.rotor2.rotate()
            if self.rotor2.is_notched_offset():
                self.rotor3.rotate()
