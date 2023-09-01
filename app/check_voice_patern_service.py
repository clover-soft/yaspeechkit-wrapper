from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from settings import Settings
import logging
import time
from flask import request, abort


logger = logging.getLogger("yandex speech kit wrapper app")


def recognize(audio):
    model = model_repository.recognition_model()

    # Задайте настройки распознавания.
    model.model = 'general'
    model.language = 'ru-RU'
    model.audio_processing_type = AudioProcessingType.Full

    # Распознавание речи в указанном аудиофайле и вывод результатов в консоль.
    result = model.transcribe_file(audio)
    logger.info(result)
   #  for c, res in enumerate(result):
   #      logger.info(res.raw_text)


def check_voice_pattern():
    linkedid = request.args.get("linkedid")
    retry_count = request.args.get("retry_count")
    filename = f"{Settings.get_wav_files_path()}/{linkedid}_{retry_count}.wav"
    force_agree_patterns = Settings.get_force_agree_patterns()
    agree_patterns = Settings.get_agree_patterns()
    disagree_patterns = Settings.get_disagree_patterns()
    max_session_time = Settings.get_max_session_time()
    call_time = int(linkedid.split(".")[0])
    # Аутентификация через API-ключ.
    configure_credentials(yandex_credentials=creds.YandexCredentials(api_key=Settings.get_api_key(),)
                          )
    recognize(filename)
    return "repeat"
