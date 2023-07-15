import math
import uuid
import time
import logging
import calendar
from datetime import datetime, timedelta
from flask import url_for
from typing import Dict

from common.execution_env import ExecutionEnv
from config.config import get_server_config, DevConfig, TestingConfig, ProdConfig

class Utils:

    date_format = "%Y-%m-%d"
    time_format = "%H:%M:%S"
    date_time_format = "%Y-%m-%d--%H-%M-%S"


    @staticmethod
    def round_off(price: int) -> int:  # Round off to 2 decimal places
        return round(price, 2)

    @staticmethod
    def get_epoch(datetime_obj=None):
        # This method converts given datetime_obj to epoch seconds
        if datetime_obj == None:
            datetime_obj = datetime.now()
        epoch_seconds = datetime.timestamp(datetime_obj)
        return int(epoch_seconds)  # converting double to long

    @staticmethod
    def get_time_of_day(hours, minutes, seconds, date_time_obj=None):
        if date_time_obj == None:
            date_time_obj = datetime.now()
        date_time_obj = date_time_obj.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        return date_time_obj

    @staticmethod
    def get_time_of_today(hours, minutes, seconds):
        return Utils.get_time_of_day(hours, minutes, seconds, datetime.now())

    @staticmethod
    def get_today_date_str(time=False):
        if time == True:
            return Utils.convert_to_date_time_str(datetime.now())
        else:
            return Utils.convert_to_date_str(datetime.now())

    @staticmethod
    def convert_to_date_str(datetime_obj):
        return datetime_obj.strftime(Utils.date_format)
    
    @staticmethod
    def convert_to_date_time_str(datetime_obj):
        return datetime_obj.strftime(Utils.date_time_format)

    @staticmethod
    def get_execution_env() -> str:
        env =  get_server_config().get('env')        
        return env

    @staticmethod
    def get_config():
        env = Utils.get_execution_env()
        if env == ExecutionEnv.DEV:
            config = DevConfig()
        elif env == ExecutionEnv.TEST:
            config = TestingConfig()
        elif env == ExecutionEnv.PROD:
            config = ProdConfig()
        else:
            config = None
        return config
    
    @staticmethod
    def get_log_dir():
        return get_server_config().get('logFileDir')

    @staticmethod
    def get_mismatches_from_two_dict(dict1: Dict, 
                                     dict2: Dict, 
                                     result_dict: int = 1) -> Dict:
        # Currently the dictionary which fetches the data from db contains all the fields. For optimaziation, we should fetch the fields which are in scope of my profile page.
        return_dict = dict()
        mismatches = dict(dict1.items() ^ dict2.items())
        for i in mismatches.keys():
            return_dict[i] = dict1.get(i) if result_dict == 1 else dict2.get(i)
        
        return_dict = {keys: values for keys, values in return_dict.items() if values is not None}
        return return_dict

    @staticmethod
    def get_external_url(api_name: str, args=None) -> str:
        if args and 'token' in args:
            return url_for(api_name, token=list(args.values())[0], _external=True)
        return url_for(api_name, _external=True)
