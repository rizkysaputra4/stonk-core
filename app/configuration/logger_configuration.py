import logging
import logging.config
import os

import yaml


def init_log_config():
    # Initialize the logger once as the application starts up.
    d = os.getcwd()+"/app/resource/"
    with open(d+"logging.yaml", 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

    # Get an instance of the logger and use it to write a log!
    # Note: Do this AFTER the config is loaded above or it won't use the config.
    logger = logging.getLogger(__name__)
    logger.info("Configured the logger!")

