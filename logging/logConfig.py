# https://python.civic-apps.com/logging-conf/
# https://docs.python.org/ja/3/howto/logging.html#configuring-logging
import logging.config

logging.config.fileConfig("log.conf")

logging.debug("debug message")
logging.info("info message")
logging.warn("warn message")
logging.error("error message")