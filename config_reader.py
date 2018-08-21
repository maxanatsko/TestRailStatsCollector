import configparser
import sys
import os

os.chdir(os.path.dirname(sys.argv[0]))

config = configparser.ConfigParser()
config.read("config.ini")