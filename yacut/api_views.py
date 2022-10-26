from flask import jsonify, request

from . import app, db
from .constants import MATCH
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .utils import get_unique_short_id, check_original
from http import HTTPStatus


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_link(short_id):
    target: str = check_original(short_id)
    if not target:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': target}), HTTPStatus.OK


@app.route('/api/id/', methods=('POST',))
def push_link():
    data: dict[str, str] = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if not data.get('custom_id'):
        data.update({'custom_id': get_unique_short_id()})

    if not MATCH.search(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    if check_original(data['custom_id']):
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')

    short = URL_map()
    short.from_dict(data)
    db.session.add(short)
    db.session.commit()
    return jsonify(short.to_dict()), HTTPStatus.CREATED
