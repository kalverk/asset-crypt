from flask import request, Blueprint

from ..service.decrypt import decrypt_message_from_file
from ..util.response_wrapper import wrap_as_json

decrypt = Blueprint('decrypt', __name__)


@decrypt.route('/decrypt', methods=['POST'])
def decrypt_file():
    if 'file' not in request.files:
        return wrap_as_json({'error': 'File not present'}, 400)

    file = request.files['file']
    return wrap_as_json({'message': decrypt_message_from_file(file)}, 200)
