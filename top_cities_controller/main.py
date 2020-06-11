#!/usr/bin/env python3

import os
import sys
import time
import logging
from top_cities_controller.top_cities_controller import TopCitiesController

from configparser import ConfigParser, NoSectionError, NoOptionError
import os.path

CONFIG_FILE = 'config/config.ini'

def parse_config_params():
    if os.path.isfile(CONFIG_FILE):
        return read_from_config_file()
    
    return read_from_env()

def read_from_config_file():
    config_params = {}

    configParser = ConfigParser()
    configParser.read(CONFIG_FILE)
            
    config_params["recv_queue"] = configParser.get('SETTINGS', 'RECV_QUEUE')
    config_params["send_queue"] = configParser.get('SETTINGS', 'SEND_QUEUE')

    return config_params

def read_from_env():
    config_params = {}

    try:
        config_params["recv_queue"] = os.environ["RECV_QUEUE"]
        config_params["send_queue"] = os.environ["SEND_QUEUE"]
    except KeyError as e:
        raise KeyError("Key was not found. Error: {}. Aborting server".format(e))
    except ValueError as e:
        raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))
    
    return config_params	

def main():
    config_params = parse_config_params()

    worker = TopCitiesController(
        config_params["recv_queue"],
        config_params["send_queue"]
    )

    worker.start()

if __name__== "__main__":
    main()
