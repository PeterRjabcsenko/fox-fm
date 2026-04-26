import logging
from time import time

from fox_ears.config.config import Config


class WakeUpService:
    def __init__(self, cfg: Config):
        self.logger = logging.getLogger("Wake Up Service")
        self.info = self.logger.isEnabledFor(logging.INFO)

        if self.info:
            time_init = time()

        self.cfg = cfg

        if self.info:
            self.logger.info(f"initialized ({time() - time_init:.2f}s)")
