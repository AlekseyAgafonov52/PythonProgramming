

class CharUtil():
    @staticmethod
    def char_to_int(in_character):
        """
        Превращает символ в число
        :param in_character: char
        :return: int
        """
        in_character = in_character.upper()
        return ord(in_character) - 65

    @staticmethod
    def int_to_char(number):
        """
        Превращает число в символ
        :param number: int
        :return: char
        """
        return chr(number + 65)

