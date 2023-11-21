import configparser
import sys
import os


def read_config(config_file):
    """
    Reads the configuration from the given file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        configparser.ConfigParser: The loaded configuration object.
    """
    config = configparser.ConfigParser()
    try:
        config_path = os.path.join(os.path.dirname(sys.argv[0]), config_file)
        config.read(config_path)
    except Exception as e:
        print(f"Error reading config file: {e}")
        sys.exit(1)
    return config


# Example usage
config = read_config("config.ini")
