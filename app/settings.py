import json


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
    
    