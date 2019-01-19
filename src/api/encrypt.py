from flask import request, Blueprint

from ..service.encrypt import encrypt_image_to_png
from ..util.file_utils import get_filename
from ..util.message_utils import get_max_message
from ..util.response_wrapper import wrap_as_json, wrap_as_file

encrypt = Blueprint('encrypt', __name__)


@encrypt.route('/encrypt', methods=['POST'])
def encrypt_file():
    if 'file' not in request.files:
        return wrap_as_json({'error': 'File not present'}, 400)
    if 'message' not in request.form:
        return wrap_as_json({'error': 'Message not present'}, 400)

    file = request.files['file']
    message = request.form['message']
    filename = get_filename(file)

    return wrap_as_file(encrypt_image_to_png(file, get_max_message(file, message)), filename)
