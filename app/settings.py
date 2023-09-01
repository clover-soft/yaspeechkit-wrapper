import json
import logging

class Settings:
    config_dict = {}
    crm_user_cache = {}

    @staticmethod
    def load_config():
        with open('.settings.json') as file:
            Settings.config_dict = json.load(file)


    @staticmethod
    def get_asterisk_server_ip() -> str:
        return Settings.config_dict['asterisk_server_ip']
    
    @staticmethod
    def get_api_key() -> str:
        if "key" not in Settings.config_dict:
            return "sdfdfsfd"
        return Settings.config_dict['key']
    
    @staticmethod
    def get_wav_files_path() -> str:
        return Settings.config_dict['wav_files_path']
    
    @staticmethod
    def get_max_session_time() -> int:
        return Settings.config_dict['max_session_time']
    
    @staticmethod
    def get_force_agree_patterns() -> list:
        return Settings.config_dict['force_agree_patterns']
    
    @staticmethod
    def get_agree_patterns() -> list:
        return Settings.config_dict['agree_patterns']
    
    @staticmethod
    def get_disagree_patterns() -> list:
        return Settings.config_dict['force_patterns']
    
    