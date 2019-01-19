import json

from flask import send_file, Response

from .file_utils import get_extension


def wrap_as_json(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )


def wrap_as_file(binary, filename):
    switcher = {
        '.jpg': wrap_as_jpg,
        '.jpeg': wrap_as_jpeg,
        '.png': wrap_as_png
    }
    return switcher.get(get_extension(filename), wrap_as_binary)(binary, filename)


def wrap_as_jpg(binary, filename):
    return wrap_as_generic_file(binary, 'image/jpg', filename)


def wrap_as_jpeg(binary, filename):
    return wrap_as_generic_file(binary, 'image/jpeg', filename)


def wrap_as_png(binary, filename):
    return wrap_as_generic_file(binary, 'image/png', filename)


def wrap_as_binary(binary, filename):
    return wrap_as_generic_file(binary, 'application/binary', filename)


def wrap_as_generic_file(binary, content_type, filename):
    return send_file(
        binary,
        mimetype=content_type,
        as_attachment=True,
        attachment_filename=filename
    )
