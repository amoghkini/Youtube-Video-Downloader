from typing import Union

from common.execution_env import ExecutionEnv
from config.config import get_server_config, DevConfig, TestingConfig, ProdConfig

class Utils:

    
    @staticmethod
    def get_execution_env() -> str:
        """
        Get the execution environment.

        Returns:
        - str: The environment in which the code is executed.
        """
        return get_server_config().get('env')        
        

    @staticmethod
    def get_config() -> Union[DevConfig, TestingConfig, ProdConfig, None]:
        """
        Get the appropriate configuration based on the execution environment.

        Returns:
        - BaseConfig or None: The configuration object based on the environment,
          or None if the environment is not recognized.
        """
        env = Utils.get_execution_env()
        if env == ExecutionEnv.DEV:
            return DevConfig()
        elif env == ExecutionEnv.TEST:
            return TestingConfig()
        elif env == ExecutionEnv.PROD:
            return ProdConfig()
        else:
            return None
    
    @staticmethod
    def get_log_dir() -> str:
        """
        Get the directory for log files.

        Returns:
        - str: The directory path for log files.
        """
        return get_server_config().get('logFileDir')