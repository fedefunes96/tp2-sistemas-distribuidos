FROM rabbitmq-python-base:0.0.1

COPY count_controller /
COPY common/middleware /middleware
COPY common/redirector /redirector
COPY common/config_reader /config_reader

ENTRYPOINT ["/bin/sh"]
