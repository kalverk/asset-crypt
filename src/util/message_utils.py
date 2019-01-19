from PIL import Image
from stegano import tools


def get_max_message(input_image, message, encoding: str = 'UTF-8'):
    message = message + ' '

    img = Image.open(input_image)
    width, height = img.size
    n_pixels = width * height

    message_length = len(message)
    calc_message = str(message_length) + ":" + str(message)
    message_bits = "".join(tools.a2bits_list(calc_message, encoding))
    message_bits += '0' * ((3 - (len(message_bits) % 3)) % 3)

    len_message_bits = len(message_bits)

    max_len = n_pixels * 3
    return message * (max_len // len_message_bits)
