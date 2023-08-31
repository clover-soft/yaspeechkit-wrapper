import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, abort
app = Flask(__name__)

handler = RotatingFileHandler('/var/log/yaspeechkitwrapper.log', maxBytes=200*1024*1024, backupCount=10)
formatter = logging.Formatter('[%(asctime)s][%(name)s] => %(message)s')
handler.setFormatter(formatter)
logging.basicConfig(handlers=[handler], level=logging.INFO)
logger = logging.getLogger('yandex speech kit wrapper app')
logger.info("Start worker...")

# Обработчик для неопределенных маршрутов
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def unqnown_request(path):
    abort(403, "Access denied")