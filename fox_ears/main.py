import logging

from fox_ears.config.config import Config
from fox_ears.services.wake_up_service import WakeUpService
from fox_ears.routers.general_api import GeneralAPI

cfg: Config = Config.get_instance()

logl_lvls = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING
}

logging.basicConfig(level=logl_lvls[cfg.log_lvl])

################ ROUTERS ################

general_api = GeneralAPI(cfg)

######## MAIN ########


def main():
    wake_up_service = WakeUpService(cfg)
    wake_up_service()


if __name__ == '__main__':
    main()
