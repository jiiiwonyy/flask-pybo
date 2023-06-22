from config.default import *

SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=b'\xf89!\xb1m\xfb3\x98\x96\xba\xc6\x12\xbb5\xe6B'