import logging
import argparse
from config_reader import config as cr

# adding command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="you can pass --log (-l) argument: INFO/WARN/DEBUG", type=str)
# parse command-line arguments
args = parser.parse_args()

log_level = ""
#read config
log_level = cr.get('Dev', 'log_level')

# if log_level is null
if args.log is not None and log_level is None:
    log_level = args.log
if args.log is None and log_level is not None:
    log_level = log_level
else:
    log_level = "INFO"

logger = logging.getLogger()
logger.setLevel(log_level) # or whatever
handler = logging.FileHandler('system_log.log', 'a+', 'utf-8')
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

