from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

#라우팅 함수 추가
@bp.route('/')
def index():
    return redirect(url_for('question._list'))

