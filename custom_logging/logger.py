import logging.config
import yaml
import os

def setup_logger():
    config_path = os.path.join(os.path.dirname(__file__), "loggerconfig.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("app_logger")
setup_logger()

