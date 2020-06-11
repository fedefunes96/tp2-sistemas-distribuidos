#!/usr/bin/env python3

import os
import sys
import time
import logging
from chunk_manager.chunk_manager import ChunkManager

from configparser import ConfigParser, NoSectionError, NoOptionError
import os.path

CONFIG_FILE = 'config/config.ini'
DATA_FILE = 'data/data.csv'

def parse_config_params():
    if os.path.isfile(CONFIG_FILE):
        return read_from_config_file()
    
    return read_from_env()

def read_from_config_file():
    config_params = {}

    configParser = ConfigParser()
    configParser.read(CONFIG_FILE)

    config_params["queue_map"] = configParser.get('SETTINGS', 'QUEUE_MAP')
    config_params["queue_date"] = configParser.get('SETTINGS', 'QUEUE_DATE')
    config_params["queue_count"] = configParser.get('SETTINGS', 'QUEUE_COUNT')

    return config_params

def read_from_env():
    config_params = {}

    try:
        config_params["queue_map"] = os.environ["QUEUE_MAP"]
        config_params["queue_date"] = os.environ["QUEUE_DATE"]
        config_params["queue_count"] = os.environ["QUEUE_COUNT"]
    except KeyError as e:
        raise KeyError("Key was not found. Error: {}. Aborting server".format(e))
    except ValueError as e:
        raise ValueError("Key could not be parsed. Error: {}. Aborting server".format(e))
    
    return config_params	

def main():
    config_params = parse_config_params()
    
    chunk_manager = ChunkManager(
        config_params["queue_map"],
        config_params["queue_date"],
        config_params["queue_count"]
    )

    chunk_manager.process_data(DATA_FILE)

if __name__== "__main__":
    main()
