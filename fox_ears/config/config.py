from dataclasses import dataclass


@dataclass
class Config:
    _instance = None

    def __init__(self):
        self.log_lvl = "INFO"

    def get_instance():
        if Config._instance == None:
            Config._instance = Config()

        return Config._instance

    log_lvl: str
