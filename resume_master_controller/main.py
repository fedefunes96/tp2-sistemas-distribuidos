#!/usr/bin/env python3
from resume_master_controller.resume_master_controller import ResumeMasterController

from config_reader.config_reader import ConfigReader

def main():
    config_params = ConfigReader().parse_vars(
        ["RECV_QUEUE",
        "SEND_QUEUE",
        "TOTAL_WORKERS"]
    )

    master_controller = ResumeMasterController(
        config_params["RECV_QUEUE"],
        config_params["SEND_QUEUE"],
        int(config_params["TOTAL_WORKERS"])
    )

    master_controller.start()

if __name__== "__main__":
    main()
