from pathlib import Path

from werkzeug import secure_filename


def get_filename(file):
    return secure_filename(file.filename)


def get_extension(file_path):
    return Path(file_path).suffix.lower()
