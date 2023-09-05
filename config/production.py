from config.default import *

SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=b'\xd8U\xf0\xa2\xf8\xd3\x06\rs\xb0a\x95}\x9fW\xb2'