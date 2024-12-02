from enigma.RotaryBlock import RotaryBlock

def encode_input(input, encoder):
    output = []
    for i in range(0, len(input)):
        output.append(encoder.encode(input[i]))
    return ''.join(output)

encoder = RotaryBlock()
msg = input("Введите, что хотите зашифровать: ")
offset_a = int(input("Введите сдвиг для 1-го ротора: "))
offset_b = int(input("Введите сдвиг для 2-го ротора: "))
offset_c = int(input("Введите сдвиг для 3-го ротора: "))


encoder.set_offset(offset_a, offset_b, offset_c)
encoded_str = encode_input(msg.upper(), encoder)
print(f"Зашифрованное сообщение: {encoded_str}")

encoder.set_offset(offset_a, offset_b, offset_c)
print(f"Расшифрованное сообщение: {encode_input(encoded_str, encoder)}")




