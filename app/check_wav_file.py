from speechkit import model_repository, configure_credentials, creds
from speechkit.stt import AudioProcessingType
from settings import Settings
logger = Settings.get_logger()
# Аутентификация через API-ключ.
configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key=Settings.get_api_key(),
   )
)

def recognize(audio):
   model = model_repository.recognition_model()

   # Задайте настройки распознавания.
   model.model = 'general'
   model.language = 'ru-RU'
   model.audio_processing_type = AudioProcessingType.Full

   # Распознавание речи в указанном аудиофайле и вывод результатов в консоль.
   result = model.transcribe_file(audio)
   for c, res in enumerate(result):
      logger.info(res.raw_text)
    
def check_patterns(key):
   params = key.split("_")
   filename = f"{Settings.get_wav_files_path}/{params[0]}.wav"
   try_count = int(params[1])
   logger.info(Settings.get_api_key)
   recognize(filename)
   return "repeat"

