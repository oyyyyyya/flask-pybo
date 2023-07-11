from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}' .format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMT_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xfd\xf6\xf9g\xc7\xc75\xd16,\xe9Q}\x1e\xbf+'