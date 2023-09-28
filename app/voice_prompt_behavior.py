from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from settings import Settings
import logging
import os
from flask import request


class voice_prompt_behavior:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.linkedid = request.args.get("linkedid")
        self.retry_count = int(request.args.get("retry_count"))
        self.audio = f"{Settings.get_config_param('wav_files_path')}/r_{self.linkedid}_{self.retry_count}.wav"
        self.api_key = Settings.get_config_param('key')
        credentials = creds.YandexCredentials(api_key=self.api_key,)
        configure_credentials(yandex_credentials=credentials)

    def wave_file_exists(self):
        if not os.path.exists(self.audio):  # Проверяем, существует ли файл
            return False
        if os.path.getsize(self.audio) < 500:  # Проверяем размер файла
            return False
        return True

    def excute(self) -> str:
        if not self.wave_file_exists():
            return ''
        model = model_repository.recognition_model()
        model.model = 'general'
        model.language = 'ru-RU'
        model.audio_processing_type = AudioProcessingType.Full
        result = model.transcribe_file(self.audio)
        self.logger.info(result)
        text = ''
        for c, res in enumerate(result):
            # text += res.normalized_text
            text += res.raw_text
        return text

# sox small_time.wav -r 8000 -b 16 -c 1 small_time_.wav