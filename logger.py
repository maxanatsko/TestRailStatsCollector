import logging
import argparse
from config_reader import config as cr

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="Specify log level: INFO/WARN/DEBUG", type=str.upper)
args = parser.parse_args()

log_level = cr.get('Dev', 'log_level', fallback='INFO').upper()

if args.log:
    log_level = args.log

logger = logging.getLogger()
valid_log_levels = {'INFO', 'WARN', 'DEBUG', 'ERROR', 'CRITICAL'}
log_level = log_level if log_level in valid_log_levels else 'INFO'
logger.setLevel(log_level)
handler = logging.FileHandler('system_log.log', 'a+', 'utf-8')
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
