import json
import logging

class Settings:
    config_dict = {}
    crm_user_cache = {}
    logger = None

    @staticmethod
    def load_config():
        with open('.settings.json') as file:
            Settings.config_dict = json.load(file)
        Settings.logger.info(Settings.config_dict)


    @staticmethod
    def get_asterisk_server_ip() -> str:
        return Settings.config_dict['asterisk_server_ip']
    
    @staticmethod
    def get_api_key() -> str:
        return Settings.config_dict['key']
    
    @staticmethod
    def get_wav_files_path() -> str:
        return Settings.config_dict['wav_files_path']
    
    @staticmethod
    def get_logger():
        return Settings.logger
    
    