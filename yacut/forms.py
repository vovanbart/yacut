from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp
from .constants import PATTERN_LINK


class ShortURLForm(FlaskForm):
    original_link = URLField(
        'Вставьте URL',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Некорректная ссылка')
        )
    )
    custom_id = StringField(
        validators=(
            Length(1, max=16),
            Regexp(
                regex=PATTERN_LINK,
                message='В сокращенние присутствуют недопустимые символы'
            ),
            Optional()
        )
    )
    submit = SubmitField('Создать')
