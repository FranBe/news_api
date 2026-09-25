import configparser
from pathlib import Path
import os

class Config:

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent

        self.config_file = self.project_root / "config.ini"

        self.parser = configparser.ConfigParser()
        self.parser.read(self.config_file)


    @property
    def smtp_server(self):
        return self.parser.get("email", "smtp_server")

    @property
    def smtp_port(self):
        return self.parser.getint("email", "smtp_port")

    @property
    def recipients(self):
        return self.parser.get("email", "recipients")

    @property
    def url(self):
        return self.parser.get("news_api", "url")




    """
    def create_config(self, userName='username@mail.com', password='password',receivers=['receiver1@mail.com']):
        config = configparser.ConfigParser()
        # Add sections and key-value pairs
        config['General'] = {
            'debug': 'True',
            'log_path': '/log',
            'log_level': 'info'
        }
        config['Email'] = {
            'smtp_server' : 'smtp.gmail.com',
            'port' : '465',
            'username': userName,
            'password': password,
            'receivers': receivers
        }
        # Write the configuration to a file
        with open(self.configFile, 'w') as configfile:
            config.write(configfile)

    """
