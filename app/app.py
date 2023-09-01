from check_wav_file import check_patterns
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, abort
from settings import Settings
from ip_access_checker import IPAccessChecker
Settings.load_config()

app = Flask(__name__)

handler = RotatingFileHandler(
    '/var/log/yaspeechkitwrapper.log', maxBytes=200*1024*1024, backupCount=10)
formatter = logging.Formatter('[%(asctime)s][%(name)s] => %(message)s')
handler.setFormatter(formatter)
logging.basicConfig(handlers=[handler], level=logging.INFO)
logger = logging.getLogger('yandex speech kit wrapper app')
Settings.logger = logger
logger.info("Start worker...")


@app.before_request
def log_request():
    """Log incoming requests."""
    log_str = f"[{request.headers.get('X-Forwarded-For', request.remote_addr)}] "
    log_str += f"[{request.path}] "
    log_str += f"[{str(request.args)}] "
    log_str += f"[{request.get_data(as_text=True)}] "
    logger.info(log_str)


@app.after_request
def log_response(response):
    """Log outgoing responses."""
    log_str = f"[{request.headers.get('X-Forwarded-For', request.remote_addr)}] "
    log_str += f"[{request.path}] => "
    log_str += f"[{response.status}] "
    log_str += f"Response Body: {response.get_data(as_text=True)}"
    log_str += f"Request status: {response.status}"
    logger.info(log_str)
    return response


@app.route('/check_wav_file/<string:key>')
def download(key):
    IPAccessChecker.check_access()
    return check_patterns(key)

# Обработчик для неопределенных маршрутов


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def unqnown_request(path):
    abort(403, "Access denied")
