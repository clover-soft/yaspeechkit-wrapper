import json
import logging
from typing import Any


class Settings:
    config_dict = {}
    crm_user_cache = {}

    @staticmethod
    def load_config():
        with open('.settings.json') as file:
            Settings.config_dict = json.load(file)

    @staticmethod
    def get_config_param(param):
        if param in Settings.config_dict:
            return Settings.config_dict[param]
        return None
    