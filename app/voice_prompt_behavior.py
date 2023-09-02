from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from settings import Settings
import logging
import time
from flask import request, abort


class voice_prompt_behavior:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.linkedid = request.args.get("linkedid")
        self.retry_count = request.args.get("retry_count")
        self.audio = f"{Settings.get_config_param('wav_files_path')}/{self.linkedid}_{self.retry_count}.wav"
        self.force_agree_patterns = Settings.get_config_param('force_agree_patterns')
        self.agree_patterns = Settings.get_config_param('agree_patterns')
        self.disagree_patterns = Settings.get_config_param('disagree_patterns')
        self.max_session_time = Settings.get_config_param('max_session_time')
        self.max_retry_count = Settings.get_config_param('max_retry_count')
        self.call_time = int(self.linkedid.split(".")[0])
        self.session_time = time.time() - self.call_time
        credentials = creds.YandexCredentials(api_key=Settings.get_config_param('api_key'),)
        configure_credentials(yandex_credentials=credentials)

    def get_behavior(self) -> str:
        model = model_repository.recognition_model()
        model.model = 'general'
        model.language = 'ru-RU'
        model.audio_processing_type = AudioProcessingType.Full
        result = model.transcribe_file(self.audio)
        def getNextPattern(patterns_list,text,pattern_layer):
            nextPattern = next((pattern for pattern in patterns_list if pattern in text), None)
            if nextPattern is not None:
                self.logger.info(f"Found {pattern_layer} pattern: {nextPattern}")
                return True
            return False
        for c, res in enumerate(result):
            if getNextPattern(self.force_agree_patterns, res.raw_text, 'force_agree'):
                return 'connect'
            elif getNextPattern(self.disagree_patterns, res.raw_text, 'disagree'):
                return 'disconnect'
            elif getNextPattern(self.agree_patterns, res.raw_text, 'agree'):
                return 'connect'
        if self.session_time > self.max_session_time:
            self.logger.info("Session time over")
            return 'disconnect'
        if self.retry_count >= self.max_session_time:
            self.logger.info("Retry count over")
            return 'disconnect'
        return 'repeat'
