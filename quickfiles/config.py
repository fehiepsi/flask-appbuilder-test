import os

# get the directory which running the script
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True # not important
SECRET_KEY = "abc"

# use sqlite as a default link
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
}

UPLOAD_FOLDER = os.path.join(basedir, "app/static/uploads/")
IMG_UPLOAD_FOLDER = os.path.join(basedir, "app/static/uploads/")
IMAGE_UPLOAD_URL = "/static/uploads/"
FILE_ALLOWED_EXTENSIONS = ("txt", "pdf", "jpeg", "jpg", "gif", "png")
AUTH_TYPE = 1
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "App to upload files"
APP_THEME = "" # default
