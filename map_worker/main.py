#!/usr/bin/env python3

import os
import sys
import time
import logging
from worker.worker import Worker

from configparser import ConfigParser, NoSectionError, NoOptionError
import os.path

CONFIG_FILE = 'config/config.ini'
PLACES_FILE = 'data/places.csv'

def parse_config_params():
    if os.path.isfile(CONFIG_FILE):
        return read_from_config_file()
    
    return read_from_env()

def read_from_config_file():
    config_params = {}

    configParser = ConfigParser()
    configParser.read(CONFIG_FILE)
            
    #config_params["ip"] = int(configParser.get('SETTINGS', 'SERVER_IP'))
    #config_params["port"] = int(configParser.get('SETTINGS', 'SERVER_PORT'))

    return config_params

def read_from_env():
    config_params = {}

    try:
        config_params["recv_queue"] = os.environ["RECV_QUEUE"]
        config_params["send_queue"] = os.environ["SEND_QUEUE"]
        config_params["master_queue"] = os.environ["MASTER_SEND_QUEUE"]
    except KeyError as e:
        raise KeyError("Key was not found. Error: {}. Aborting server".format(e))
    except ValueError as e:
        raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))
    
    return config_params	

def main():
    config_params = parse_config_params()

    time.sleep(15)

    worker = Worker(
        config_params["recv_queue"],
        config_params["send_queue"],
        config_params["master_queue"]
    )

    worker.start(PLACES_FILE)

if __name__== "__main__":
    main()
