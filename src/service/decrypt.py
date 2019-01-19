from stegano import lsb


def decrypt_message_from_file(file):
    return lsb.reveal(file)
