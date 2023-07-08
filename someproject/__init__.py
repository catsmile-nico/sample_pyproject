# Logging configurations
import logging.config
import yaml

with open('./someproject/logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

from someproject import Modules
from someproject import App