import io

from stegano import lsb


def encrypt_image_to_png(file, message):
    output_bytes = io.BytesIO()
    bytes_image = lsb.hide(file, message)
    bytes_image.save(output_bytes, 'png')
    output_bytes.seek(0)
    return output_bytes
