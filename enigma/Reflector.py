class Reflector:
    def __init__(self):
        """
        Создание рефлектора
        """
        self.map_reflector = {'A': 'Q', 'B': 'Y', 'C': 'H', 'D': 'O', 'E': 'G', 'F': 'N', 'G': 'E', 'H': 'C', 'I': 'V',
                              'J': 'P', 'K': 'U', 'L': 'Z', 'M': 'T', 'N': 'F', 'O': 'D', 'P': 'J', 'Q': 'A', 'R': 'X',
                              'S': 'W', 'T': 'M', 'U': 'K', 'V': 'I', 'W': 'S', 'X': 'R', 'Y': 'B', 'Z': 'L'}

    def encode(self, in_char):
        """
        Отражение символа в рефлекторе
        :param in_char: char
        :return: char
        """
        return self.map_reflector.get(in_char)

