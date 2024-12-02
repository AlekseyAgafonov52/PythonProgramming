from enigma.Rotor import Rotor

class RotorFactory:
    @staticmethod
    def rotor_a():
        return Rotor(input_map={'A': 'D', 'B': 'M', 'C': 'T', 'D': 'W', 'E': 'S', 'F': 'I', 'G': 'L', 'H': 'R', 'I': 'U',
                'J': 'Y', 'K': 'Q', 'L': 'N', 'M': 'K', 'N': 'F', 'O': 'E', 'P': 'J', 'Q': 'C', 'R': 'A', 'S': 'Z',
                'T': 'B', 'U': 'P', 'V': 'G', 'W': 'X', 'X': 'O', 'Y': 'H', 'Z': 'V'}, notch=2)

    @staticmethod
    def rotor_b():
        return Rotor(input_map={'A': 'H', 'B': 'Q', 'C': 'Z', 'D': 'G', 'E': 'P', 'F': 'J', 'G': 'T', 'H': 'M', 'I': 'O',
                    'J': 'B', 'K': 'L', 'L': 'N', 'M': 'C', 'N': 'I', 'O': 'F', 'P': 'D', 'Q': 'Y', 'R': 'A',
                    'S': 'W', 'T': 'V', 'U': 'E', 'V': 'U', 'W': 'S', 'X': 'R', 'Y': 'K', 'Z': 'X'}, notch=4)

    @staticmethod
    def rotor_c():
        return Rotor(input_map={'A': 'U', 'B': 'Q', 'C': 'N', 'D': 'T', 'E': 'L', 'F': 'S', 'G': 'Z', 'H': 'F', 'I': 'M',
                    'J': 'R', 'K': 'E', 'L': 'H', 'M': 'D', 'N': 'P', 'O': 'X', 'P': 'K', 'Q': 'I', 'R': 'B',
                    'S': 'V', 'T': 'Y', 'U': 'G', 'V': 'J', 'W': 'C', 'X': 'W', 'Y': 'O', 'Z': 'A'}, notch=7)
